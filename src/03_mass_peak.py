import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import numpy as np

import config
import tools

tools.require("SIGNAL_WINDOW", "SIDEBANDS")

mass, charge, polarity = tools.load_selected()

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(mass, bins=tools.mass_edges(), histtype="step", color="black")
tools.shade_regions(ax)
ax.set_xlabel(r"$m(K^+K^-K^\pm)$ [MeV/$c^2$]")
ax.set_ylabel(f"Candidates per {config.MASS_BIN} MeV/$c^2$")
ax.legend()
fig.tight_layout()
fig.savefig(config.FIG_DIR / "03_mass_regions.pdf")

n_win = tools.count_in(mass, config.SIGNAL_WINDOW)
n_sig, err = tools.sideband_subtract(mass, config.SIGNAL_WINDOW, config.SIDEBANDS)
tools.save_text("03_regions.txt", [
    f"Signal window {config.SIGNAL_WINDOW} MeV/c^2: {n_win} candidates",
    f"Sidebands {config.SIDEBANDS} MeV/c^2: "
    f"{sum(tools.count_in(mass, sb) for sb in config.SIDEBANDS)} candidates",
    f"Estimated background in window: {n_win - n_sig:.0f}",
    f"Estimated signal: {n_sig:.0f} +/- {err:.0f}",
    f"Background fraction in window: {(n_win - n_sig) / n_win:.3f}",])