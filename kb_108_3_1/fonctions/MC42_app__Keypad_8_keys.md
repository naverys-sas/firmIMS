# MC42 app — Keypad 8 keys

73 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## Keypad 8 keys — actif seulement si `Keypad 8 keys`

#### FSM keypad  `FSM`
- Propriétés : Store value=No
- État 0 **Default state**
  - transition *0 - 2* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 5`
  - transition *0 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 127`
  - transition *0 - 3* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 4`
- État 1 **Pre-operational**
  - transition *1 - 2* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 5`
  - transition *1 - 3* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 4`
  - transition *1 - 0* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 0`
- État 2 **Operational**
  - transition *2 - 3* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 4`
  - transition *2 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 127`
  - transition *2 - 0* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 0`
- État 3 **Stop**
  - transition *3 - 0* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 0`
  - transition *3 - 2* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 5`
  - transition *3 - 1* (état cible non exporté par IQANdesign)
    - **Activating** = `Heartbeat/statut = 127`
- Lit : `Heartbeat/statut`
- Utilisé par : `Statut stop`, `statut pre-op`
- Ligne export : 103911 · id 241136

#### Start/Stop keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `keys number = 1`
- Lit : `keys number`
- Utilisé par : `B9`, `blue led #1`, `red led#1`
- Ligne export : 105175 · id 241218

#### Free keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(keys number = 2) AND (BUTTON DRIVE 4ET)`
- Lit : `BUTTON DRIVE 4ET`, `keys number`
- Utilisé par : `B8 F4 Speed Free 4ET FREE Sel`
- Ligne export : 105220 · id 241583

#### No heartbeat  `IDC`
- Propriétés : Toggle=No · Delay on=500 · Delay off=0
- Logique :
  - **Activating** = `heartbeat Status = Timeout`
- Lit : `heartbeat`
- Utilisé par : `Keypad HS`
- Ligne export : 105272 · id 241608

#### Keypad HS  `CMSG`
- Propriétés : Show message=All · Dialog type=Warning · Header=Keypad is not working · Text=Use this touch screen to run the IMS.
- Logique :
  - **Showing** = `(No heartbeat) OR (Statut stop) OR (statut pre-op)`
- Lit : `No heartbeat`, `Statut stop`, `statut pre-op`
- Utilisé par : *(personne)*
- Ligne export : 105317 · id 241620

#### Up Keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(keys number = 8) AND (T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `keys number`
- Utilisé par : `down keypad toggle`, `keypad up quick`, `keypad up wait`, `up keypad toggle`, `up or down keypad`
- Ligne export : 105377 · id 241631

#### Down Keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(keys number = 128) AND (T Engine_Started mc)`
- Lit : `T Engine_Started mc`, `keys number`
- Utilisé par : `down keypad toggle`, `keypad down quick`, `keypad down wait`, `up keypad toggle`, `up or down keypad`
- Ligne export : 105429 · id 241639

#### Slow keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `keys number = 16`
- Lit : `keys number`
- Utilisé par : `45 Speed state`
- Ligne export : 105481 · id 241676

#### Normal keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `keys number = 32`
- Lit : `keys number`
- Utilisé par : `45 Speed state`
- Ligne export : 105526 · id 241684

#### Fast keypad  `IDC`
> s'active quand le bouton concerné est enfoncé
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `keys number = 64`
- Lit : `keys number`
- Utilisé par : `45 Speed state`
- Ligne export : 105571 · id 241692

