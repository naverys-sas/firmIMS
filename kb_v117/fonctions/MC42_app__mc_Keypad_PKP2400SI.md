# MC42 app — mc.Keypad_PKP2400SI

3 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## mc.Keypad_PKP2400SI
> 8 boutons

#### FSM Keypad X100  `FSM`
- Propriétés : Store value=No
- État 0 **Default state**
- Utilisé par : *(personne)*
- Ligne export : 103375 · id 241124

#### heart  `GFIN`
- Propriétés : Identifier=0x715 · Data length=Dont care · Paged protocol={Not used} · Parameters={{heartbeat; 0}} · Module=Keypad PKP_2400_SI (Generic) · Module index=0
- Lit : `heartbeat`
- Utilisé par : *(personne)*
- Ligne export : 103407 · id 241140

#### heartbeat  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `heart`
- Ligne export : 103426 · id 241141
