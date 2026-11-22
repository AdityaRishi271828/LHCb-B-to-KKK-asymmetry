import numpy as np

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])) 

import uproot
from scipy import stats

import config

TRACKS = (1, 2, 3)
TRACK_VARS = ("PX", "PY", "PZ", "Charge", "ProbK", "ProbPi", "isMuon")
BRANCHES = [f"H{i}_{v}" for i in TRACKS for v in TRACK_VARS]



# Reading Data
def load(polarity, entry_stop=None, branches=BRANCHES):
    with uproot.open(str(config.FILES[polarity])) as f:
        return f[config.TREE].arrays(branches, entry_stop=entry_stop, library="np")

def iterate(polarity, step_size="100 MB", branches=BRANCHES):
    path = str(config.FILES[polarity]) + ":" + config.TREE
    yield from uproot.iterate(path, branches, step_size=step_size, library="np")



# Energy
def energy(PX, PY, PZ, m):
    return np.sqrt(PX**2 + PY**2 + PZ**2 + m**2)

def three_body_mass(d, m=config.M_K):
    E = sum(energy(d[f"H{i}_PX"], d[f"H{i}_PY"], d[f"H{i}_PZ"], m) for i in TRACKS)
    px = sum(d[f"H{i}_PX"] for i in TRACKS)
    py = sum(d[f"H{i}_PY"] for i in TRACKS)
    pz = sum(d[f"H{i}_PZ"] for i in TRACKS)
    return np.sqrt(np.maximum(E**2 - px**2 - py**2 - pz**2, 0.0))

x = three_body_mass(1)
print(x)