#### blue led #1  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (Start/Stop keypad = 1 or T Engine_Started mc = 1) then
  Result := 1
  else
  Result := 0
  endif
  if (red led#1 = 1) then
  Result := 0
  endif
  ```
- Lit : `Start/Stop keypad`, `T Engine_Started mc`, `red led#1`
- Utilisé par : `blue led #1`
- Ligne export : 105616 · id 241710

#### blue led #5  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (Voyant  slow = 1) then
  Result := 1
  else
  Result := 0
  endif
  ```
- Lit : `Voyant  slow`
- Utilisé par : `blue led #5`
- Ligne export : 105641 · id 241728

#### blue led #6  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (voyant normal = 1) then
  Result := 1
  else
  Result := 0
  endif
  ```
- Lit : `voyant normal`
- Utilisé par : `blue led #6`
- Ligne export : 105663 · id 241741

#### blue led #7  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (voyant fast = 1) then
  Result := 1
  else
  Result := 0
  endif
  ```
- Lit : `voyant fast`
- Utilisé par : `blue led #7`
- Ligne export : 105685 · id 241754

#### red led#1  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (Start/Stop keypad = 1 and T Engine_Started mc = 1) then
  Result := 1
  else
  Result := 0
  endif
  ```
- Lit : `Start/Stop keypad`, `T Engine_Started mc`
- Utilisé par : `blue led #1`, `red led#1`
- Ligne export : 105707 · id 241767

#### blue led #2  `MAC`
> activation ou non du bit correspondant au nom de la channel
- Logique :
  ```qcode
  if (Voyant free = 1) then
  Result := 1
  else
  Result := 0
  endif
  ```
- Lit : `Voyant free`
- Utilisé par : `blue led#2`
- Ligne export : 105729 · id 241782

#### up or down keypad  `SMC`
> permet de savoir quel bouton entre "up" or "down" est enfoncé en dernier pour faire clignoter le bon bouton lors de la montée ou descente des bras
- Propriétés : Default state name=Default state
- Fonction *Click Up* :
  - **Activating** = `(up keypad toggle) OR (B1 up toggle)`
  - **Blocking** = `(Down Keypad) OR (B2 Virtual DOWN 4ETDOWN sel)`
- Fonction *Click Down* :
  - **Activating** = `(down keypad toggle) OR (B2 down toggle)`
  - **Blocking** = `(Up Keypad) OR (B1 Virtual UP 4ETUP sel)`
- Lit : `B1 Virtual UP 4ETUP sel`, `B1 up toggle`, `B2 Virtual DOWN 4ETDOWN sel`, `B2 down toggle`, `Down Keypad`, `Up Keypad`, `down keypad toggle`, `up keypad toggle`
- Utilisé par : `Blue led blink #4`, `Blue led blink #8`
- Ligne export : 105751 · id 241868

#### Blue led blink #4  `IDC`
> activation ou non du bit correspondant au nom de la channel
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(up or down keypad = 1) AND (T State Up/Down = 2)`
- Lit : `T State Up/Down`, `up or down keypad`
- Utilisé par : `Blue led blink #4`
- Ligne export : 105864 · id 241879

#### Blue led blink #8  `IDC`
> activation ou non du bit correspondant au nom de la channel
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(up or down keypad = 2) AND (T State Up/Down = 2)`
- Lit : `T State Up/Down`, `up or down keypad`
- Utilisé par : `Blue led blink #8`
- Ligne export : 105918 · id 241884

#### blue led #4  `IDC`
> activation ou non du bit correspondant au nom de la channel
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T State Up/Down = 3`
- Lit : `T State Up/Down`
- Utilisé par : `Blue led #4`
- Ligne export : 105972 · id 241942

#### blue led #8  `IDC`
> activation ou non du bit correspondant au nom de la channel
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `T State Up/Down = 1`
- Lit : `T State Up/Down`
- Utilisé par : `blue led #8`
- Ligne export : 106017 · id 241946

#### up keypad toggle  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Up Keypad`
  - **Blocking** = `Down Keypad`
- Lit : `Down Keypad`, `Up Keypad`
- Utilisé par : `up or down keypad`
- Ligne export : 106062 · id 242089

#### down keypad toggle  `IDC`
- Propriétés : Toggle=Yes · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Down Keypad`
  - **Blocking** = `Up Keypad`
- Lit : `Down Keypad`, `Up Keypad`
- Utilisé par : `up or down keypad`
- Ligne export : 106112 · id 242093

#### Statut stop  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `FSM keypad = 3`
- Lit : `FSM keypad`
- Utilisé par : `Keypad HS`
- Ligne export : 106162 · id 242187

#### statut pre-op  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=0
- Logique :
  - **Activating** = `FSM keypad = 1`
- Lit : `FSM keypad`
- Utilisé par : `Keypad HS`
- Ligne export : 106207 · id 242191

## Keypad 8 keys / Keypad CAN

#### heartbeat  `GFIN`
> voir page 24 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x715 · Data length=Dont care · Timeout=2000 · Paged protocol={Not used} · Parameters={{Heartbeat/statut; 0}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=0
- Lit : `Heartbeat/statut`
- Utilisé par : `No heartbeat`
- Ligne export : 104332 · id 241139

#### Heartbeat/statut  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `FSM keypad`, `heartbeat`
- Ligne export : 104351 · id 241140

#### keys number frame  `GFIN`
> voir page 8 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x195 · Data length=Dont care · Paged protocol={Not used} · Parameters={{keys number; 0}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=1
- Lit : `keys number`
- Utilisé par : *(personne)*
- Ligne export : 104363 · id 241210

#### keys number  `GPIN`
> le 1er octet donne le numéro du bouton préssé (bouton 1=1, bouton 8 = 128)
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `Down Keypad`, `Fast keypad`, `Free keypad`, `Normal keypad`, `Slow keypad`, `Start/Stop keypad`, `Up Keypad`, `keys number frame`
- Ligne export : 104382 · id 241211

#### set led ON  `GFOUT`
> voir page 8 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x215 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{Red led part 1; 0}; {Red led part 2; 4}; {Green led part 1; 8}; {Green led part 2; 12}; {Blue led part 2; 20}; {Blue led part 1; 16}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=0
- Lit : `Blue led part 1`, `Blue led part 2`, `Green led part 1`, `Green led part 2`, `Red led part 1`, `Red led part 2`
- Utilisé par : *(personne)*
- Ligne export : 104394 · id 241225

#### Blue led part 2  `GPOUT`
- Propriétés : Input value=Blue led 5, 6, 7 & 8 · Length=4 bits · Type=Unsigned integer
- Lit : `Blue led 5, 6, 7 & 8`
- Utilisé par : `set led ON`
- Ligne export : 104428 · id 241226

#### Green led part 1  `GPOUT`
- Propriétés : Input value=0 · Length=4 bits · Type=Unsigned integer
- Utilisé par : `set led ON`
- Ligne export : 104439 · id 241264

#### Red led part 2  `GPOUT`
- Propriétés : Input value=0 · Length=4 bits · Type=Unsigned integer
- Utilisé par : `set led ON`
- Ligne export : 104450 · id 241266

#### Blue led 1, 2, 3 & 4  `MAC`
> Addition des bit pour savoir quelle led mettre sur ON (voir page 8 de la datasheet "PKP_2400_SI_CANopen_UM")
- Logique :
  ```qcode
  Result := blue led #1 * 1 + blue led#2 * 2 + Blue led #4 * 8
  ```
- Lit : `Blue led #4`, `blue led #1`, `blue led#2`
- Utilisé par : `Blue led part 1`
- Ligne export : 104461 · id 241335

#### Blue led part 1  `GPOUT`
> sur la datasheet du PKP 2400SI (page 8/39) "blue led part 1" correspond au nombre binaire "B4 B3 B2 B1"
- Propriétés : Input value=Blue led 1, 2, 3 & 4 · Length=4 bits · Type=Unsigned integer
- Lit : `Blue led 1, 2, 3 & 4`
- Utilisé par : `set led ON`
- Ligne export : 104479 · id 241349

#### Green led part 2  `GPOUT`
- Propriétés : Input value=0 · Length=4 bits · Type=Unsigned integer
- Utilisé par : `set led ON`
- Ligne export : 104490 · id 241351

#### Red led part 1  `GPOUT`
- Propriétés : Input value=Red led 1, 2, 3 & 4 · Length=4 bits · Type=Unsigned integer
- Lit : `Red led 1, 2, 3 & 4`
- Utilisé par : `set led ON`
- Ligne export : 104501 · id 241353

#### Blue led 5, 6, 7 & 8  `MAC`
> Addition des bit pour savoir quelle led mettre sur ON (voir page 8 de la datasheet "PKP_2400_SI_CANopen_UM")
- Logique :
  ```qcode
  Result := blue led #5 * 1 + blue led #6 * 2 + blue led #7 * 4 + blue led #8 * 8
  ```
- Lit : `blue led #5`, `blue led #6`, `blue led #7`, `blue led #8`
- Utilisé par : `Blue led part 2`
- Ligne export : 104512 · id 241355

#### Red led 1, 2, 3 & 4  `MAC`
> Addition des bit pour savoir quelle led mettre sur ON (voir page 8 de la datasheet "PKP_2400_SI_CANopen_UM")
- Logique :
  ```qcode
  Result := red led#1 * 1
  ```
- Lit : `red led#1`
- Utilisé par : `Red led part 1`
- Ligne export : 104530 · id 241473

#### red led#1  `FGI`
- Propriétés : Input type=Real · Input=red led#1 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `red led#1`
- Utilisé par : `Red led 1, 2, 3 & 4`
- Ligne export : 104548 · id 241814

#### blue led #1  `FGI`
- Propriétés : Input type=Real · Input=blue led #1 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `blue led #1`
- Utilisé par : `Blue led 1, 2, 3 & 4`
- Ligne export : 104562 · id 241815

#### blue led#2  `FGI`
- Propriétés : Input type=Real · Input=blue led #2 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `blue led #2`
- Utilisé par : `Blue led 1, 2, 3 & 4`
- Ligne export : 104576 · id 241816

#### blue led #5  `FGI`
- Propriétés : Input type=Real · Input=blue led #5 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `blue led #5`
- Utilisé par : `Blue led 5, 6, 7 & 8`
- Ligne export : 104590 · id 241817

#### blue led #6  `FGI`
- Propriétés : Input type=Real · Input=blue led #6 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `blue led #6`
- Utilisé par : `Blue led 5, 6, 7 & 8`
- Ligne export : 104604 · id 241818

#### blue led #7  `FGI`
- Propriétés : Input type=Real · Input=blue led #7 · Min limit=Unlimited · Max limit=Unlimited · Default state name=Default state
- Lit : `blue led #7`
- Utilisé par : `Blue led 5, 6, 7 & 8`
- Ligne export : 104618 · id 241819

#### set led blink ON  `GFOUT`
> voir page 9 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x315 · Data length=8 · Send method=On change · Unused bits=Set to 0 · Parameters={{blue led blink part1; 16}; {blue led blink part2; 20}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=1
- Lit : `blue led blink part1`, `blue led blink part2`
- Utilisé par : *(personne)*
- Ligne export : 104632 · id 241895

#### blue led blink part1  `GPOUT`
- Propriétés : Input value=Blue led blink 1, 2, 3 & 4 · Length=4 bits · Type=Unsigned integer
- Lit : `Blue led blink 1, 2, 3 & 4`
- Utilisé par : `set led blink ON`
- Ligne export : 104654 · id 241896

#### blue led blink part2  `GPOUT`
- Propriétés : Input value=Blue led blink 5, 6, 7 & 8 · Length=4 bits · Type=Unsigned integer
- Lit : `Blue led blink 5, 6, 7 & 8`
- Utilisé par : `set led blink ON`
- Ligne export : 104665 · id 241897

#### Blue led blink #4  `FGI`
- Propriétés : Input type=Digital · Input=Blue led blink #4 · Default state name=Default state
- Lit : `Blue led blink #4`
- Utilisé par : `Blue led blink 1, 2, 3 & 4`
- Ligne export : 104676 · id 241899

#### Blue led blink #8  `FGI`
- Propriétés : Input type=Digital · Input=Blue led blink #8 · Default state name=Default state
- Lit : `Blue led blink #8`
- Utilisé par : `Blue led blink 5, 6, 7 & 8`
- Ligne export : 104687 · id 241901

#### Blue led blink 1, 2, 3 & 4  `MAC`
> Addition des bit pour savoir quelle led mettre sur ON (voir page 8 de la datasheet "PKP_2400_SI_CANopen_UM")
- Logique :
  ```qcode
  Result := Blue led blink #4 * 8
  ```
- Lit : `Blue led blink #4`
- Utilisé par : `blue led blink part1`
- Ligne export : 104698 · id 241909

#### Blue led blink 5, 6, 7 & 8  `MAC`
> Addition des bit pour savoir quelle led mettre sur ON (voir page 8 de la datasheet "PKP_2400_SI_CANopen_UM")
- Logique :
  ```qcode
  Result := Blue led blink #8 * 8
  ```
- Lit : `Blue led blink #8`
- Utilisé par : `blue led blink part2`
- Ligne export : 104716 · id 241925

#### Blue led #4  `FGI`
- Propriétés : Input type=Digital · Input=blue led #4 · Default state name=Default state
- Lit : `blue led #4`
- Utilisé par : `Blue led 1, 2, 3 & 4`
- Ligne export : 104734 · id 241936

#### blue led #8  `FGI`
- Propriétés : Input type=Digital · Input=blue led #8 · Default state name=Default state
- Lit : `blue led #8`
- Utilisé par : `Blue led 5, 6, 7 & 8`
- Ligne export : 104745 · id 241937

#### Backlight default color  `GFOUT`
> voir page 15 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x615 · Data length=5 · Send method=On change · Unused bits=Set to 0 · Parameters={{Set device register; 0}; {CAN object 2003h byte 1; 8}; {CAN object 2003h byte 2; 16}; {Sub index 04; 24}; {Color; 32}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=2
- Lit : `CAN object 2003h byte 1`, `CAN object 2003h byte 2`, `Color`, `Set device register`, `Sub index 04`
- Utilisé par : *(personne)*
- Ligne export : 104756 · id 241953

#### Set device register  `GPOUT`
- Propriétés : Input value=0x2F · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `Backlight default color`, `Brightness default level`
- Ligne export : 104787 · id 241954

#### CAN object 2003h byte 1  `GPOUT`
- Propriétés : Input value=0x03 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `Backlight default color`, `Brightness default level`
- Ligne export : 104798 · id 241955

#### Sub index 04  `GPOUT`
- Propriétés : Input value=0x04 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `Backlight default color`
- Ligne export : 104809 · id 241957

#### Color  `GPOUT`
- Propriétés : Input value=Color en hex · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `Color en hex`
- Utilisé par : `Backlight default color`
- Ligne export : 104820 · id 241958

#### CAN object 2003h byte 2  `GPOUT`
- Propriétés : Input value=0x20 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `Backlight default color`, `Brightness default level`
- Ligne export : 104831 · id 241961

#### Keypad backlight color  `SP`
- Propriétés : Input channel=None · Default state name=white · States={yellow; Cyan; violet; amber; yellow/green}
- Utilisé par : `Color en hex`, `Adjust group: Setup`, `Single adjust item: Keypad backlight color`
- Ligne export : 104842 · id 241962

#### Color en hex  `MAC`
> code couleur en hex 
- Logique :
  ```qcode
  if Keypad backlight color = 0 then
  Result := 0x07
  endif
  if Keypad backlight color = 1 then
  Result := 0x04
  endif
  if Keypad backlight color = 2 then
  Result := 0x05
  endif
  if Keypad backlight color = 3 then
  Result := 0x06
  endif
  if Keypad backlight color = 4 then
  Result := 0x08
  endif
  if Keypad backlight color = 5 then
  Result := 0x09
  endif
  ```
- Lit : `Keypad backlight color`
- Utilisé par : `Color`
- Ligne export : 104858 · id 241978

#### backlight 20% activation  `GFOUT`
> voir page 10 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x515 · Data length=1 · Send method=On trigger · Trigger=trigger · Unused bits=Set to 0 · Parameters={{backlight level 20%; 0}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=3
- Lit : `backlight level 20%`, `trigger`
- Utilisé par : *(personne)*
- Ligne export : 104893 · id 242007

#### backlight level 20%  `GPOUT`
- Propriétés : Input value=backlight · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `backlight`
- Utilisé par : `backlight 20% activation`
- Ligne export : 104913 · id 242020

#### Keypad backlight?  `DP`
- Propriétés : True text=backlight · False text=No backlight · Default mode={False}
- Utilisé par : `backlight`, `trigger backlight`, `Adjust group: Setup`, `Single adjust item: Keypad backlight?`
- Ligne export : 104924 · id 242026

#### backlight  `MAC`
> No backlight = 0x00; with backlight = 0x0D
- Logique :
  ```qcode
  if Keypad backlight? = 0 then
  Result := 0x00
  endif
  if Keypad backlight? = 1 then
  Result := 0x0D
  endif
  ```
- Lit : `Keypad backlight?`
- Utilisé par : `backlight level 20%`
- Ligne export : 104937 · id 242028

#### trigger backlight  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(PositiveFlank(Keypad backlight?)) OR (NegativeFlank(Keypad backlight?))`
- Lit : `Keypad backlight?`
- Utilisé par : `trigger`
- Ligne export : 104960 · id 242061

#### trigger  `IDC`
> s'active si activation du MC42 ou si changement de backlight
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Activation OR (trigger backlight)`
- Lit : `Activation`, `trigger backlight`
- Utilisé par : `backlight 20% activation`
- Ligne export : 105012 · id 242068

#### Keypad LED brightness level  `SP`
- Propriétés : Input channel=None · Default state name=100% · States={90%; 80%; 70%; 60%; 50%; 40%; 30%}
- Utilisé par : `level brightness in hex`, `Adjust group: Setup`, `Single adjust item: Keypad LED brightness level`
- Ligne export : 105062 · id 242127

#### level brightness in hex  `MAC`
- Logique :
  ```qcode
  if Keypad LED brightness level = 0 then
  Result := 0x3F
  endif
  if Keypad LED brightness level = 1 then
  Result := 0x39
  endif
  if Keypad LED brightness level = 2 then
  Result := 0x32
  endif
  if Keypad LED brightness level = 3 then
  Result := 0x2C
  endif
  if Keypad LED brightness level = 4 then
  Result := 0x26
  endif
  if Keypad LED brightness level = 5 then
  Result := 0x20
  endif
  if Keypad LED brightness level = 6 then
  Result := 0x19
  endif
  if Keypad LED brightness level = 7 then
  Result := 0x13
  endif
  ```
- Lit : `Keypad LED brightness level`
- Utilisé par : `Brightness level`
- Ligne export : 105080 · id 242135

#### Brightness default level  `GFOUT`
> voir page 16 datasheet "PKP_2400_SI_CANopen_UM"
- Propriétés : Identifier=0x615 · Data length=5 · Send method=On change · Unused bits=Set to 0 · Parameters={{Set device register; 0}; {CAN object 2003h byte 1; 8}; {CAN object 2003h byte 2; 16}; {Sub index 05; 24}; {Brightness level; 32}} · Module=Keypad Blink marine 8 keys (Generic) · Module index=4
- Lit : `Brightness level`, `CAN object 2003h byte 1`, `CAN object 2003h byte 2`, `Set device register`, `Sub index 05`
- Utilisé par : *(personne)*
- Ligne export : 105121 · id 242171

#### Sub index 05  `GPOUT`
- Propriétés : Input value=0x05 · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Utilisé par : `Brightness default level`
- Ligne export : 105152 · id 242179

#### Brightness level  `GPOUT`
- Propriétés : Input value=level brightness in hex · Length=1 Byte (= 8 bits) · Type=Unsigned integer
- Lit : `level brightness in hex`
- Utilisé par : `Brightness default level`
- Ligne export : 105163 · id 242181
