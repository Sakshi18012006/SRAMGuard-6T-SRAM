# Project Overview

## Title
SRAMGuard – 6T SRAM Cell Stability and Variation Analysis

## Problem Statement
A 6T CMOS SRAM cell must retain stored data, allow controlled read/write operations, and remain reliable under voltage, temperature, process and device-mismatch variations. This project studies these properties using transistor-level simulation.

## Objectives
1. Design a conventional 6T SRAM bitcell.
2. Verify hold, read and write operations.
3. Extract hold/read Static Noise Margin (SNM).
4. Evaluate write ability/write margin.
5. Study PVT sensitivity.
6. Perform Monte Carlo mismatch analysis when supported by the selected SPICE model/simulator.
7. Investigate transistor sizing as an optimization variable.

## Cell Components
- M1, M2: PMOS pull-up devices
- M3, M4: NMOS pull-down devices
- M5, M6: NMOS access devices
- Q and QB: complementary internal storage nodes
- BL and BLB: complementary bit lines
- WL: word line
- VDD: positive supply
- VSS/GND: reference node

## Operating Modes
### Hold
WL is low, isolating the internal storage nodes from BL/BLB. The cross-coupled inverter pair maintains the stored state.

### Read
BL and BLB are precharged and WL is asserted. One internal node may discharge through an access and pull-down path. Read stability is characterized using SNM.

### Write
Complementary data is applied to BL/BLB and WL is asserted. The access devices must overpower the cell feedback sufficiently to change the stored state.

## Main Metrics
- Hold SNM
- Read SNM
- Write margin/write ability
- PVT sensitivity
- Monte Carlo distribution/yield

## Scope Limitation
This repository contains the project framework and simulation models/scripts. Numerical results must be generated from the actual simulator and device model used by the student; no fabricated measurements are included.
