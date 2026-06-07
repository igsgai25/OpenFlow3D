# Report 8: Verification & Validation — Trust in 3D CFD

**PhD-Level Deep Research Report** | **All Theories** | Generated: 2026-06-07

---

## Executive Summary

Verification and Validation (V&V) is the cornerstone of credibility in computational fluid dynamics. Without rigorous V&V, simulation results are merely colorful pictures — potentially misleading and dangerously unreliable. ASME V&V 20-2009 and NASA-STD-7009A establish the framework for assessing CFD credibility. This report provides a PhD-level analysis of V&V methodology, grid convergence, uncertainty quantification, and benchmark databases for 3D flow simulation.

---

## 1. Fundamental Concepts

### 1.1 Definitions (AIAA G-077-1998)

- **Verification**: "Solving the equations right" — assessing numerical accuracy
- **Validation**: "Solving the right equations" — assessing physical model accuracy
- **Uncertainty**: A potential deficiency due to lack of knowledge
- **Error**: A recognizable deficiency not due to lack of knowledge

### 1.2 V&V Hierarchy

```
Level 4: Complete System (full aircraft, full engine)
  |
Level 3: Subsystem (wing + body, combustor + turbine)
  |
Level 2: Benchmark Cases (backward-facing step, Ahmed body, flat plate BL)
  |
Level 1: Unit Problems (channel flow, pipe flow, cylinder flow)
```

### 1.3 Verification Methods

| Method | Purpose | Key Reference |
|:---|:---|:---|
| Grid Convergence Index (GCI) | Estimate discretization error | Roache (1994) |
| Richardson Extrapolation | Estimate exact solution from grid sequence | Richardson (1911) |
| Order of Accuracy Test | Verify formal vs observed order | ASME V&V 20 |
| Method of Manufactured Solutions (MMS) | Verify code correctness | Salari & Knupp (2000) |
| Iterative Convergence | Ensure solver convergence | |
| Solution Sensitivity | Assess sensitivity to parameters | |

### 1.4 Grid Convergence Index (GCI)

For three grids with refinement ratio r and observed order p:

```
GCI_fine = F_s * |epsilon| / (r^p - 1)
```

where:
- F_s = 1.25 (safety factor for 3+ grids, Roache recommends 3.0 for 2 grids)
- epsilon = (f_2 - f_1) / f_1 (relative change)
- r = h_coarse / h_fine (refinement ratio)
- p = ln((f_3 - f_2)/(f_2 - f_1)) / ln(r) (observed order)

**Asymptotic range check**: GCI_coarse / (r^p * GCI_fine) should be close to 1.0

---

## 2. Five-Layer 5W1H Analysis

### Layer 1: Surface

| Q | Analysis |
|:---|:---|
| **What** | Systematic assessment of CFD simulation credibility through numerical verification and experimental validation |
| **Who** | Roache (GCI, 1994), Oberkampf & Trucano (V&V framework, 2002), ASME V&V 20 Committee |
| **When** | Every CFD simulation should include V&V; mandatory for safety-critical applications (nuclear, aerospace) |
| **Where** | All CFD software (ANSYS, Star-CCM+, FLOW-3D, OpenFOAM); all application domains |
| **Why** | Without V&V, simulation results have unknown accuracy — could lead to design failures and safety incidents |
| **How** | Verification: grid study + code verification; Validation: comparison with experimental data + UQ |

### Layer 2: Mechanism

| Q | Analysis |
|:---|:---|
| **What** | Discretization error (grid), modeling error (turbulence model), input uncertainty (BCs, properties), human error (setup) |
| **Who** | CFD analysts perform V&V; standards bodies (ASME, AIAA, NASA) define procedures |
| **When** | Verification: before production runs; Validation: before trusting results for decisions |
| **Where** | Error sources: spatial discretization, temporal discretization, iterative convergence, round-off, modeling |
| **Why** | Each error source is independent; total uncertainty = combination (RSS or worst-case) of all sources |
| **How** | Systematic grid refinement (at least 3 levels); comparison with experimental data + uncertainty bands |

### Layer 3: Mathematics

| Q | Analysis |
|:---|:---|
| **What** | Richardson extrapolation: f_exact = f_h + C*h^p + O(h^(p+1)); GCI quantifies discretization uncertainty |
| **Who** | Richardson (1911, extrapolation), Roache (1994, GCI), Eqa et al. (2014, systematic V&V procedure) |
| **When** | Applicable when solution is in the asymptotic range (observed order ~ formal order) |
| **Where** | In discretization error space: monotonic convergence required for GCI to be meaningful |
| **Why** | Asymptotic analysis provides mathematical framework for estimating the "unknown" exact solution |
| **How** | Three grids with constant refinement ratio (r=1.3-2.0); compute observed order p; compute GCI |

### Layer 4: Computation

| Q | Analysis |
|:---|:---|
| **What** | Grid convergence study: 3+ meshes with controlled refinement; MMS for code verification |
| **Who** | Every CFD user should perform; required by ASME V&V 20, NASA-STD-7009A for credibility |
| **When** | Grid study: before reporting any results; code verification: during software development |
| **Where** | QoI (Quantities of Interest): drag, lift, pressure drop, heat transfer coefficient, local velocities |
| **Why** | Different QoIs may have different convergence rates; must assess each independently |
| **How** | Automate: parametric mesh generation -> batch solve -> extract QoIs -> compute GCI -> plot convergence |

