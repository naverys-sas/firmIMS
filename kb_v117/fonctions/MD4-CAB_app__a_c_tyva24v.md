# MD4-CAB app — a/c tyva24v

120 canaux. Généré depuis l'export texte v117 ; ne pas éditer à la main.

## a/c tyva24v — actif seulement si `a/c option tyva`

#### BatteryState_M0  `GFIN`
- Propriétés : Identifier=0x18FF0980 · Data length=Dont care · Paged protocol={Not used} · Parameters={{SOC tyva [%]; 0}; {SOH [%]; 16}; {CycleCount; 32}} · Module=tyva 24v a/c (Generic) · Module index=1
- Lit : `CycleCount`, `SOC tyva`, `SOH`
- Utilisé par : *(personne)*
- Ligne export : 111173 · id 234854

#### SOC tyva  `GPIN`
- Propriétés : Unit=% · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `BatteryState_M0`, `SOC Tyva1`
- Ligne export : 111198 · id 234855

#### SOH  `GPIN`
- Propriétés : Unit=% · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `BatteryState_M0`, `SOH1`, `Measure group: Battery Tyva`
- Ligne export : 111211 · id 234856

#### PDUStatus_M0b  `GFIN`
- Propriétés : Identifier=0x18FF1380 · Data length=Dont care · Paged protocol={Not used} · Parameters={{PDURelayStatusCharge; 2}; {PDURelayStatusDecharge; 1}; {PDURelayStatusPrecharge; 0}} · Module=tyva 24v a/c (Generic) · Module index=2
- Lit : `PDURelayStatusCharge`, `PDURelayStatusDecharge`, `PDURelayStatusPrecharge`
- Utilisé par : *(personne)*
- Ligne export : 111224 · id 234857

#### PDURelayStatusCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 111249 · id 234858

#### PDURelayStatusDecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 111260 · id 234859

#### PDURelayStatusPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `PDUStatus_M0b`
- Ligne export : 111271 · id 234860

#### SynthesisBMS_M0  `GFIN`
- Propriétés : Identifier=0x18FF1280 · Data length=Dont care · Timeout=10000 · Paged protocol={Not used} · Parameters={{isBalancing; 0}; {isChargePossible; 2}; {isChargeRelayClosingAuth; 4}; {isDischargePossible; 3}; {isDischargeRelayClosingAuth; 5}; {isReadyToStart; 1}; {StateBMS; 6}} · Module=tyva 24v a/c (Generic) · Module index=3
- Lit : `StateBMS`, `isBalancing`, `isChargePossible`, `isChargeRelayClosingAuth`, `isDischargePossible`, `isDischargeRelayClosingAuth`, `isReadyToStart`
- Utilisé par : `tyva1 batt can nok`, `tyva1 batt can ok idc`
- Ligne export : 111282 · id 234861

#### isBalancing  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 111319 · id 234862

#### isChargePossible  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 111330 · id 234863

#### isChargeRelayClosingAuth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 111341 · id 234864

#### isDischargePossible  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`, `Tyva1 - isDischargePossible`
- Ligne export : 111352 · id 234865

#### isDischargeRelayClosingAuth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 111363 · id 234866

#### isReadyToStart  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `SynthesisBMS_M0`
- Ligne export : 111374 · id 234867

#### StateBMS  `GPIN`
- Propriétés : Length=8 · Type=Unsigned integer · Error value=0
- Utilisé par : `SynthesisBMS_M0`, `bms decode bin1`
- Ligne export : 111385 · id 234868

