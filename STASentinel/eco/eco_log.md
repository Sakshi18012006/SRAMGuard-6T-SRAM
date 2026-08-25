# ECO Iteration Log

| Iteration | Diagnosis | Action | Setup WNS | Hold WNS | Result |
|---|---|---|---:|---:|---|
| Baseline | Critical combinational path too slow for 1.0 ns clock | None | -0.080 ns | +0.060 ns | Setup violation |
| ECO-1 | Cell delay dominates critical path | Resize NAND2/INV/NOR2 cells X1 → X2 | +0.230 ns | +0.060 ns | Setup closed |
| ECO-2 | Output loading/transition margin | Add X2 output buffers | +0.230 ns | +0.060 ns | Signoff-style package |

The values above are deterministic educational reference values and are not claimed as foundry signoff measurements.
