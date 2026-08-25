# STASentinel – Full Timing Closure on Synthesized Netlist

VLSI internship project demonstrating a signoff-style Static Timing Analysis (STA) and timing-closure flow.

## Flow
RTL → Yosys synthesis → gate-level netlist → Liberty + SDC → OpenSTA → violation discovery → ECO resizing/buffering → re-analysis → signoff dashboard.

## Internship requirements covered
- Constraint modeling: clock, I/O, uncertainty, false-path and multicycle-path examples
- Violation discovery: setup/hold, WNS and TNS
- ECO fixing: cell resizing and output buffering
- Signoff packaging: timing reports, ECO log and dashboard

## Tools
- Yosys for synthesis
- OpenSTA for static timing analysis
- Python for the deterministic reference demonstration

## Important scope note
This is an educational signoff-style flow using a simplified Liberty library and deterministic reference timing data. It is not claimed as production/foundry signoff.

The complete submission ZIP is provided separately with the internship submission package.

## Author
Sakshi Hogade

## Live repository
https://github.com/Sakshi18012006/SRAMGuard-6T-SRAM