#### Error_M0  `GFIN`
- Propriétés : Identifier=0x18FF1180 · Data length=Dont care · Timeout=10000 · Paged protocol={Not used} · Parameters={{ErrorAFEIssues; 23}; {ErrorBluetooth; 13}; {ErrorBmsOverTemperature; 18}; {ErrorCellIssues; 20}; {ErrorChargerIssue; 19}; {ErrorCurrentCalibration; 9}; {ErrorDataLogger; 14}; {ErrorHighVoltage; 11}; {ErrorLowVoltage; 10}; {ErrorNTC; 12}; {ErrorOverCurrent; 30}; {ErrorOverTemperatureCharge; 25}; {ErrorOverTemperatureDischarge; 27}; {ErrorOverVoltage; 29}; {ErrorPDULock; 31}; {ErrorPduFailure; 16}; {ErrorPduOverTemperature; 17}; {ErrorShortCircuit; 21}; {ErrorShortCircuitOnPrecharge; 8}; {ErrorSlaveSilent; 22}; {ErrorUnderTemperatureCharge; 24}; {ErrorUnderTemperatureDischarge; 26}; {ErrorUnderVoltage; 28}} · Module=tyva 24v a/c (Generic) · Module index=8
- Lit : `12`, `13`, `ErrorAFEIssues`, `ErrorBluetooth`, `ErrorBmsOverTemperature`, `ErrorCellIssues`, `ErrorChargerIssue`, `ErrorCurrentCalibration`, `ErrorDataLogger`, `ErrorHighVoltage`, `ErrorLowVoltage`, `ErrorNTC`, `ErrorOverCurrent`, `ErrorOverTemperatureCharge`, `ErrorOverTemperatureDischarge`, `ErrorOverVoltage`, `ErrorPDULock`, `ErrorPduFailure`, `ErrorPduOverTemperature`, `ErrorShortCircuit`, `ErrorShortCircuitOnPrecharge`, `ErrorSlaveSilent`, `ErrorUnderTemperatureCharge`, `ErrorUnderTemperatureDischarge`, `ErrorUnderVoltage`
- Utilisé par : *(personne)*
- Ligne export : 111397 · id 234869

#### ErrorAFEIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111482 · id 234870

#### ErrorBluetooth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111493 · id 234871

#### ErrorBmsOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111504 · id 234872

#### ErrorCellIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111515 · id 234873

#### ErrorChargerIssue  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111526 · id 234874

#### ErrorCurrentCalibration  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111537 · id 234875

#### ErrorDataLogger  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`
- Ligne export : 111548 · id 234876

#### ErrorHighVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111559 · id 234877

#### ErrorLowVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111570 · id 234878

#### ErrorNTC  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111581 · id 234879

#### ErrorOverCurrent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111592 · id 234880

#### ErrorOverTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111603 · id 234881

#### ErrorOverTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111614 · id 234882

#### ErrorOverVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111625 · id 234883

#### ErrorPDULock  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111636 · id 234884

#### ErrorPduFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111647 · id 234885

#### ErrorPduOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111658 · id 234886

#### ErrorShortCircuit  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111669 · id 234887

#### ErrorShortCircuitOnPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111680 · id 234888

#### ErrorSlaveSilent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111691 · id 234889

#### ErrorUnderTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111702 · id 234890

#### ErrorUnderTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111713 · id 234891

#### ErrorUnderVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Error_M0`, `tyva1 - ERROR DIGIT`, `Event log: New event log`, `Event log: Tyva Battery`
- Ligne export : 111724 · id 234892

#### TemperaturePDU_M0  `GFIN`
- Propriétés : Identifier=0x18FF0F80 · Data length=Dont care · Paged protocol={Not used} · Parameters={{TemperaturePDU [°C]; 0}} · Module=tyva 24v a/c (Generic) · Module index=4
- Lit : `TemperaturePDU`
- Utilisé par : *(personne)*
- Ligne export : 111735 · id 234893

#### TemperaturePDU  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperaturePDU1`, `TemperaturePDU_M0`
- Ligne export : 111754 · id 234894

#### VoltageBattery_M0  `GFIN`
- Propriétés : Identifier=0x18FF0080 · Data length=Dont care · Paged protocol={Not used} · Parameters={{VoltageCellMax [mV]; 16}; {VoltageCellMin [mV]; 0}; {BatteryVoltage tyva [V]; 32}} · Module=tyva 24v a/c (Generic) · Module index=5
- Lit : `BatteryVoltage tyva`, `VoltageCellMax`, `VoltageCellMin`
- Utilisé par : *(personne)*
- Ligne export : 111767 · id 234895

