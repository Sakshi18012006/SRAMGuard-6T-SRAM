# LTspice Simulation

This folder contains a simulator-independent SPICE starting point for the 6T SRAM cell.

## Node naming
- `vdd`: positive supply
- `0`: ground/VSS
- `q`, `qb`: internal storage nodes
- `bl`, `blb`: bit lines
- `wl`: word line

## Device mapping
- M1/M2 = PMOS pull-up pair
- M3/M4 = NMOS pull-down pair
- M5/M6 = NMOS access pair

## Recommended simulation sequence
1. DC operating-point/initialization check.
2. Hold operation.
3. Read operation with BL/BLB precharge and WL pulse.
4. Write 0/1 and 1/0 transitions.
5. Generate butterfly-curve data for SNM extraction.
6. Sweep VDD and temperature.
7. Repeat for process corners if the selected model provides corner cards.
8. Run mismatch/Monte Carlo if supported by the model and simulator.

The included netlist uses simple educational MOS models so that the topology can be simulated without a foundry PDK. These are **not** a substitute for a real CMOS technology model.
