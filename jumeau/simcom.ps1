# Pont vers IQANsimulate 7 par son interface COM (IQANsimulate.IQANsimulateControl2 / IQANProject2).
# Les canaux sont designes par leur nom IQANdesign. Un nom porte par plusieurs canaux se qualifie
# par son module : "Motor_Speed_Raw@Inverter_HVLP_j19". Un nom ambigu non qualifie est refuse.
# Mode -Fake : pas de simulateur, les valeurs ecrites sont relues telles quelles (essai des scripts).

$script:ACMODULE = 2
$script:ACCHANNEL = 4
$script:ENTREES = 'GPIN', 'GFIN', 'JPIN', 'JFIN', 'SPN', 'DM1IN', 'VIN', 'VIN32', 'DIN', 'DPCNT', 'APPIN', 'VDIN'

# GetComponent renvoie une structure (ComponentRecord) que PowerShell ne sait pas lire par IDispatch :
# la bibliotheque de types n'est pas enregistree. On appelle donc l'interface double par sa table
# virtuelle, declaree d'apres API\IQANsimulate.h.
if (-not ('IqanSim.Natif' -as [type])) {
    Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
namespace IqanSim {
    [StructLayout(LayoutKind.Sequential)]
    public struct ComponentRecord {
        [MarshalAs(UnmanagedType.BStr)] public string Name;
        public int Id;
        public int ComponentType;
        public byte ComponentSubType;
        [MarshalAs(UnmanagedType.BStr)] public string Unit;
        public short Controllable;
        public int ModuleId;
    }
    [ComImport, Guid("7888F8D8-D244-440E-AE18-287A4A4DEA98"), InterfaceType(ComInterfaceType.InterfaceIsDual)]
    public interface IIQANProject2 {
        ComponentRecord GetComponent(int componentType, int index);
        int GetComponentCount(int componentType);
        object GetComponentValue(int id);
        void SetComponentRawValue(int id, int value);
        int GetComponentRawValue(int id);
        int GetComponentStatus(int id);
        void SetComponentStatus(int id, int status);
        void SetComponentValue(int id, object value);
        [return: MarshalAs(UnmanagedType.BStr)] string GetComponentStatusText(int id);
        int GetCycletime();
        int GetInputCount();
        ComponentRecord GetInput(int index);
        int GetOutputCount();
        ComponentRecord GetOutput(int index);
        object GetProperty(int key, int id);
        [return: MarshalAs(UnmanagedType.BStr)] string GetComponentTypeName(int componentType, byte subType);
    }
    public static class Natif {
        // Appels compiles : PowerShell passerait par IDispatch, qui ne sait pas renvoyer la structure.
        public static ComponentRecord Composant(object prj, int type, int index) { return ((IIQANProject2)prj).GetComponent(type, index); }
        public static int Nombre(object prj, int type) { return ((IIQANProject2)prj).GetComponentCount(type); }
    }
}
'@
}

class SimCom {
    [object]$Sim
    [object]$Prj
    [object]$Nat
    [bool]$Fake
    [hashtable]$ParNom = @{}      # nom -> liste d'ids
    [hashtable]$ParQualif = @{}   # nom ou nom@qualifiant deja resolu -> id
    [hashtable]$Info = @{}        # id -> enregistrement
    [hashtable]$Valeurs = @{}     # mode Fake
    [int]$Cycle = 10              # ms
    [long]$TempsFake = 0

    SimCom([bool]$fake) { $this.Fake = $fake }

    [void] Ouvrir([string]$projet) {
        $this.Indexer($projet)
        if ($this.Fake) { return }
        $this.Sim = New-Object -ComObject IQANsimulate.IQANsimulateControl2
        if (-not $this.Sim.OpenFile($projet)) { throw "IQANsimulate refuse d'ouvrir $projet" }
        $this.Prj = New-Object -ComObject IQANsimulate.IQANProject2
        $this.Nat = 'IqanSim.Natif' -as [type]   # type charge par Add-Type, inconnu a l'analyse de la classe
        $this.Sim.StartSimulation(); $this.Sim.PauseSimulation()
        $c = $this.Prj.GetCycletime()
        if ($c -gt 0) { $this.Cycle = $c }
    }