#### VoltageCellMax  `GPIN`
- Propriétés : Unit=mV · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `VoltageBattery_M0`, `VoltageCellMax Tyva1 V`
- Ligne export : 111792 · id 234896

#### VoltageCellMin  `GPIN`
- Propriétés : Unit=mV · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `VoltageBattery_M0`, `VoltageCellMin Tyva1 V`
- Ligne export : 111805 · id 234897

#### CurrentBattery_M0  `GFIN`
- Propriétés : Identifier=0x18FF0880 · Data length=Dont care · Paged protocol={Not used} · Parameters={{WRONG BatteryCurrent [A]; 7}} · Module=tyva 24v a/c (Generic) · Module index=6
- Lit : `WRONG BatteryCurrent`
- Utilisé par : *(personne)*
- Ligne export : 111818 · id 234898

#### WRONG BatteryCurrent  `GPIN`
- Propriétés : Unit=A · Length=4 Bytes (= 32 bits) · Type=Signed integer · Byte order=Big-endian · Error value=0
- Utilisé par : `CurrentBattery_M0`
- Ligne export : 111837 · id 234899

#### TemperatureCell_M0  `GFIN`
- Propriétés : Identifier=0x18FF0B80 · Data length=Dont care · Paged protocol={Not used} · Parameters={{TemperatureCellMax [°C]; 16}; {TemperatureCellMin [°C]; 0}; {TemperatureCellMean [°C]; 32}} · Module=tyva 24v a/c (Generic) · Module index=0
- Lit : `TemperatureCellMax`, `TemperatureCellMean`, `TemperatureCellMin`
- Utilisé par : *(personne)*
- Ligne export : 111850 · id 234900

#### TemperatureCellMax  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperatureCellMax calc1`, `TemperatureCell_M0`
- Ligne export : 111875 · id 234901

#### TemperatureCellMin  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperatureCellMin calc1`, `TemperatureCell_M0`
- Ligne export : 111888 · id 234902

#### MaxAdmissibleCurrent_M0  `GFIN`
- Propriétés : Identifier=0x18FF1580 · Data length=Dont care · Paged protocol={Not used} · Parameters={{IMD [A]; 0}; {IMR [A]; 32}} · Module=tyva 24v a/c (Generic) · Module index=7
- Lit : `IMD`, `IMR`
- Utilisé par : *(personne)*
- Ligne export : 111901 · id 234903

#### IMD  `GPIN`
- Propriétés : Unit=A · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `IMD Tyva1 Max curr`, `MaxAdmissibleCurrent_M0`
- Ligne export : 111923 · id 234904

#### Warning_M0  `GFIN`
- Propriétés : Identifier=0x18FF1480 · Data length=Dont care · Timeout=10000 · Paged protocol={Not used} · Parameters={{WarningAFEIssues; 23}; {WarningBluetooth; 13}; {WarningBmsOverTemperature; 18}; {WarningCellIssues; 20}; {WarningChargerIssue; 19}; {WarningCurrentCalibration; 9}; {WarningDataLogger; 14}; {WarningHighVoltage; 11}; {WarningLowVoltage; 10}; {WarningNTC; 12}; {WarningOverCurrent; 30}; {WarningOverTemperatureCharge; 25}; {WarningOverTemperatureDischarge; 27}; {WarningOverVoltage; 29}; {WarningPDULock; 31}; {WarningPduFailure; 16}; {WarningPduOverTemperature; 17}; {WarningShortCircuit; 21}; {WarningShortCircuitOnPrecharge; 8}; {WarningSlaveSilent; 22}; {WarningUnderTemperatureCharge; 24}; {WarningUnderTemperatureDischarge; 26}; {WarningUnderVoltage; 28}} · Module=tyva 24v a/c (Generic) · Module index=9
- Lit : `12`, `13`, `WarningAFEIssues`, `WarningBluetooth`, `WarningBmsOverTemperature`, `WarningCellIssues`, `WarningChargerIssue`, `WarningCurrentCalibration`, `WarningDataLogger`, `WarningHighVoltage`, `WarningLowVoltage`, `WarningNTC`, `WarningOverCurrent`, `WarningOverTemperatureCharge`, `WarningOverTemperatureDischarge`, `WarningOverVoltage`, `WarningPDULock`, `WarningPduFailure`, `WarningPduOverTemperature`, `WarningShortCircuit`, `WarningShortCircuitOnPrecharge`, `WarningSlaveSilent`, `WarningUnderTemperatureCharge`, `WarningUnderTemperatureDischarge`, `WarningUnderVoltage`
- Utilisé par : *(personne)*
- Ligne export : 111936 · id 234905

#### WarningAFEIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112021 · id 234906

#### WarningBluetooth  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112032 · id 234907

#### WarningBmsOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112043 · id 234908

#### WarningCellIssues  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112054 · id 234909

#### WarningChargerIssue  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112065 · id 234910

#### WarningCurrentCalibration  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112076 · id 234911

#### WarningDataLogger  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`
- Ligne export : 112087 · id 234912

#### WarningHighVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112098 · id 234913

#### WarningLowVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112109 · id 234914

#### WarningNTC  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112120 · id 234915

#### WarningOverCurrent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112131 · id 234916

#### WarningOverTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112142 · id 234917

#### WarningOverTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112153 · id 234918

#### WarningOverVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 112164 · id 234919

#### WarningPDULock  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112175 · id 234920

#### WarningPduFailure  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112186 · id 234921

#### WarningPduOverTemperature  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112197 · id 234922

#### WarningShortCircuit  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112208 · id 234923

#### WarningShortCircuitOnPrecharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112219 · id 234924

#### WarningSlaveSilent  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`
- Ligne export : 112230 · id 234925

#### WarningUnderTemperatureCharge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112241 · id 234926

#### WarningUnderTemperatureDischarge  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Tyva Battery`
- Ligne export : 112252 · id 234927

#### WarningUnderVoltage  `GPIN`
- Propriétés : Length=1 · Type=Digital
- Utilisé par : `Warning_M0`, `Event log: Novum battery`, `Event log: Tyva Battery`
- Ligne export : 112263 · id 234928

#### TemperaturePDU1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperaturePDU [°C] * 0,01`
- Lit : `TemperaturePDU`
- Utilisé par : *(personne)*
- Ligne export : 112274 · id 234929

#### VoltageCellMax Tyva1 V  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `VoltageCellMax [mV] * 0,001`
- Lit : `VoltageCellMax`
- Utilisé par : *(personne)*
- Ligne export : 112318 · id 234937

#### VoltageCellMin Tyva1 V  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `VoltageCellMin [mV] * 0,001`
- Lit : `VoltageCellMin`
- Utilisé par : *(personne)*
- Ligne export : 112362 · id 234945

#### TemperatureCellMax calc1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMax [°C] * 0,01`
- Lit : `TemperatureCellMax`
- Utilisé par : `Tyva1 - MaxTemp`
- Ligne export : 112406 · id 234953

#### TemperatureCellMin calc1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMin [°C] * 0,01`
- Lit : `TemperatureCellMin`
- Utilisé par : *(personne)*
- Ligne export : 112450 · id 234961

#### IMD Tyva1 Max curr  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `IMD [A] * 0,001`
- Lit : `IMD`
- Utilisé par : *(personne)*
- Ligne export : 112494 · id 234969

#### SOC Tyva1  `MAC`
- Propriétés : Unit=% · Limiting object group=Signed
- Logique :
  - **Controlling** = `SOC tyva [%] * 0,01`
- Lit : `SOC tyva`
- Utilisé par : `Last Soc value Tyva1`, `Soc Tyva1 onoff CHECK`
- Ligne export : 112538 · id 234977

#### SOH1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `SOH [%] * 0,01`
- Lit : `SOH`
- Utilisé par : *(personne)*
- Ligne export : 112582 · id 234985

