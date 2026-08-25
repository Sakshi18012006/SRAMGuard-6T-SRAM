"""Analyze actual Monte Carlo CSV output.

Expected columns:
run,snm

This script does not generate fake samples. Replace the template CSV with
actual simulator results before using the statistics in the report.
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "05_Results" / "Monte_Carlo_Results.csv"

if not DATA.exists():
    print(f"Create {DATA} with actual Monte Carlo results first.")
    raise SystemExit(0)

df = pd.read_csv(DATA)
if not {"run", "snm"}.issubset(df.columns):
    raise ValueError("CSV must contain run and snm columns")

snm = pd.to_numeric(df["snm"], errors="coerce").dropna()
if snm.empty:
    raise ValueError("No numeric SNM values found")

print("Samples:", len(snm))
print("Mean SNM:", snm.mean())
print("Std. deviation:", snm.std(ddof=1) if len(snm) > 1 else 0.0)
print("Minimum SNM:", snm.min())
print("Maximum SNM:", snm.max())
