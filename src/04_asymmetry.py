import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import numpy as np

import config
import tools

tools.require("SIGNAL_WINDOW", "SIDEBANDS", "SIGNIFICANCE_LEVEL")

mass, charge, polarity = tools.load_selected()
r = tools.measure(mass, charge, config.SIGNAL_WINDOW, config.SIDEBANDS)


fig, ax = plt.subplots(figsize=(6, 4))
for q, label in ((+1, r"$B^+$"), (-1, r"$B^-$")):
    ax.hist(mass[charge == q], bins=tools.mass_edges(), histtype="step", label=label)
tools.shade_regions(ax)
ax.set_xlabel(r"$m(K^+K^-K^\pm)$ [MeV/$c^2$]")
ax.set_ylabel(f"Candidates per {config.MASS_BIN} MeV/$c^2$")
ax.legend()
fig.tight_layout()
fig.savefig(config.FIG_DIR / "04_mass_by_charge.pdf")

rejected = r["p"] < config.SIGNIFICANCE_LEVEL
tools.save_text("04_asymmetry.txt", [
    f"N(B+) = {r['N+']:.0f} +/- {r['err N+']:.0f}",
    f"N(B-) = {r['N-']:.0f} +/- {r['err N-']:.0f}",
    f"Raw asymmetry A = {r['A']:.4f} +/- {r['sigma']:.4f}",
    f"Significance z = {r['z']:.2f}, two-sided p = {r['p']:.2e}",
    f"H0 rejected at the {config.SIGNIFICANCE_LEVEL} level: {rejected}",])