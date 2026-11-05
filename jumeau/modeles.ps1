# Modeles simples des equipements du bateau, actifs seulement dans le jumeau (rien n'est ajoute au firmware).
# Chaque modele lit les sorties de la MC42 et ecrit les entrees que l'equipement reel enverrait.
# Les noms de canaux et les codes d'etat viennent du profil (profils/*.json) ; ceux marques
# "a_verifier" sont des hypotheses tirees de la lecture de la 108.3.1, a confirmer au premier essai.
# $Bus : table partagee entre modeles (tension du pack, courants, regime...).

class Modele {
    [SimCom]$S
    [object]$P            # section du profil
    [hashtable]$Bus
    [hashtable]$Pannes = @{}
    [hashtable]$Absents = @{}
    [string]$Nom

    Modele([SimCom]$s, [object]$p, [hashtable]$bus, [string]$nom) { $this.S = $s; $this.P = $p; $this.Bus = $bus; $this.Nom = $nom }

    [string] Canal([string]$cle) { $c = $this.P.canaux.$cle; if ($c) { return $c } return $null }

    [void] Ecrire([string]$cle, [double]$v) {
        $c = $this.Canal($cle)
        if (-not $c -or $this.Absents.ContainsKey($c)) { return }
        try { $this.S.Ecrire($c, $v) } catch { $this.Absents[$c] = $_.Exception.Message; Write-Warning "[$($this.Nom)] $c : $($_.Exception.Message)" }
    }

    [double] Lire([string]$cle, [double]$defaut) {
        $c = $this.Canal($cle)
        if (-not $c -or $this.Absents.ContainsKey($c)) { return $defaut }
        try { return $this.S.Lire($c) } catch { $this.Absents[$c] = $_.Exception.Message; Write-Warning "[$($this.Nom)] $c : $($_.Exception.Message)"; return $defaut }
    }

    # Perte CAN : les trames de l'equipement passent en defaut (timeout) et ses valeurs ne sont plus ecrites.
    [void] Panne([string]$type, [bool]$active) {
        if ($active) { $this.Pannes[$type] = $true } else { $this.Pannes.Remove($type) }
        if ($type -eq 'can') {
            $statut = if ($active) { [int]$this.P.statut_trame_perdue } else { [int]$this.P.statut_trame_ok }
            foreach ($t in $this.P.trames) { try { $this.S.Etat($t, $statut) } catch { Write-Warning "[$($this.Nom)] trame $t : $($_.Exception.Message)" } }
        }
    }

    [bool] EnPanne([string]$type) { return $this.Pannes.ContainsKey($type) }
    [void] Init([hashtable]$etat) { }
    [void] Pas([double]$dt) { }
}

# Batterie HV (profil Tyva). Courant = traction + pompe + auxiliaires - charge.
class Batterie : Modele {
    [double]$Soc = 80; [double]$Temp = 20; [bool]$Fermee = $false; [double]$Precharge = 0

    Batterie([SimCom]$s, [object]$p, [hashtable]$bus) : base($s, $p, $bus, 'batterie') { }

    [void] Init([hashtable]$etat) {
        if ($etat.ContainsKey('soc')) { $this.Soc = $etat.soc }
        if ($etat.ContainsKey('temperature')) { $this.Temp = $etat.temperature }
        $this.Bus.tension_pack = $this.Tension(0)
    }

    [double] Tension([double]$i) {
        $p = $this.P
        $ocv = $p.v_cell_vide + ($p.v_cell_plein - $p.v_cell_vide) * $this.Soc / 100
        return $p.cellules * $ocv - $p.resistance_ohm * $i
    }

