# SRAMGuard – 6T SRAM Cell Stability and Variation Analysis

**VLSI Internship Project**

## Project Overview
SRAMGuard is a transistor-level study of a conventional 6-transistor (6T) CMOS SRAM bit cell. The project focuses on cell operation, read/write behavior, Static Noise Margin (SNM), write ability, process-voltage-temperature (PVT) sensitivity, and Monte Carlo variation analysis.

## Objectives
- Build a transistor-level 6T SRAM cell.
- Verify hold, read and write operation.
- Evaluate hold/read Static Noise Margin (SNM).
- Evaluate write ability/write margin.
- Study PVT corners.
- Study device mismatch using Monte Carlo analysis where the simulator/model supports it.
- Compare baseline and optimized transistor sizing.

## Cell Architecture
The cell contains:
- M1, M2: PMOS pull-up transistors
- M3, M4: NMOS pull-down transistors
- M5, M6: NMOS access/pass transistors
- Q and QB: complementary storage nodes
- BL and BLB: complementary bit lines
- WL: word line
- VDD: supply

## Tools
- LTspice for SPICE-level circuit simulation
- Proteus 8.17 for schematic/reference visualization where applicable
- Python 3 for data processing and plotting
- GitHub for version control and project submission

## Repository Structure
```text
01_Theory/
02_LTspice/
03_Proteus/
04_Python_Analysis/
05_Results/
06_Documentation/
07_Viva/
```

## Important note about results
Simulation result files in this repository are templates until they are replaced with measurements from the actual simulator/model used for the project. No fabricated SNM, PVT or Monte Carlo values are presented as experimental results.

## Expected Deliverables
1. 6T SRAM schematic and testbench
2. Read/hold SNM plots
3. Write-margin analysis
4. PVT analysis
5. Monte Carlo/variation analysis
6. Final comparison and report

## Author
**Sakshi Hogade**

## GitHub Repository
https://github.com/Sakshi18012006/SRAMGuard-6T-SRAM
