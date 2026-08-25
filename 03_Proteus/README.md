# Proteus 8.17 Guide

Proteus can be used for schematic presentation and basic circuit visualization. For transistor-level SRAM characterization, LTspice/SPICE is the primary simulation environment in this project because SNM and device-level sweeps are more naturally handled there.

## 6T cell wiring reference

### Left inverter/storage node Q
- M1 PMOS source -> VDD
- M1 PMOS gate -> QB
- M1 PMOS drain -> Q
- M3 NMOS drain -> Q
- M3 NMOS gate -> QB
- M3 NMOS source -> GND

### Right inverter/storage node QB
- M2 PMOS source -> VDD
- M2 PMOS gate -> Q
- M2 PMOS drain -> QB
- M4 NMOS drain -> QB
- M4 NMOS gate -> Q
- M4 NMOS source -> GND

### Access devices
- M5 NMOS: one terminal -> Q, other terminal -> BL, gate -> WL
- M6 NMOS: one terminal -> QB, other terminal -> BLB, gate -> WL

**Important:** The gates of M5 and M6 are connected to **WL**, not to ground. Their source/drain terminals connect between the internal storage nodes and the bit lines.

## Supply polarity
VDD is the positive supply. GND/VSS is the 0 V reference. Never connect VDD directly to GND.
