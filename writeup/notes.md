# Project notes: B± → K⁺K⁻K± decay asymmetry


## Setup

- Python version: Python 3.15.2
- Package versions: uproot, numpy, scipy, matplotlib
- Data: CERN Open Data record 4900, files `B2HHH_MagnetDown.root` and `B2HHH_MagnetUp.root`
- Number of candidates in each file:
- GitHub repository link: https://github.com/AdityaRishi271828/LHCb-B-to-KKK-asymmetry.git



## Exploring the data


| Variable | Meaning | 
| --- | --- |
| H1_PX, PY, PZ | Momentum componants x,y,z for particle 1 |
| H1_Charge | Charge of particle 1|
| H1_ProbK | Probability that the particle is a kaon|
| H1_ProbPi | Probability that the particle is a pion |
| H1_isMuon | 1 if the particle is a muon |
| B_FlightDistance | Distance travelled from collision sight |


- The unselected mass plot looks like a linear line with negative gradient, and the peak is hard to see. This is due to the number of incorrect particles


## Step 2: Selection


- **Chosen cuts:** ProbK > 0.5 , ProbPi < 0.2 , isMuon = 0
- These values for K and Pi allowed for minimal background noise while maintaining a clear plateu (I tested a few in the mass_peak notebook)
- Alternatives: loose = (0.4, 0.3), tight = (0.6, 0.1)



| Selection | Proportion of Original Data | 
| --- | --- |
| All candidates |8556118 (100.00%)|
| Total charge is +/-1 | 8556118 (100.00%)|
| Not Muon | 6311517 ( 73.77%)|
| All three ProbK > 0.5 | 26959 (0.32%) |
| All three ProbPi < 0.2 | 15958 (0.19%) |

- The remaining items have a small but still existent chance of being a mis-identified particle.

---

## Step 3: Signal window and sidebands

- Peak position μ from fit: ___ ± ___ MeV/c²
- Width σ from fit: ___ ± ___ MeV/c²
- FWHM from half-height method: ___  → σ = FWHM / 2.355 = ___ (agrees with fit?)
- **Signal window:** 5264 to 5304 MeV/c² (= μ ± ___σ) 
- **Sidebands:** ___ and ___ MeV/c². Why here, and why they contain no signal:
- Is the background close to linear? Any concern about the low-mass side?
- Window variations chosen: ___ and ___
- Significance level chosen: ___ and why
- Estimated signal and background in window (copy from `results/03_regions.txt`):
- Date and commit of the `selection-fixed` tag:

---

## Step 4: Asymmetry

Copy from `results/04_asymmetry.txt`:

- N(B⁺) = ___ ± ___
- N(B⁻) = ___ ± ___
- Raw asymmetry A = ___ ± ___
- z = ___ , p = ___
- H₀ rejected? ___
- Binomial uncertainty √((1−A²)/N) calculated by hand: ___ . How much larger is the real uncertainty, and why?
- Difference between B⁺ and B⁻ peaks visible by eye?

---

## Step 5: Checks

| Check | Result | Interpretation |
| --- | --- | --- |
| Polarity: Down | A = | |
| Polarity: Up | A = | |
| Polarity difference | z = , p = | Agree? What would disagreement mean? |
| Sideband asymmetry | A = | Is the background asymmetric? |
| Loose selection | A = | Shift relative to nominal? |
| Tight selection | A = | |
| Narrow window | A = | Stable? |
| Wide window | A = | |

- Reminder: overlapping samples should differ by *less* than their combined uncertainty.
- Any check that worried you, and what you think caused it:

---

## Step 6: Interpretation and literature

| Quantity | Value | Uncertainty | Source |
| --- | --- | --- | --- |
| LHCb A_CP(B± → K⁺K⁻K±) | −0.043 | ±0.009 (stat) ±0.003 (syst) ±0.007 (J/ψK) → total ±0.012 | LHCb, PRL 111, 101801 (2013) |
| B± production asymmetry at LHCb | | | |
| Kaon detection asymmetry at LHCb | | | |
| Mass of B± | | | PDG |
| Mass of K± | 493.677 MeV/c² | | PDG |

- Comparison of my A with LHCb's A_CP using Equation 3.10: z = ___
- Could A_P + A_D explain the difference? Could they explain my whole result?
- **What I can honestly claim:**
- What I cannot claim:
- Statistical vs systematic: which dominates, and the evidence:

---

## Improvements and further work

- Control channel (B± → J/ψK±) to remove A_P and A_D
- Fit the mass peak instead of counting
- Larger datasets from later LHC runs
- Other ideas:

---

## Context for the introduction

- Sakharov conditions (with reference):
- Why the Standard Model's CP violation is too small (with reference):
- Quark content of B⁺ and B⁻; tree and penguin diagrams:
- Why two amplitudes with different weak and strong phases are needed:

---

## Problems encountered and how they were solved

(Useful for the method section and for interviews.)

- e.g. `select.py` clashed with Python's built-in `select` module — renamed to `02_select.py`
-

---

## References collected

1.
2.
3.

---

## Acknowledgements and tools

- Note any help received, including AI assistance, as required by the journal's policy.