    [void] Pas([double]$dt) {
        $p = $this.P
        # Demande de fermeture des contacteurs : sortie MC42 si le profil la connait, sinon fermee d'office.
        $demande = if ($this.Canal('demande_marche')) { $this.Lire('demande_marche', 0) -eq [double]$p.valeur_demande_marche } else { $true }
        if ($demande -and -not $this.EnPanne('defaut')) { $this.Precharge = [Math]::Min($this.Precharge + $dt, $p.precharge_s + 1) } else { $this.Precharge = 0 }
        $this.Fermee = $this.Precharge -ge $p.precharge_s

        $i = 0.0
        if ($this.Fermee) { $i = [double]$this.Bus.courant_traction + [double]$this.Bus.courant_pompe + $p.courant_aux_a - [double]$this.Bus.courant_charge }
        $this.Soc = [Math]::Max(0, [Math]::Min(100, $this.Soc - $i * $dt / 3600 / $p.capacite_ah * 100))
        $chauffe = $i * $i * $p.resistance_ohm * $p.k_chauffe
        if ($this.EnPanne('surchauffe')) { $chauffe += 0.5 }
        $this.Temp += ($chauffe - ($this.Temp - $p.t_ambiante) / $p.tau_thermique_s) * $dt
        $v = $this.Tension($i)
        $this.Bus.tension_pack = $v
        $this.Bus.tension_bus = if ($this.Fermee) { $v } else { 0 }
        $this.Bus.courant_batterie = $i
        $this.Bus.soc = $this.Soc

        if ($this.EnPanne('can')) { return }
        $vc = $v / $p.cellules
        $ecart = if ($this.EnPanne('desequilibre')) { $p.desequilibre_mv / 1000 } else { 0.005 }
        $e = $p.codes
        $this.Ecrire('soc', $this.Soc)
        $this.Ecrire('soh', 100)
        $this.Ecrire('tension', $v)
        $this.Ecrire('courant', $i)
        $this.Ecrire('v_cell_min', ($vc - $ecart / 2) * $p.echelle_v_cell)
        $this.Ecrire('v_cell_max', ($vc + $ecart / 2) * $p.echelle_v_cell)
        $this.Ecrire('t_cell_max', $this.Temp + 1)
        $this.Ecrire('t_cell_min', $this.Temp - 1)
        $this.Ecrire('t_cell_moy', $this.Temp)
        $this.Ecrire('t_pdu', $this.Temp + 3)
        $etat = if ($this.EnPanne('defaut')) { $e.etat_defaut } elseif ($this.Bus.courant_charge -gt 0 -and $this.Fermee) { $e.etat_charge } elseif ($this.Fermee) { $e.etat_decharge } else { $e.etat_attente }
        $this.Ecrire('etat_bms', $etat)
        $this.Ecrire('pret', [int](-not $this.EnPanne('defaut')))
        $this.Ecrire('decharge_possible', [int](-not $this.EnPanne('defaut')))
        $this.Ecrire('charge_possible', [int]($this.Soc -lt 100 -and -not $this.EnPanne('defaut')))
        $this.Ecrire('relais_decharge', [int]$this.Fermee)
        $this.Ecrire('relais_charge', [int]$this.Fermee)
        $this.Ecrire('relais_precharge', [int]($this.Precharge -gt 0 -and -not $this.Fermee))
        $this.Ecrire('isolement', $(if ($this.EnPanne('isolement')) { $p.isolement_defaut_kohm } else { $p.isolement_ok_kohm }))
        $this.Ecrire('erreur_surtemperature', [int]($this.Temp -gt $p.t_alarme))
        $this.Ecrire('erreur_sous_tension', [int]($vc -lt $p.v_cell_vide))
    }
}

# Variateur de chenille (Sevcon gen4, M1 droite ou M2 gauche). Vitesse = consigne filtree.
class Variateur : Modele {
    [double]$Vitesse = 0; [double]$TempRad = 20; [double]$TempMot = 20

    Variateur([SimCom]$s, [object]$p, [hashtable]$bus, [string]$nom) : base($s, $p, $bus, $nom) { }

    [void] Pas([double]$dt) {
        $p = $this.P
        $consigne = $this.Lire('consigne', 0)          # tension de throttle envoyee par la MC42
        $avant = $this.Lire('avant', 0) -ne 0
        $arriere = $this.Lire('arriere', 0) -ne 0
        $sens = if ($avant -and -not $arriere) { 1 } elseif ($arriere -and -not $avant) { -1 } else { 0 }
        $alimente = [double]$this.Bus.tension_bus -gt $p.tension_min
        $cible = if ($alimente -and -not $this.EnPanne('defaut')) { $sens * [Math]::Min(1, [Math]::Abs($consigne) / $p.consigne_pleine) * $p.vitesse_max_rpm } else { 0 }
        $acc = ($cible - $this.Vitesse) / $p.tau_s
        $this.Vitesse += $acc * $dt
        $couple = $p.couple_frottement_nm * [Math]::Sign($this.Vitesse) + $p.inertie * $acc
        $courant = [Math]::Abs($couple * $this.Vitesse) / [Math]::Max(1, [double]$this.Bus.tension_bus) * 0.105 + $(if ($alimente) { 2 } else { 0 })
        $this.Bus["courant_$($this.Nom)"] = $courant
        $this.TempRad += ($courant * $p.k_chauffe - ($this.TempRad - $p.t_ambiante) / $p.tau_thermique_s) * $dt
        $this.TempMot += ($courant * $p.k_chauffe * 0.8 - ($this.TempMot - $p.t_ambiante) / $p.tau_thermique_s) * $dt

        if ($this.EnPanne('can')) { return }
        $this.Ecrire('vitesse', $this.Vitesse)
        $this.Ecrire('courant', $courant)
        $this.Ecrire('couple', $couple)
        $this.Ecrire('tension', [double]$this.Bus.tension_bus)
        $this.Ecrire('t_radiateur', $this.TempRad)
        $this.Ecrire('t_moteur', $this.TempMot)
        $this.Ecrire('statut', $(if ($alimente) { $p.codes.statut_marche } else { $p.codes.statut_arret }))
        $this.Ecrire('erreur', $(if ($this.EnPanne('defaut')) { $p.codes.erreur_defaut } else { 0 }))
    }
}