### Layer 5: Application

| Q | Analysis |
|:---|:---|
| **What** | Industry-specific V&V: aerospace (AIAA standards), nuclear (NRC regulatory guides), automotive (SAE J2966) |
| **Who** | Regulatory bodies mandate V&V for safety-critical applications; journals require for publication |
| **When** | Pre-certification: V&V package submitted to FAA/NRC/FDA; publication: required by J. Fluids Eng. |
| **Where** | Aerospace: AIAA CFD V&V guidelines; Nuclear: NRC Standard Review Plan; Biomedical: FDA V&V guidance |
| **Why** | Regulatory acceptance of CFD depends on demonstrated credibility; liability drives rigor |
| **How** | V&V plan -> execution -> documentation -> review -> acceptance by regulator/reviewer |

---

## 3. Twenty-One Why Analysis

| # | Why Question | Answer |
|:---:|:---|:---|
| 1 | Why is V&V essential? | CFD predictions without V&V have unknown accuracy — they may be completely wrong |
| 2 | Why separate verification from validation? | Verification checks math/numerics (code correctness); validation checks physics (model accuracy) — different things |
| 3 | Why use three or more grids? | Three grids enable computing the observed order of accuracy; two grids assume the formal order |
| 4 | Why is the safety factor F_s needed? | GCI estimates discretization error, which is uncertain itself; F_s provides a confidence margin |
| 5 | Why does Roache recommend F_s=1.25? | With 3+ grids and observed order, the uncertainty in the error estimate is lower, justifying a smaller safety factor |
| 6 | Why can't we just use the finest mesh? | Even the finest mesh has discretization error; GCI quantifies this remaining error |
| 7 | Why is the asymptotic range important? | GCI is only valid when the solution converges monotonically at the expected rate |
| 8 | Why does non-monotonic convergence occur? | Insufficient resolution, competing error terms, or grid-dependent flow features (separation point movement) |
| 9 | Why is MMS the gold standard for code verification? | It provides a known exact solution for any PDE; any discretization error is guaranteed to be a code bug |
| 10 | Why is turbulence model validation problematic? | Experimental data has its own uncertainty; model constants are calibrated to specific flows |
| 11 | Why is experimental uncertainty often ignored? | Experimentalists report uncertainty; CFD practitioners often compare with "exact" experimental values |
| 12 | Why should V&V be QoI-specific? | Different quantities converge at different rates; a grid adequate for pressure may be inadequate for wall shear stress |
| 13 | Why is user error the largest source of CFD error? | Incorrect BC, wrong turbulence model, poor mesh quality, wrong physical properties — all user choices |
| 14 | Why are benchmark databases important? | Standard test cases with well-defined BCs and high-quality experimental data enable reproducible validation |
| 15 | Why is the ERCOFTAC database valuable? | It provides curated benchmark cases specifically designed for turbulence model validation |
| 16 | Why is uncertainty quantification (UQ) emerging? | Single-point V&V is insufficient; UQ propagates input uncertainties to output predictions |
| 17 | Why use polynomial chaos for UQ? | It provides spectral convergence in probability space; more efficient than Monte Carlo for moderate dimensions |
| 18 | Why is Bayesian calibration gaining traction? | It quantifies model parameter uncertainty using Bayes' theorem; provides posterior distributions |
| 19 | Why do journals increasingly require V&V? | Journal of Fluids Engineering policy (2002): grid convergence study required for any CFD paper |
| 20 | Why is V&V a cultural challenge? | Engineers want "the answer"; V&V reveals uncertainty, which is uncomfortable but necessary |
| 21 | Why will V&V become even more important? | As CFD is used for certification (FDA, FAA), legal liability demands documented, traceable V&V evidence |

---

## 4. Key V&V Benchmark Cases

| # | Benchmark | Key QoIs | Re Range | Data Quality |
|:---:|:---|:---|:---|:---|
| 1 | Turbulent channel flow (DNS) | u+, Reynolds stresses | 180-5200 | Excellent (DNS) |
| 2 | Backward-facing step | Reattachment length, Cp | 5000-40000 | Good |
| 3 | Flow over cylinder | Cd, St, Cp distribution | 100-10^6 | Excellent |
| 4 | Ahmed body | Cd, wake structure | 2.8 x 10^6 | Good |
| 5 | NASA CRM (Common Research Model) | CL, CD, Cp | 5 x 10^6 | Excellent |
| 6 | DrivAer car model | Cd, surface pressures | 4.9 x 10^6 | Good |
| 7 | Lid-driven cavity | Velocity profiles | 100-10000 | Excellent (reference solutions) |
| 8 | NACA 0012 airfoil | CL, CD, transition point | 3-6 x 10^6 | Excellent |
| 9 | Flat plate boundary layer | Cf, BL profiles | 10^5-10^7 | Excellent (Coles law) |
| 10 | Taylor-Green vortex | Enstrophy, dissipation | DNS | Exact (analytical IC) |

---

*Report 8 of 10 | Flow in 3D PhD Research Project | AEOS Director Sigma v9.1*
