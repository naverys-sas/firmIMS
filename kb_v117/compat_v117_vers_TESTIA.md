# Contrôle de compatibilité

- Référence : export de `v117_testia.idax` (108.2.2_117)
- Candidat : export de `TESTIA.idax` (version 108.3.1)

**2 éléments supprimés, 0 modifiés, 35 ajoutés.** Un élément supprimé ou modifié casse potentiellement un bateau déjà livré ; il doit être justifié.

## Supprimés (2)

- Signal CAN · MC42 app · `heartbeat` — était : GPIN longueur=1 Byte (= 8 bits) type=Unsigned integer unité=Not used
- Trame CAN · MC42 app · `heart` — était : GFIN module=Keypad PKP_2400_SI (Generic) id=0x715 dlc=Dont care contenu={{heartbeat; 0}}

## Modifiés (0)


## Ajoutés (35)

- Journal ·  · `Event log: Balancing TYVA` — 
- Message · MC42 app · `Keypad HS` — Keypad is not working | Warning
- Paramètre · MC42 app · `Keypad 8 keys` — DP unité= défaut={False} états= modes=Not used
- Paramètre · MC42 app · `Keypad LED brightness level` — SP unité= défaut=100% états=90%|80%|70%|60%|50%|40%|30% modes=
- Paramètre · MC42 app · `Keypad backlight color` — SP unité= défaut=white états=yellow|Cyan|violet|amber|yellow/green modes=
- Paramètre · MC42 app · `Keypad backlight?` — DP unité= défaut={False} états= modes=Not used
- Réglage ·  · `Keypad 8 keys` — Keypad 8 keys 
- Réglage ·  · `Keypad LED brightness level` — Keypad LED brightness level 
- Réglage ·  · `Keypad backlight color` — Keypad backlight color 
- Réglage ·  · `Keypad backlight?` — Keypad backlight? 
- Signal CAN · MC42 app · `Blue led part 1` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Blue led part 2` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Brightness level` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `CAN object 2003h byte 1` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `CAN object 2003h byte 2` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `Color` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `Green led part 1` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Green led part 2` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Heartbeat/statut` — GPIN longueur=1 Byte (= 8 bits) type=Unsigned integer unité=Not used
- Signal CAN · MC42 app · `Red led part 1` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Red led part 2` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `Set device register` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `Sub index 04` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `Sub index 05` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `backlight level 20%` — GPOUT longueur=1 Byte (= 8 bits) type=Unsigned integer unité=
- Signal CAN · MC42 app · `blue led blink part1` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `blue led blink part2` — GPOUT longueur=4 bits type=Unsigned integer unité=
- Signal CAN · MC42 app · `keys number` — GPIN longueur=1 Byte (= 8 bits) type=Unsigned integer unité=Not used
- Trame CAN · MC42 app · `Backlight default color` — GFOUT module=Keypad Blink marine 8 keys (Generic) id=0x615 dlc=5 contenu={{Set device register; 0}; {CAN object 2003h byte 1; 8}; {CAN object 2003h byte 2; 16}; {Sub index 04; 24}; {Color; 32}}
- Trame CAN · MC42 app · `Brightness default level` — GFOUT module=Keypad Blink marine 8 keys (Generic) id=0x615 dlc=5 contenu={{Set device register; 0}; {CAN object 2003h byte 1; 8}; {CAN object 2003h byte 2; 16}; {Sub index 05; 24}; {Brightness level; 32}}
- Trame CAN · MC42 app · `backlight 20% activation` — GFOUT module=Keypad Blink marine 8 keys (Generic) id=0x515 dlc=1 contenu={{backlight level 20%; 0}}
- Trame CAN · MC42 app · `heartbeat` — GFIN module=Keypad Blink marine 8 keys (Generic) id=0x715 dlc=Dont care contenu={{Heartbeat/statut; 0}}
- Trame CAN · MC42 app · `keys number frame` — GFIN module=Keypad Blink marine 8 keys (Generic) id=0x195 dlc=Dont care contenu={{keys number; 0}}
- Trame CAN · MC42 app · `set led ON` — GFOUT module=Keypad Blink marine 8 keys (Generic) id=0x215 dlc=8 contenu={{Red led part 1; 0}; {Red led part 2; 4}; {Green led part 1; 8}; {Green led part 2; 12}; {Blue led part 2; 20}; {Blue led part 1; 16}}
- Trame CAN · MC42 app · `set led blink ON` — GFOUT module=Keypad Blink marine 8 keys (Generic) id=0x315 dlc=8 contenu={{blue led blink part1; 16}; {blue led blink part2; 20}}