#### BatteryVoltage tyva  `GPIN`
- Propriétés : Unit=V · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `BatteryVoltage Tyva1`, `VoltageBattery_M0`
- Ligne export : 112626 · id 234993

#### BatteryVoltage Tyva1  `MAC`
- Propriétés : Unit=V · Limiting object group=Signed
- Logique :
  - **Controlling** = `BatteryVoltage tyva [V] * 0,001`
- Lit : `BatteryVoltage tyva`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 112639 · id 234994

#### TemperatureCellMean  `GPIN`
- Propriétés : Unit=°C · Length=16 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `TemperatureCellMean calc1`, `TemperatureCell_M0`
- Ligne export : 112683 · id 235002

#### TemperatureCellMean calc1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMean [°C] * 0,01`
- Lit : `TemperatureCellMean`
- Utilisé par : *(personne)*
- Ligne export : 112696 · id 235003

#### IMR  `GPIN`
- Propriétés : Unit=A · Length=32 · Type=Unsigned integer · Byte order=Big-endian · Error value=0
- Utilisé par : `IMR1`, `MaxAdmissibleCurrent_M0`
- Ligne export : 112740 · id 235011

#### IMR1  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `IMR [A] * 0,001`
- Lit : `IMR`
- Utilisé par : *(personne)*
- Ligne export : 112753 · id 235012

#### CycleCount  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `BatteryState_M0`
- Ligne export : 112797 · id 235020

#### bms decode bin1  `ARC`
- Propriétés : Array size=9 · Store value=No
- Logique :
  ```qcode
  This[0]:=StateBMS mod 2
  This[1]:=(StateBMS div 2) mod 2
  This[2]:=(StateBMS div 4) mod 2
  This[3]:=(StateBMS div 8) mod 2
  This[4]:=(StateBMS div 16) mod 2
  This[5]:=(StateBMS div 32) mod 2
  This[6]:=(StateBMS div 64) mod 2
  This[7]:=(StateBMS div 128) mod 2
  ```
- Lit : `StateBMS`
- Utilisé par : `Tyva charge b4 1`, `Tyva discharge b3 1`, `Tyva standby b2 1`, `fw update b7 1`, `idle b1 1`, `off b0 1`
- Ligne export : 112809 · id 235021

#### off b0 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin1[0]
  ```
- Lit : `bms decode bin1`
- Utilisé par : *(personne)*
- Ligne export : 112836 · id 235051

#### idle b1 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin1[1]
  ```
- Lit : `bms decode bin1`
- Utilisé par : *(personne)*
- Ligne export : 112856 · id 235059

#### Tyva standby b2 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin1[2]
  ```
- Lit : `bms decode bin1`
- Utilisé par : *(personne)*
- Ligne export : 112876 · id 235067

#### Tyva discharge b3 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=3000
- Logique :
  ```qcode
  Result:=bms decode bin1[3]
  ```
- Lit : `bms decode bin1`
- Utilisé par : `auto off tyva 24v not charge`
- Ligne export : 112896 · id 235075

#### Tyva charge b4 1  `IDC`
- Propriétés : Toggle=No · Delay on=2000 · Delay off=3000
- Logique :
  ```qcode
  Result:=bms decode bin1[4]
  ```
- Lit : `bms decode bin1`
- Utilisé par : `Low A/C battery`, `auto off tyva 24v not charge`, `MD4-10 page: FEATURE`
- Ligne export : 112916 · id 235083

#### fw update b7 1  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  ```qcode
  Result:=bms decode bin1[8]
  ```
- Lit : `bms decode bin1`
- Utilisé par : *(personne)*
- Ligne export : 112936 · id 235091

#### Tyva1 - MaxTemp  `MAC`
- Propriétés : Unit=°C · Limiting object group=Signed
- Logique :
  - **Controlling** = `TemperatureCellMax calc1`
- Lit : `TemperatureCellMax calc1`
- Utilisé par : *(personne)*
- Ligne export : 112956 · id 235099

#### Tyva1 - isDischargePossible  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `isDischargePossible`
- Lit : `isDischargePossible`
- Utilisé par : *(personne)*
- Ligne export : 112998 · id 235107

#### tyva1 batt can nok  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(SynthesisBMS_M0 Status = Not evaluated) OR (SynthesisBMS_M0 Status = Timeout)`
- Lit : `SynthesisBMS_M0`
- Utilisé par : *(personne)*
- Ligne export : 113040 · id 235115