# Variateur de la pompe hydraulique HVLP (Sevcon, J1939 ou CANopen).
class Pompe : Modele {
    [double]$Vitesse = 0; [double]$Temp = 20

    Pompe([SimCom]$s, [object]$p, [hashtable]$bus) : base($s, $p, $bus, 'pompe') { }

    [void] Pas([double]$dt) {
        $p = $this.P
        $demande = $this.Lire('couple_demande', 0)
        $marche = $this.Lire('mot_etat_demande', 0) -ne 0 -and [double]$this.Bus.tension_bus -gt $p.tension_min -and -not $this.EnPanne('defaut')
        $cible = if ($marche) { [Math]::Min($p.vitesse_max_rpm, [Math]::Abs($demande) * $p.rpm_par_unite_couple) } else { 0 }
        $this.Vitesse += ($cible - $this.Vitesse) / $p.tau_s * $dt
        $courant = if ($marche) { $p.courant_marche_a * $this.Vitesse / $p.vitesse_max_rpm + 1 } else { 0 }
        $this.Bus.courant_pompe = $courant
        $this.Temp += ($courant * $p.k_chauffe - ($this.Temp - $p.t_ambiante) / $p.tau_thermique_s) * $dt

        if ($this.EnPanne('can')) { return }
        $this.Ecrire('mot_etat', $(if ($this.EnPanne('defaut')) { $p.codes.etat_defaut } elseif ($marche) { $p.codes.etat_marche } else { $p.codes.etat_pret }))
        $this.Ecrire('vitesse', $this.Vitesse)
        $this.Ecrire('tension', [double]$this.Bus.tension_bus)
        $this.Ecrire('couple', $demande)
        $this.Ecrire('t_radiateur', $this.Temp)
        $this.Ecrire('t_moteur', $this.Temp - 5)
        $this.Ecrire('erreur', $(if ($this.EnPanne('defaut')) { $p.codes.erreur_defaut } else { 0 }))
    }
}

# Moteur thermique J1939 (EB2). Demarre quand la MC42 actionne le demarreur, regime vers la consigne TSC1.
class MoteurThermique : Modele {
    [double]$Regime = 0; [double]$Eau = 20; [string]$Etat = 'arret'; [double]$Lancement = 0

    MoteurThermique([SimCom]$s, [object]$p, [hashtable]$bus) : base($s, $p, $bus, 'moteur') { }

    [void] Init([hashtable]$etat) { if ($etat.ContainsKey('t_eau')) { $this.Eau = $etat.t_eau } }

    [void] Pas([double]$dt) {
        $p = $this.P
        $demarreur = $this.Lire('demarreur', 0) -ne 0
        $contact = if ($this.Canal('contact')) { $this.Lire('contact', 1) -ne 0 } else { $true }
        if (-not $contact -or $this.EnPanne('calage')) { $this.Etat = 'arret' }
        elseif ($this.Etat -eq 'arret' -and $demarreur) { $this.Etat = 'lancement'; $this.Lancement = 0 }
        elseif ($this.Etat -eq 'lancement') { $this.Lancement += $dt; if ($this.Lancement -ge $p.duree_lancement_s) { $this.Etat = 'marche' } elseif (-not $demarreur) { $this.Etat = 'arret' } }
        $consigne = $this.Lire('consigne_regime', 0)
        $cible = switch ($this.Etat) { 'marche' { [Math]::Max($p.ralenti_rpm, [Math]::Min($p.regime_max_rpm, $consigne)) } 'lancement' { $p.regime_lancement_rpm } default { 0 } }
        $this.Regime += ($cible - $this.Regime) / $p.tau_s * $dt
        $charge = if ($this.Etat -eq 'marche') { [Math]::Min(100, 15 + 60 * ($this.Regime - $p.ralenti_rpm) / ($p.regime_max_rpm - $p.ralenti_rpm)) } else { 0 }
        $vers = if ($this.Etat -eq 'marche') { $p.t_eau_regulee } else { $p.t_ambiante }
        if ($this.EnPanne('surchauffe') -and $this.Etat -eq 'marche') { $vers = 115 }
        $this.Eau += ($vers - $this.Eau) / $p.tau_thermique_s * $dt
        $this.Bus.regime_moteur = $this.Regime

        if ($this.EnPanne('can')) { return }
        $this.Ecrire('regime', $this.Regime)
        $this.Ecrire('charge', $charge)
        $this.Ecrire('couple', $charge)
        $this.Ecrire('t_eau', $this.Eau)
        $this.Ecrire('pression_huile', $(if ($this.Etat -eq 'marche') { $p.pression_huile_kpa } else { 0 }))
    }
}

