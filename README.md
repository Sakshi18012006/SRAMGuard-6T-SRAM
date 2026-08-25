# SRAMGuard – 6T SRAM Cell Stability and Variation Analysis

**VLSI Internship Projects Repository**

This repository contains the SRAMGuard project material and the STASentinel timing-closure project.

## STASentinel – Full Timing Closure on Synthesized Netlist

STASentinel is an educational signoff-style Static Timing Analysis (STA) and timing-closure flow covering the four internship phases: constraint modeling, violation discovery, ECO-based fixing, and signoff packaging.

### STASentinel flow
RTL → Yosys synthesis → gate-level netlist → Liberty + SDC → OpenSTA → setup/hold analysis → WNS/TNS → ECO resizing/buffering → re-analysis → signoff summary.

### STASentinel deliverables in this repository
- `STASentinel/README.md`
- `STASentinel/rtl/stasentinel_core.v`
- `STASentinel/constraints/timing.sdc`
- `STASentinel/library/stasentinel_cells.lib`
- `STASentinel/synthesis/synth.ys`
- `STASentinel/sta/run_sta.tcl`
- `STASentinel/eco/eco_log.md`
- `STASentinel/reports/timing_summary.csv`
- `STASentinel/reports/signoff_summary.md`

The complete internship submission ZIP contains the full project package, including the remaining netlists, scripts, reports, dashboard and documentation.

**Scope note:** STASentinel uses a simplified educational Liberty library and deterministic reference timing values. It is not claimed as foundry-qualified production signoff.

## SRAMGuard – 6T SRAM Cell Stability and Variation Analysis

SRAMGuard is a transistor-level study of a conventional 6-transistor (6T) CMOS SRAM bit cell, covering cell operation, read/write behavior, Static Noise Margin (SNM), write ability, PVT sensitivity and Monte Carlo variation analysis.

## Author
**Sakshi Hogade**

## GitHub Repository
https://github.com/Sakshi18012006/SRAMGuard-6T-SRAM
