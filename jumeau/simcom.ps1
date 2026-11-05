# Pont vers IQANsimulate 7 par son interface COM (IQANsimulate.IQANsimulateControl2 / IQANProject2).
# Les canaux sont designes par leur nom IQANdesign. Un nom porte par plusieurs canaux se qualifie
# par son module : "Motor_Speed_Raw@Inverter_HVLP_j19". Un nom ambigu non qualifie est refuse.
# Mode -Fake : pas de simulateur, les valeurs ecrites sont relues telles quelles (essai des scripts).

$script:ACMODULE = 2
$script:ACCHANNEL = 4

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
        public static IIQANProject2 Projet(object rcw) { return (IIQANProject2)rcw; }
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
    [hashtable]$ParQualif = @{}   # nom@module -> id
    [hashtable]$Info = @{}        # id -> enregistrement
    [hashtable]$Valeurs = @{}     # mode Fake
    [int]$Cycle = 10              # ms
    [long]$TempsFake = 0

    SimCom([bool]$fake) { $this.Fake = $fake }

    [void] Ouvrir([string]$projet) {
        if ($this.Fake) { return }
        $this.Sim = New-Object -ComObject IQANsimulate.IQANsimulateControl2
        if (-not $this.Sim.OpenFile($projet)) { throw "IQANsimulate refuse d'ouvrir $projet" }
        $this.Prj = New-Object -ComObject IQANsimulate.IQANProject2
        $this.Nat = [IqanSim.Natif]::Projet($this.Prj)
        # La liste des canaux n'est remplie qu'une fois la simulation lancee.
        $this.Sim.StartSimulation(); $this.Sim.PauseSimulation()
        $this.Indexer()
        $c = $this.Prj.GetCycletime()
        if ($c -gt 0) { $this.Cycle = $c }
    }

    [void] Indexer() {
        $modules = @{}
        $n = $this.Prj.GetComponentCount($script:ACMODULE)
        for ($i = 0; $i -lt $n; $i++) { $m = $this.Nat.GetComponent($script:ACMODULE, $i); $modules[[int]$m.Id] = $m.Name }
        $n = $this.Prj.GetComponentCount($script:ACCHANNEL)
        for ($i = 0; $i -lt $n; $i++) {
            $c = $this.Nat.GetComponent($script:ACCHANNEL, $i)
            $mod = $modules[[int]$c.ModuleId]
            $this.Info[[int]$c.Id] = [pscustomobject]@{ Id = [int]$c.Id; Nom = $c.Name; Module = $mod; Unite = $c.Unit; Pilotable = [bool]$c.Controllable; SousType = [int]$c.ComponentSubType }
            if (-not $this.ParNom.ContainsKey($c.Name)) { $this.ParNom[$c.Name] = New-Object System.Collections.ArrayList }
            [void]$this.ParNom[$c.Name].Add([int]$c.Id)
            if ($mod) { $this.ParQualif["$($c.Name)@$mod"] = [int]$c.Id }
        }
    }

    [int] Id([string]$nom) {
        if ($this.ParQualif.ContainsKey($nom)) { return $this.ParQualif[$nom] }
        $ids = $this.ParNom[$nom]
        if (-not $ids) { throw "Canal inconnu dans le simulateur : $nom" }
        if ($ids.Count -gt 1) {
            $mods = ($ids | ForEach-Object { $this.Info[$_].Module }) -join ', '
            throw "Nom ambigu : $nom (modules $mods). Qualifier avec @module."
        }
        return $ids[0]
    }

    [bool] Existe([string]$nom) {
        if ($this.Fake) { return $true }
        return $this.ParQualif.ContainsKey($nom) -or ($this.ParNom.ContainsKey($nom) -and $this.ParNom[$nom].Count -eq 1)
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

    [void] Demarrer() { }
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

    # Liste des canaux pour verifier les noms et ce qui est pilotable.
    [object[]] Inventaire() { return @($this.Info.Values | Sort-Object Module, Nom) }
}
