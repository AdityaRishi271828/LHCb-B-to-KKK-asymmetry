import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])) 

import matplotlib.pyplot as plt
import numpy as np

import config
import tools

tools.require("SIGNAL_WINDOW", "SIDEBANDS", "PID_LOOSE", "PID_TIGHT", "WINDOW_VARIATIONS")

mass, charge, polarity = tools.load_selected()
W, SB = config.SIGNAL_WINDOW, config.SIDEBANDS
nominal = tools.measure(mass, charge, W, SB)
lines = [f"Nominal: A = {nominal['A']:.4f} +/- {nominal['sigma']:.4f}", ""]

# magnet polarity
down = tools.measure(mass[polarity == -1], charge[polarity == -1], W, SB)
up = tools.measure(mass[polarity == +1], charge[polarity == +1], W, SB)
z, p = tools.compare(up["A"], up["sigma"], down["A"], down["sigma"])
lines += ["1. Magnet polarity",
        f" Down: A = {down['A']:.4f} +/- {down['sigma']:.4f}",
        f" Up: A = {up['A']:.4f} +/- {up['sigma']:.4f}",
        f" Difference: z = {z:.2f}, p = {p:.3f}", ""]

# asymmetry of the background candidates alone
in_sb = np.zeros(len(mass), dtype=bool)
for lo, hi in SB:
    in_sb |= (mass >= lo) & (mass < hi)
n_p = int(np.sum(in_sb & (charge == +1)))
n_m = int(np.sum(in_sb & (charge == -1)))
a_sb = (n_m - n_p) / (n_m + n_p)
s_sb = np.sqrt((1 - a_sb**2) / (n_m + n_p)) # no background to subtract here
lines += ["2. Sideband candidates",
        f" N+ = {n_p}, N- = {n_m}, A = {a_sb:.4f} +/- {s_sb:.4f}", ""]

# alternative selections 
lines.append("3. Selection variations")
for name, cuts in (("Loose", config.PID_LOOSE), ("Tight", config.PID_TIGHT)):
    m2, q2, _, _ = tools.select(**cuts)
    r = tools.measure(m2, q2, W, SB)
    lines.append(f" {name} {cuts}: A = {r['A']:.4f} +/- {r['sigma']:.4f}")
lines.append("")

# 4. Signal-window variations
lines.append("4. Window variations")
for w in config.WINDOW_VARIATIONS:
    r = tools.measure(mass, charge, w, SB)
    lines.append(f" Window {w}: A = {r['A']:.4f} +/- {r['sigma']:.4f}")

tools.save_text("05_checks.txt", lines)