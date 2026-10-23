# MC42 app — mc.d3 Screen State

29 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.d3 Screen State

#### VIEW SOC md3 d3  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `lin(Battery SOC Customer [%]: 0->12, 100->83, Freeze)`
- Lit : `Battery SOC Customer`
- Utilisé par : `SOC Scroller Limit d3`
- Ligne export : 54463 · id 166719

#### VIEW BAT Ready d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(E.Power Management System = 1) AND (not(Repeated errors locker))`
  - **Blocking** = `Charger State Feed-back = 2`
- Lit : `Charger State Feed-back`, `E.Power Management System`, `Repeated errors locker`
- Utilisé par : *(personne)*
- Ligne export : 54510 · id 166727

#### VIEW BAT Charging d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 3`
- Lit : `E.Power Management System`
- Utilisé par : *(personne)*
- Ligne export : 54572 · id 166737

#### VIEW BAT Run d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `E.Power Management System = 2`
  - **Blocking** = `Charger State Feed-back = 2`
- Lit : `Charger State Feed-back`, `E.Power Management System`
- Utilisé par : *(personne)*
- Ligne export : 54617 · id 166745

#### VIEW Power State d3  `SP`
- Propriétés : Input channel=Power State Int d3 · Default state name=Off · States={Starting; Run}
- Lit : `Power State Int d3`
- Utilisé par : *(personne)*
- Ligne export : 54671 · id 166754

#### SOC Scroller Limit d3  `MAC`
- Propriétés : Unit=ms
- Logique :
  ```qcode
  Result:= VIEW SOC md3 d3 * 50
  ```
- Lit : `VIEW SOC md3 d3`
- Utilisé par : `SOC Scroller d3`
- Ligne export : 54684 · id 166800

#### SOC Scroller d3  `TMR`
- Propriétés : Type (Unit)=Milliseconds [ms] · Store value=No · Reset value=SOC Scroller Limit d3 [ms]
- Logique :
  - **Increasing** = `Charger State Feed-back = 4`
  - **Resetting** = `(SOC Scroller d3 [ms] >= 5000) OR (Charger State Feed-back <> 4)`
- Lit : `Charger State Feed-back`, `SOC Scroller Limit d3`
- Utilisé par : `SOC Display d3`
- Ligne export : 54702 · id 166778

#### SOC Display d3  `MAC`
- Logique :
  ```qcode
  Result:= SOC Scroller d3 / 50
  ```
- Lit : `SOC Scroller d3`
- Utilisé par : *(personne)*
- Ligne export : 54774 · id 166790

#### Power State Int E  `IMAC`
- Logique :
  - **Controlling** = `Electric Engine State Feed-back`
- Lit : `Electric Engine State Feed-back`
- Utilisé par : `Power State Int d3`
- Ligne export : 54803 · id 208690

#### Power State Int T  `IMAC`
- Logique :
  - **Controlling** = `T Engine State mc`
- Lit : `T Engine State mc`
- Utilisé par : `Power State Int d3`
- Ligne export : 54844 · id 208698

#### Power State Int d3  `IMAC`
- Logique :
  - **Controlling** = `Power State Int E + Power State Int T`
- Lit : `Power State Int E`, `Power State Int T`
- Utilisé par : `VIEW Power State d3`, `off d3`, `ready d3`, `starting d3`
- Ligne export : 54885 · id 208706

#### e State All Speed d3 Int  `IMAC`
- Logique :
  - **Controlling** = `e State All Speed`
- Lit : `e State All Speed`
- Utilisé par : `Speed All State d3 int`
- Ligne export : 54942 · id 209477

#### T State All Speed d3 Int  `IMAC`
- Logique :
  - **Controlling** = `T State All Speed`
- Lit : `T State All Speed`
- Utilisé par : `Speed All State d3 int`
- Ligne export : 54983 · id 209485

#### Speed All State d3 int  `IMAC`
- Logique :
  - **Controlling** = `e State All Speed d3 Int + T State All Speed d3 Int`
