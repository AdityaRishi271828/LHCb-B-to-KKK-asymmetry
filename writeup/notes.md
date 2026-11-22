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


## Selection


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



## Signal window and sidebands

- Peak position μ from fit: 5284 MeV/c²
- Width σ from fit: 16.6 MeV/c²
- FWHM from half-height method: 39.2  → σ = FWHM / 2.355 = 16.6 MeV/c² which is the same
- **Signal window:** 5264 to 5304 MeV/c² (centre 5284, ± 20 MeV/c² (half-width)). 
- **Sidebands:** 5100–5150 and 5400–5450 MeV/c² (total width 100 MeV/c²). These were visibly far away from the peak and in a purely linear section.
- Scale factor r = w_window / w_sidebands = 40 / 100 = 0.4
- Window variations chosen: 5267–5301 (half-width 17) and 5251–5317 (half-width 33) MeV/c²
- Significance level chosen: 0.0027 (3σ)
- From `results/03_regions.txt`:
    - Candidates in signal window: 8413
    - Candidates in sidebands: 890
    - Estimated background in window: 356 (= 0.4 × 890)
    - Estimated signal: 8057 ± 92
    - Background fraction in window: 0.042 (4.2%)



## Asymmetry

From `results/04_asymmetry.txt`:

- N(B⁺) = 4226 ± 67
- N(B⁻) = 3831 ± 64
- Total signal N = 8057 
- Raw asymmetry A = −0.0491 ± 0.0115
- z = −4.28 , two-sided p ≈ 1.9 × 10⁻⁵ 
- Therefore H₀ rejected at the 0.0027 level
- Binomial uncertainty √((1−A²)/N) by hand: √((1 − 0.0491²) / 8057) = 0.0111. The real uncertainty (0.0115) is about 3% larger ??




## Checks

From `results/05_checks.txt`. Nominal: A = −0.0491 ± 0.0115.

| Check | Result | Interpretation |
| --- | --- | --- |
| Polarity: Down | A = −0.0496 ± 0.0149 | |
| Polarity: Up | A = −0.0483 ± 0.0179 | |
| Polarity difference | z = 0.06, p = 0.953 | negligable |
| Sideband asymmetry | N⁺ = 452, N⁻ = 438, A = −0.0157 ± 0.0335 | Symmetric |
| Loose selection (ProbK > 0.4, ProbPi < 0.3) | A = -0.0470 ± 0.0097 | Increased |
| Tight selection (ProbK > 0.6, ProbPi < 0.1) | A = -0.0576 ± 0.0222 | Decreased |
| Narrow window (5267–5301) | A = −0.0508 ± 0.0121 |  |
| Wide window (5251–5317) | A = −0.0505 ± 0.0105 | |

- Reminder: overlapping samples should differ by *less* than their combined uncertainty.
- Any check that worried you, and what you think caused it:



##  Interpretation and literature
 
| Quantity | Value | Uncertainty | Source |
| --- | --- | --- | --- |
| LHCb A_CP(B± → K⁺K⁻K±) | −0.043 | ±0.009 (stat) ±0.003 (syst) ±0.007 (J/ψK) → total ±0.012 | LHCb, PRL 111, 101801 (2013), arXiv:1306.1246 |
| LHCb raw asymmetry A_raw(KKK), same paper | −0.060 | ±0.007 (stat) | LHCb, PRL 111, 101801 (2013) — from 22 119 ± 164 signal decays |
| LHCb correction A_Δ = A_D(K±) + A_P(B±) | not quoted directly; measured from ~6.3 × 10⁴ B± → J/ψK± decays | | LHCb, PRL 111, 101801 (2013), Eqs. 2–3 |
| B± production asymmetry at LHCb, √s = 7 TeV (2011 data) | −0.41% (−0.0041) | ±0.49% (stat) ±0.10% (syst) | LHCb, Phys. Rev. D 95, 052005 (2017) |
| Kaon detection asymmetry at LHCb (per kaon, approximate) | −0.96% (−0.0096) | ±0.13% | LHCb, arXiv:2012.09903 (B± → DK± analysis, Run 1 + 2) — not specific to 2011 |
| Mass of B± | 5279.41 MeV/c² | ±0.07 MeV/c² | PDG (Navas et al., Phys. Rev. D 110, 030001 (2024)) |
| Mass of K± | 493.677 MeV/c² | ±0.015 MeV/c² | PDG |