#### tyva1 - ERROR DIGIT  `IDC`
- Propriétés : Toggle=No · Delay on=100 · Delay off=100
- Logique :
  - **Activating** = `ErrorOverCurrent OR ErrorOverTemperatureCharge OR ErrorOverTemperatureDischarge OR ErrorOverVoltage OR ErrorLowVoltage OR ErrorHighVoltage OR ErrorPduOverTemperature OR ErrorUnderTemperatureCharge OR ErrorUnderTemperatureDischarge OR ErrorUnderVoltage OR ErrorBmsOverTemperature`
- Lit : `ErrorBmsOverTemperature`, `ErrorHighVoltage`, `ErrorLowVoltage`, `ErrorOverCurrent`, `ErrorOverTemperatureCharge`, `ErrorOverTemperatureDischarge`, `ErrorOverVoltage`, `ErrorPduOverTemperature`, `ErrorUnderTemperatureCharge`, `ErrorUnderTemperatureDischarge`, `ErrorUnderVoltage`
- Utilisé par : *(personne)*
- Ligne export : 113094 · id 235171

#### tyva1 batt can ok idc  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=3000
- Logique :
  - **Activating** = `SynthesisBMS_M0 Status = OK`
- Lit : `SynthesisBMS_M0`
- Utilisé par : `SocTriggerRecord tyva1`, `Tyva1 batt can ok`, `tyva1 batt can nok D`, `MD4-10 page: FEATURE`
- Ligne export : 113207 · id 235190

#### Tyva1 batt can ok  `MAC`
- Propriétés : Limiting object group=Signed
- Logique :
  - **Controlling** = `tyva1 batt can ok idc`
- Lit : `tyva1 batt can ok idc`
- Utilisé par : `tyva1 off on state`
- Ligne export : 113252 · id 235198

#### SocTriggerRecord tyva1  `IDC`
- Propriétés : Toggle=No · Delay on=3000 · Delay off=0
- Logique :
  - **Activating** = `tyva1 batt can ok idc`
- Lit : `tyva1 batt can ok idc`
- Utilisé par : `Last Soc value Tyva1`
- Ligne export : 113294 · id 235214

#### Last Soc value Tyva1  `MEM`
- Propriétés : Input channel=SOC Tyva1 [%] · Action=Replace · Store value=Yes · Reset value=50
- Logique :
  - **Activating** = `SocTriggerRecord tyva1`
- Lit : `SOC Tyva1`, `SocTriggerRecord tyva1`
- Utilisé par : `Soc Tyva1 onoff CHECK`, `prevent discharge if soc below 15%`, `MD4-10 page: FEATURE`
- Ligne export : 113337 · id 235206

#### tyva1 off on state  `SP`
- Propriétés : Input channel=Tyva1 batt can ok · Default state name=off · States={on}
- Lit : `Tyva1 batt can ok`
- Utilisé par : `Soc Tyva1 onoff CHECK`
- Ligne export : 113381 · id 235222

#### Soc Tyva1 onoff CHECK  `MAC`
- Propriétés : Limiting object group=Signed · Function selector=tyva1 off on state
- Fonction *off* :
  - **Controlling** = `Last Soc value Tyva1 [%]`
- Fonction *on* :
  - **Controlling** = `SOC Tyva1 [%]`
- Lit : `Last Soc value Tyva1`, `SOC Tyva1`, `tyva1 off on state`
- Utilisé par : *(personne)*
- Ligne export : 113393 · id 235224