# Chargeur embarque (profil Elcon). Branche quand le scenario met la prise secteur ; debite si la MC42 l'autorise.
class Chargeur : Modele {
    [bool]$Secteur = $false; [double]$Courant = 0; [double]$Temp = 20

    Chargeur([SimCom]$s, [object]$p, [hashtable]$bus) : base($s, $p, $bus, 'chargeur') { }

    [void] Pas([double]$dt) {
        $p = $this.P
        $autorise = $this.Lire('autorisation', 0) -eq [double]$p.valeur_autorisation
        $limite = $this.Lire('courant_max', $p.courant_nominal_a)
        $cible = if ($this.Secteur -and $autorise -and -not $this.EnPanne('defaut')) { [Math]::Min($p.courant_nominal_a, [Math]::Max(0, $limite)) } else { 0 }
        if ([double]$this.Bus.soc -ge 99.5) { $cible = [Math]::Min($cible, 1) }
        $this.Courant += ($cible - $this.Courant) / $p.tau_s * $dt
        $this.Bus.courant_charge = $this.Courant
        $this.Temp += ($this.Courant * $p.k_chauffe - ($this.Temp - $p.t_ambiante) / $p.tau_thermique_s) * $dt

        if ($this.EnPanne('can') -or -not $this.Secteur) { return }
        $this.Ecrire('tension_secteur', 230)
        $this.Ecrire('courant_sortie', $this.Courant)
        $this.Ecrire('tension_sortie', [double]$this.Bus.tension_pack)
        $this.Ecrire('temperature', $this.Temp)
        $this.Ecrire('defaut_materiel', [int]$this.EnPanne('defaut'))
        $this.Ecrire('etat', $(if ($this.Courant -gt 1) { $p.codes.etat_charge } else { $p.codes.etat_attente }))
        $this.Ecrire('etat_com', $p.codes.com_ok)
    }
}

# Clavier CAN Blink 8 touches : battement de coeur et code de la touche appuyee.
class Clavier : Modele {
    [string]$Touche = ''; [double]$Reste = 0

    Clavier([SimCom]$s, [object]$p, [hashtable]$bus) : base($s, $p, $bus, 'clavier') { }

    [void] Appuyer([string]$touche, [double]$duree) { $this.Touche = $touche; $this.Reste = $duree }

    [void] Pas([double]$dt) {
        if ($this.EnPanne('can')) { return }
        $this.Ecrire('etat', $this.P.codes.operationnel)
        if ($this.Reste -gt 0) { $this.Reste -= $dt; $code = $this.P.touches.($this.Touche) } else { $code = 0 }
        $this.Ecrire('touches', $code)
    }
}

# Fabrique a partir des sections presentes dans le profil.
function New-Modeles([SimCom]$s, [object]$profil, [hashtable]$bus) {
    $m = [ordered]@{}
    if ($profil.batterie) { $m.batterie = [Batterie]::new($s, $profil.batterie, $bus) }
    if ($profil.variateur_droit) { $m.variateur_droit = [Variateur]::new($s, $profil.variateur_droit, $bus, 'variateur_droit') }
    if ($profil.variateur_gauche) { $m.variateur_gauche = [Variateur]::new($s, $profil.variateur_gauche, $bus, 'variateur_gauche') }
    if ($profil.pompe) { $m.pompe = [Pompe]::new($s, $profil.pompe, $bus) }
    if ($profil.moteur) { $m.moteur = [MoteurThermique]::new($s, $profil.moteur, $bus) }
    if ($profil.chargeur) { $m.chargeur = [Chargeur]::new($s, $profil.chargeur, $bus) }
    if ($profil.clavier) { $m.clavier = [Clavier]::new($s, $profil.clavier, $bus) }
    return $m
}