- Lit : `T State All Speed d3 Int`, `e State All Speed d3 Int`
- Utilisé par : `fast d3`, `fast d3 safetyoff`, `s.slow d3`, `s.slow d3 safetyoff`, `slow d3`, `slow d3 safetyoff`
- Ligne export : 55024 · id 209493

#### e Up/DOWN STATE d3 Int  `IMAC`
- Logique :
  - **Controlling** = `E State Up/Down`
- Lit : `E State Up/Down`
- Utilisé par : `Up/DOWN STATE d3 Int`
- Ligne export : 55081 · id 209564

#### T Up/DOWN STATE d3 Int  `IMAC`
- Logique :
  - **Controlling** = `T State Up/Down`
- Lit : `T State Up/Down`
- Utilisé par : `Up/DOWN STATE d3 Int`
- Ligne export : 55122 · id 209572

#### Up/DOWN STATE d3 Int  `IMAC`
- Logique :
  - **Controlling** = `e Up/DOWN STATE d3 Int + T Up/DOWN STATE d3 Int`
- Lit : `T Up/DOWN STATE d3 Int`, `e Up/DOWN STATE d3 Int`
- Utilisé par : `display up d3`, `down d3`, `interm d3`, `ready d3`
- Ligne export : 55163 · id 209580

#### off d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power State Int d3 = 0`
- Lit : `Power State Int d3`
- Utilisé par : `display up d3`, `down d3`, `fast d3`, `fast d3 safetyoff`, `interm d3`, `s.slow d3`, `s.slow d3 safetyoff`, `slow d3`, `slow d3 safetyoff`
- Ligne export : 55220 · id 209841

#### starting d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Power State Int d3 = 1`
- Lit : `Power State Int d3`
- Utilisé par : `display up d3`, `down d3`, `fast d3`, `fast d3 safetyoff`, `interm d3`, `s.slow d3`, `s.slow d3 safetyoff`, `slow d3`, `slow d3 safetyoff`
- Ligne export : 55265 · id 209852

#### ready d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(Power State Int d3 = 2) AND (Up/DOWN STATE d3 Int = 3)`
- Lit : `Power State Int d3`, `Up/DOWN STATE d3 Int`
- Utilisé par : *(personne)*
- Ligne export : 55310 · id 209869

#### interm d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Up/DOWN STATE d3 Int = 2`
  - **Blocking** = `(starting d3) OR (off d3)`
- Lit : `Up/DOWN STATE d3 Int`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55364 · id 209886

#### display up d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Up/DOWN STATE d3 Int = 4`
  - **Blocking** = `(starting d3) OR (off d3) OR (Up/DOWN STATE d3 Int = 3)`
- Lit : `Up/DOWN STATE d3 Int`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55423 · id 209903

#### down d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Up/DOWN STATE d3 Int = 1`
  - **Blocking** = `(starting d3) OR (off d3)`
- Lit : `Up/DOWN STATE d3 Int`, `off d3`, `starting d3`
- Utilisé par : `fast d3`, `fast d3 safetyoff`, `s.slow d3`, `s.slow d3 safetyoff`, `slow d3`, `slow d3 safetyoff`
- Ligne export : 55491 · id 209948

#### slow d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 2`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (Safety_disable mc)`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55550 · id 209955

#### fast d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 4`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (Safety_disable mc)`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55624 · id 209962

#### s.slow d3  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 3`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (Safety_disable mc)`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55698 · id 209969

#### slow d3 safetyoff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 2`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (not(Safety_disable mc))`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55772 · id 212597

#### fast d3 safetyoff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 4`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (not(Safety_disable mc))`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55847 · id 212608

#### s.slow d3 safetyoff  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Speed All State d3 int = 3`
  - **Blocking** = `(starting d3) OR (off d3) OR (not(down d3)) OR (not(Safety_disable mc))`
- Lit : `Safety_disable mc`, `Speed All State d3 int`, `down d3`, `off d3`, `starting d3`
- Utilisé par : *(personne)*
- Ligne export : 55922 · id 212619