#### prevent discharge if soc below 15%  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `Last Soc value Tyva1 [%] < 15`
- Lit : `Last Soc value Tyva1`
- Utilisé par : `Low A/C battery`, `auto off tyva 24v not charge`
- Ligne export : 113466 · id 235405

#### auto off tyva 24v not charge  `TMR`
- Propriétés : Type (Unit)=Minutes [min] · Store value=No · Reset value=10
- Logique :
  - **Decreasing** = `Tyva discharge b3 1`
  - **Resetting** = `(Tyva charge b4 1) AND (not(prevent discharge if soc below 15%))`
- Lit : `Tyva charge b4 1`, `Tyva discharge b3 1`, `prevent discharge if soc below 15%`
- Utilisé par : `auto off tyva 24v`
- Ligne export : 113511 · id 235387

#### auto off tyva 24v  `IDC`
- Propriétés : Toggle=No · Delay on=10000 · Delay off=0
- Logique :
  - **Activating** = `auto off tyva 24v not charge [min] = 0`
- Lit : `auto off tyva 24v not charge`
- Utilisé par : `auto off tyva 24v APPOUT`
- Ligne export : 113578 · id 235394

#### auto off tyva 24v APPOUT  `APPOUT`
- Propriétés : Input channel=auto off tyva 24v · Send method=On change · Transmit rate=1000
- Lit : `auto off tyva 24v`
- Utilisé par : `auto off tyva 24v APPIN`
- Ligne export : 113623 · id 235401

#### Low A/C battery  `CMSG`
- Propriétés : Show message=All · Dialog type=Message · Header=Low A/C battery · Text=Please charge your A/C battery. The charge will start automatically if you plug the charger in the 1st 10min after you start the screen.
- Logique :
  - **Showing** = `prevent discharge if soc below 15%`
  - **Hiding** = `Tyva charge b4 1`
- Lit : `Tyva charge b4 1`, `prevent discharge if soc below 15%`
- Utilisé par : *(personne)*
- Ligne export : 113634 · id 235412

#### tyva1 batt can nok D  `IDC`
- Propriétés : Toggle=No · Delay on=0 · Delay off=0
- Logique :
  - **Activating** = `(not(tyva1 batt can ok idc)) AND (a/c option tyva)`
- Lit : `a/c option tyva`, `tyva1 batt can ok idc`
- Utilisé par : `MD4-10 page: FEATURE`
- Ligne export : 113687 · id 235425

#### ConfigurationInformation_M0  `GFIN`
- Propriétés : Identifier=0x18FF1680 · Data length=Dont care · Paged protocol={Not used} · Parameters={{ConfigurationFileVersion; 7}} · Module=tyva 24v a/c (Generic) · Module index=10
- Lit : `ConfigurationFileVersion`
- Utilisé par : *(personne)*
- Ligne export : 113738 · id 235539

#### ConfigurationFileVersion  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `ConfigurationInformation_M0`
- Ligne export : 113757 · id 235540

#### FirmwareInformation_M0  `GFIN`
- Propriétés : Identifier=0x18FF1080 · Data length=Dont care · Paged protocol={Not used} · Parameters={{FirmwareMajor; 7}; {FirmwareMinor; 15}; {FirmwareRevision; 23}; {FirmwareBuildMode; 31}} · Module=tyva 24v a/c (Generic) · Module index=11
- Lit : `FirmwareBuildMode`, `FirmwareMajor`, `FirmwareMinor`, `FirmwareRevision`
- Utilisé par : *(personne)*
- Ligne export : 113769 · id 235546

#### FirmwareMajor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `FirmwareInformation_M0`
- Ligne export : 113797 · id 235547

#### FirmwareMinor  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `FirmwareInformation_M0`
- Ligne export : 113809 · id 235550

#### FirmwareRevision  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `FirmwareInformation_M0`
- Ligne export : 113821 · id 235552

#### FirmwareBuildMode  `GPIN`
- Propriétés : Length=1 Byte (= 8 bits) · Type=Unsigned integer · Error value=0
- Utilisé par : `FirmwareInformation_M0`
- Ligne export : 113833 · id 235554
