"""SRAMGuard SNM-data helper.

Input CSV format:
voltage,vinv1,vinv2
0.0,0.0,1.0
...

The script plots a butterfly curve. Exact SNM extraction should be validated
against the simulator data and the chosen extraction method before reporting.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parent.parent / "05_Results" / "snm_curve.csv"

if not DATA.exists():
    print(f"Create {DATA} using actual simulator output first.")
    raise SystemExit(0)

df = pd.read_csv(DATA)
required = {"voltage", "vinv1", "vinv2"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

plt.figure()
plt.plot(df["voltage"], df["vinv1"], label="Inverter 1")
plt.plot(df["voltage"], df["vinv2"], label="Inverter 2")
plt.xlabel("Input voltage (V)")
plt.ylabel("Output voltage (V)")
plt.title("6T SRAM Butterfly Curve")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "butterfly_curve.png", dpi=200)
plt.show()