    # IQANsimulate designe un canal par l'identifiant d'objet de l'export texte (BEGIN n) mais ne
    # liste pas les canaux par son API (GetComponentCount = 0). On lit donc les noms dans l'export
    # du projet simule (<projet>.canaux.csv, produit par index_export.py ; cree s'il manque).
    [void] Indexer([string]$projet) {
        $idx = "$projet.canaux.csv"
        if (-not (Test-Path $idx)) {
            $txt = [IO.Path]::ChangeExtension($projet, '.txt')
            if (-not (Test-Path $txt)) {
                $exe = 'C:\Program Files (x86)\IQANdesign 6.08\IQANdesign.exe'
                Start-Process $exe -ArgumentList "`"$projet`"", '-saveas', "`"$txt`"" -Wait
            }
            python -I (Join-Path $PSScriptRoot 'index_export.py') $txt $idx | Out-Null
        }
        foreach ($r in Import-Csv $idx -Delimiter ';' -Encoding UTF8) {
            $id = [int]$r.id
            $this.Info[$id] = [pscustomobject]@{ Id = $id; Nom = $r.nom; Type = $r.type; Appli = $r.appli; Chemin = $r.chemin }
            if (-not $this.ParNom.ContainsKey($r.nom)) { $this.ParNom[$r.nom] = New-Object System.Collections.ArrayList }
            [void]$this.ParNom[$r.nom].Add($id)
        }
    }

    # Entre homonymes : un qualifiant, sinon la MC42, sinon l'entree. "Nom" ou "Nom@qualifiant" : le qualifiant est un type (GPIN), une appli (MC42 app) ou un morceau
    # du chemin de groupes (E.Sevcon.M3.j19). A defaut, un nom unique dans la MC42 l'emporte.
    [int] Id([string]$nom) {
        if ($this.ParQualif.ContainsKey($nom)) { return $this.ParQualif[$nom] }
        $n = $nom; $q = $null
        $at = $nom.LastIndexOf('@')
        if ($at -gt 0) { $n = $nom.Substring(0, $at); $q = $nom.Substring($at + 1) }
        $ids = @($this.ParNom[$n])
        if (-not $this.ParNom.ContainsKey($n)) { throw "Canal inconnu : $n" }
        if ($q) { $ids = @($ids | Where-Object { $i = $this.Info[$_]; $i.Type -eq $q -or $i.Appli -eq $q -or $i.Chemin.Contains($q) }) }
        if ($ids.Count -gt 1) { $mc = @($ids | Where-Object { $this.Info[$_].Appli -eq 'MC42 app' }); if ($mc.Count -ge 1) { $ids = $mc } }
        # Puis l'entree (ce que les modeles ecrivent) plutot que le canal de calcul du meme nom.
        if ($ids.Count -gt 1) { $e = @($ids | Where-Object { $this.Info[$_].Type -in $script:ENTREES }); if ($e.Count -eq 1) { $ids = $e } }
        if ($ids.Count -ne 1) {
            $ou = ($this.ParNom[$n] | ForEach-Object { "$($this.Info[$_].Type) $($this.Info[$_].Chemin)" }) -join ' | '
            throw "Nom ambigu ou qualifiant sans effet : $nom ($ou)"
        }
        $this.ParQualif[$nom] = $ids[0]
        return $ids[0]
    }

    [bool] Existe([string]$nom) {
        try { [void]$this.Id($nom); return $true } catch { return $false }
    }
    [double] Lire([string]$nom) {
        if ($this.Fake) { if ($this.Valeurs.ContainsKey($nom)) { return $this.Valeurs[$nom] } return 0 }
        $v = $this.Prj.GetComponentValue($this.Id($nom))
        if ($v -is [bool]) { return [double][int]$v }
        return [double]$v
    }

    [void] Ecrire([string]$nom, [double]$valeur) {
        if ($this.Fake) { $this.Valeurs[$nom] = $valeur; return }
        $this.Prj.SetComponentValue($this.Id($nom), $valeur)
    }

    # Etat d'un canal ou d'une trame (perte CAN, defaut capteur). Codes a confirmer dans IQANsimulate.
    [void] Etat([string]$nom, [int]$statut) {
        if ($this.Fake) { $this.Valeurs["etat:$nom"] = $statut; return }
        $this.Prj.SetComponentStatus($this.Id($nom), $statut)
    }

    [string] TexteEtat([string]$nom) {
        if ($this.Fake) { return "$($this.Valeurs["etat:$nom"])" }
        return $this.Prj.GetComponentStatusText($this.Id($nom))
    }

    # Remet la simulation a zero (scenario suivant) sans rouvrir le projet ni redemander le mot de passe.
    [void] Relancer() { if ($this.Fake) { $this.TempsFake = 0; $this.Valeurs = @{}; return }; $this.Sim.StopSimulation(); $this.Sim.StartSimulation(); $this.Sim.PauseSimulation() }
    [void] Arreter() { if (-not $this.Fake) { $this.Sim.StopSimulation() } }

    # Avance de n cycles applicatifs, simulation en pause entre deux appels (deroulement reproductible).
    [void] Avancer([int]$n) {
        if ($this.Fake) { $this.TempsFake += $n * $this.Cycle; return }
        for ($i = 0; $i -lt $n; $i++) { $this.Sim.StepSimulation() }
    }

    [long] Temps() {
        if ($this.Fake) { return $this.TempsFake }
        return $this.Sim.GetCurrentTimestamp()
    }

    [object[]] Inventaire() { return @($this.Info.Values | Sort-Object Chemin, Nom) }
}
