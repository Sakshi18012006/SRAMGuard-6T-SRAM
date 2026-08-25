# SRAMGuard Viva Questions and Short Answers

## 1. What is SRAM?
Static Random Access Memory stores data using a bistable circuit and does not require refresh while powered.

## 2. Why is it called 6T SRAM?
A conventional bitcell uses six MOSFETs: two PMOS pull-ups, two NMOS pull-downs and two NMOS access devices.

## 3. What are Q and QB?
Q and QB are complementary internal storage nodes. Ideally, when Q is 1, QB is 0, and vice versa.

## 4. What is WL?
WL is the word line. It controls the two access transistors and connects the cell to BL and BLB when asserted.

## 5. What are BL and BLB?
They are complementary bit lines used to read and write the cell.

## 6. What is SNM?
Static Noise Margin is the maximum DC noise magnitude the cell can tolerate without losing its stored state.

## 7. Why is read SNM important?
A read operation can disturb an internal storage node, so read SNM indicates how stable the cell is during reading.

## 8. What is PVT analysis?
PVT means Process, Voltage and Temperature analysis. It studies circuit behavior under manufacturing, supply and temperature variations.

## 9. What is Monte Carlo analysis?
It repeatedly simulates random parameter variations to obtain a statistical distribution of a circuit metric such as SNM.

## 10. Why optimize transistor sizing?
Sizing changes the relative strengths of pull-up, pull-down and access devices, affecting stability and write ability.

## 11. Where are M5 and M6 gates connected?
Both access-transistor gates are connected to WL, not ground.

## 12. Where is VDD connected?
The PMOS source terminals are connected to the positive VDD supply. The NMOS pull-down sources connect to ground.
