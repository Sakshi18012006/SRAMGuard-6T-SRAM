# Static Noise Margin (SNM)

SNM is a measure of the maximum DC noise voltage that can be tolerated by an SRAM cell without changing its logical state.

## Butterfly Curve Method
For a cross-coupled SRAM cell, plot the voltage transfer characteristic of one inverter against the inverse characteristic of the other inverter. The resulting butterfly curve contains two lobes for the two stable states.

The side length of the largest square that can fit inside the relevant lobe is the SNM.

## Read SNM
Read SNM measures stability while the cell is connected to the bit lines and the word line is active. It is normally lower than hold SNM because the read path can disturb the internal node.

## Hold SNM
Hold SNM measures the cell's stability with WL disabled and the access devices isolated from the bit lines.

## Write Margin
Write margin describes how easily the cell can be forced from one stored state to the opposite state. A stronger access path and suitable pull-up sizing generally improve write ability, while excessive cell strength can make writing difficult.

## PVT and Variation
SNM depends on process corner, supply voltage and temperature. Random transistor mismatch can also produce a distribution of SNM values. Monte Carlo analysis is therefore useful for estimating variation and yield.
