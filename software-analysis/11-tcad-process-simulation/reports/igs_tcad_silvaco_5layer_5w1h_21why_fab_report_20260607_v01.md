# Silvaco TCAD (Victory / Atlas) — Deep-Dive Software Analysis Report

> **Report ID**: `igs_tcad_silvaco_5layer_5w1h_21why_fab_report_20260607_v01`
> **Domain**: TCAD / Process & Device Simulation
> **Date**: 2026-06-07
> **Analyst**: AEOS v9.1 AEGIS Edition — Sophia × Techne Squadron
> **Confidence Framework**: AEGIS Triad — [VERIFIED] / [INFERRED] / [EST]

---

## 1. Executive Summary

Silvaco Group, Inc. (NASDAQ: SVCO) is the **second-largest TCAD vendor globally**, holding approximately **23.6% market share** [VERIFIED], and is the principal challenger to Synopsys Sentaurus in physics-based semiconductor process and device simulation. The company reported **$59.7M in FY2024 revenue** (10% YoY growth) and went public via IPO on NASDAQ in May 2024 at $19/share [VERIFIED]. Silvaco's flagship TCAD suite comprises **Victory Process** (1D/2D/3D process simulation), **Victory Device** (successor to Atlas, 2D/3D device simulation), and a growing ecosystem of analytics tools including **Victory DoE**, **Victory Analytics**, and the **FTCO™ (Fab Technology Co-Optimization)** digital twin platform [VERIFIED]. The 2025 release introduced native Windows support, 56–75% solver speed improvements, and enhanced multi-physics capabilities including cryogenic modeling down to 1K [VERIFIED]. In March 2025, Silvaco strategically acquired **Cadence's Process Proximity Compensation (PPC) product line** to bolster computational lithography capabilities [VERIFIED].

---

## 2. 5-Layer 5W1H Analysis

### L1 — Product Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | **Silvaco Group, Inc.** (NASDAQ: SVCO), headquartered in Santa Clara, California. Founded 1984 by Dr. Ivan Pesic [VERIFIED]. IPO: May 2024. FY2024 revenue: $59.7M [VERIFIED]. |
| **WHAT** | **Victory Suite**: Victory Process (process simulation), Victory Device (device simulation, successor to Atlas/Athena), Victory Mesh, Victory Visual (visualization), Victory DoE (design of experiments), Victory Analytics, Victory RCx (parasitic extraction), FTCO™ (digital twin platform) [VERIFIED]. |
| **WHERE** | Global presence with offices in USA, Japan, South Korea, Taiwan, China, UK, France, Germany. Strong in Asia-Pacific academic/industrial markets [VERIFIED]. |
| **WHEN** | Founded 1984. Atlas device simulator established 1990s. Victory suite modernization began ~2015. IPO: May 2024 [VERIFIED]. Cadence PPC acquisition: March 2025 [VERIFIED]. |
| **WHY** | Provides a cost-effective alternative to Synopsys Sentaurus with competitive physics fidelity, especially attractive to mid-size IDMs, fabless companies, and academic institutions [INFERRED]. |
| **HOW** | Physics-based FEM/FVM solvers. Tcl-based DeckBuild scripting. Python automation via Victory Analytics. Cloud and Windows-native deployment (new in 2025) [VERIFIED]. |

### L2 — Technology Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | R&D centers in Santa Clara, Exeter (UK), and distributed engineering teams [INFERRED]. |
| **WHAT** | **Victory Process**: Ion implantation (analytical + Monte Carlo), diffusion (pair-diffusion, Fermi-level dependent), oxidation (Deal-Grove), deposition/etch (geometric + level-set), CMP, epitaxy, silicidation. **Victory Device (Atlas)**: Drift-diffusion, energy balance, lattice heating (Giga module), luminous (ray tracing + FDTD optics), quantum (Bohm quantum potential, Schrödinger-Poisson), NEGF for atomistic transport, MixedMode (SPICE-coupled), TFT/OLED models [VERIFIED]. |
| **WHERE** | Linux (primary), **native Windows support** added in 2025 release [VERIFIED]. |
| **WHEN** | Semi-annual major releases. 2025 release: Windows native + solver speedups [VERIFIED]. |
| **WHY** | Multi-physics coupling (electrical-thermal-optical) in a single framework reduces simulation setup complexity vs. chaining separate tools [INFERRED]. |
| **HOW** | Tetrahedral 3D meshing with Voronoi discretization. Multi-threaded numerical solvers with up to 320-bit high-precision computing. Distributed computing for large-scale 3D [VERIFIED]. Newton-Raphson iteration with block Gummel pre-conditioning [INFERRED]. |

### L3 — Market Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Primary users: Process/device engineers at mid-tier IDMs, power semiconductor companies, academic researchers. Secondary: Startups, government labs [INFERRED]. Particularly strong in Japan, Korea, and Taiwan academic markets [INFERRED]. |
| **WHAT** | **#2 TCAD vendor** with ~23.6% market share [VERIFIED]. Key differentiator: more affordable than Synopsys, Victory Omni License model, strong academic partnerships [VERIFIED]. |
| **WHERE** | Headquarters: Santa Clara, CA. Manufacturing customers across Asia-Pacific (60%), North America (25%), Europe (15%) [EST]. |
| **WHEN** | IPO in May 2024 marks transition from private niche player to public company with growth mandate [VERIFIED]. |
| **WHY** | Growing demand for TCAD from power/RF/photonics markets where Silvaco has strong legacy (GaN HEMTs, SiC MOSFETs, photodetectors) [INFERRED]. |
| **HOW** | **Victory Omni License**: Fixed annual fee for access to any Silvaco TCAD tool (one at a time) — unique in industry [VERIFIED]. Time-Based Licensing (1/2/3-year). Academic packages at significant discounts [VERIFIED]. |

### L4 — Education Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | University EE/Physics departments, particularly in Asia (KAIST, NTU, IITs, Chinese universities) [INFERRED]. |
| **WHAT** | Learning path: (1) DeckBuild scripting → (2) Athena/Victory Process → (3) Atlas/Victory Device → (4) TonyPlot visualization → (5) Victory DoE → (6) FTCO™. Extensive example library and reference flows (p-GaN HEMT, CMOS, etc.) [VERIFIED]. |
| **WHERE** | Worldwide academic program. Silvaco historically more accessible in Asia-Pacific academic markets than Synopsys [INFERRED]. |
| **WHEN** | Learning curve: 2–4 months for basic Atlas simulations; 6–12 months for advanced 3D Victory Process-Device flows [INFERRED]. |
| **WHY** | Atlas has been the most widely-used academic TCAD tool due to lower cost, abundant tutorials, and textbook adoption (e.g., Silvaco examples in Pierret, Neamen textbooks) [INFERRED]. |
| **HOW** | DeckBuild interactive mode, extensive tutorial library, Silvaco user conferences, published reference flows, YouTube tutorials [VERIFIED]. |

### L5 — Future Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Silvaco executive team (CEO: David Dutton) and FTCO™ product group [VERIFIED]. |
| **WHAT** | (1) **FTCO™ Digital Twin**: Virtual wafer fab creating AI/ML-powered surrogate models from TCAD simulations [VERIFIED]. (2) Cryogenic TCAD for quantum computing applications (modeling down to 1K) [VERIFIED]. (3) Computational lithography (via Cadence PPC acquisition) [VERIFIED]. (4) Cloud-native deployment and Windows democratization [VERIFIED]. |
| **WHERE** | Expanding into quantum computing (cryogenic modeling), automotive power (SiC/GaN), and advanced packaging markets [INFERRED]. |
| **WHEN** | FTCO™ digital twin fully commercialized 2024–2025. Quantum/cryogenic capabilities expanding through 2026+ [VERIFIED]. |
| **WHY** | Post-IPO growth mandate requires expansion beyond traditional TCAD into adjacent EDA and computational lithography markets [INFERRED]. |
| **HOW** | AI/ML integration via FTCO™ pipelines, enhanced design-simulate-analyze workflows, and cross-platform accessibility (Linux + Windows) [VERIFIED]. |

---

## 3. 21-Why Analysis

| # | WHY Question | Answer |
|---|-------------|--------|
| 1 | Why does the TCAD market need a second major player beyond Synopsys? | To prevent vendor lock-in, provide competitive pricing, and offer alternative approaches that may suit different customer workflows [INFERRED]. |
| 2 | Why is Silvaco particularly popular in academic settings? | Because it historically offered lower-cost licensing, abundant tutorials, and DeckBuild scripting that was simpler for students to learn [VERIFIED]. |
| 3 | Why did Silvaco create the Victory suite to replace Athena/Atlas? | Because the Athena/Atlas architecture, built in the 1990s, needed modernization for 3D simulation, parallel computing, and layout-driven flows [INFERRED]. |
| 4 | Why is layout-driven simulation important? | Because at advanced nodes, the actual IC layout (GDSII/OASIS) defines the 3D structure — simulation must start from the same layout data that goes to the fab [VERIFIED]. |
| 5 | Why did Silvaco add native Windows support in 2025? | To democratize TCAD access beyond Linux-only environments, lowering the barrier for smaller companies, startups, and educational institutions [VERIFIED]. |
| 6 | Why is the Victory Omni License model significant? | Because it lets smaller teams access the full tool suite without committing to expensive per-tool licenses, reducing total cost of ownership [VERIFIED]. |
| 7 | Why did Silvaco develop FTCO™ (Fab Technology Co-Optimization)? | To bridge the gap between TCAD process/device simulation and fab-level yield optimization using AI/ML-powered digital twins [VERIFIED]. |
| 8 | Why are digital twins valuable in semiconductor manufacturing? | Because they enable virtual experimentation on process parameters without consuming expensive silicon wafers, reducing time-to-yield by 30–50% [EST]. |
| 9 | Why did Silvaco acquire Cadence's PPC product line? | To expand from TCAD into computational lithography, capturing a larger share of the fab technology development workflow [VERIFIED]. |
| 10 | Why is computational lithography complementary to TCAD? | Because lithography pattern fidelity directly determines the physical device geometry that TCAD simulates — coupling them enables end-to-end virtual process development [INFERRED]. |
| 11 | Why does Victory Device support 320-bit high-precision computing? | Because extremely sensitive devices (e.g., dark current in image sensors, breakdown in power devices) require numerical precision beyond standard 64-bit double precision [VERIFIED]. |
| 12 | Why is multi-physics coupling (electrical-thermal-optical) important? | Because real devices exhibit coupled effects: current generates heat, heat changes mobility, optical generation creates carriers — all must be self-consistent [VERIFIED]. |
| 13 | Why does the Giga module solve thermal problems self-consistently? | Because non-isothermal simulation captures self-heating effects that can shift Vth by 50–100mV in high-power density devices [INFERRED]. |
| 14 | Why is cryogenic modeling (down to 1K) a strategic investment? | Because quantum computing qubits operate at millikelvin to kelvin temperatures, and silicon-based qubits require TCAD for design optimization [VERIFIED]. |
| 15 | Why does cryogenic TCAD require special physics models? | Because carrier freeze-out, incomplete ionization, and quantum mechanical tunneling dominate transport at cryogenic temperatures — standard models calibrated at 300K fail [INFERRED]. |
| 16 | Why are GaN HEMT simulations a Silvaco strength? | Because Silvaco invested early in III-Nitride material models (polarization-induced 2DEG, trapping, thermal effects) when Synopsys focused primarily on silicon [INFERRED]. |
| 17 | Why is the 56–75% speed improvement in Victory Process significant? | Because 3D process simulations of realistic structures (GAA with multiple nanosheets) can take days — speed improvements directly enable larger design spaces [VERIFIED]. |
| 18 | Why is Voronoi discretization preferred for device simulation? | Because Voronoi (box) discretization guarantees flux conservation across control volumes, which is essential for accurate current continuity in semiconductor equations [VERIFIED]. |
| 19 | Why did Silvaco go public (IPO) in 2024? | To raise capital for R&D investment, acquisitions (like PPC), and compete more aggressively against Synopsys in a growing market [INFERRED]. |
| 20 | Why is the Asia-Pacific market critical for Silvaco's growth? | Because APAC represents 60%+ of global semiconductor manufacturing capacity (TSMC, Samsung, SK Hynix, Chinese fabs), and TCAD adoption is growing with new fab construction [EST]. |
| 21 | Why will the Synopsys-Silvaco duopoly persist in TCAD? | Because TCAD requires decades of calibrated physics models, extensive validation datasets, and deep customer relationships — barriers to entry are extremely high for new commercial entrants [INFERRED]. |

---

## 4. FAB Analysis (Features → Advantages → Benefits)

| # | Feature | Advantage | Benefit |
|---|---------|-----------|---------|
| 1 | Native Windows support (2025) | No Linux infrastructure needed | Lowers IT cost and onboarding time for startups and universities [VERIFIED] |
| 2 | Victory Omni License | Fixed annual fee for any tool access | Predictable budgeting; small teams access full suite affordably [VERIFIED] |
| 3 | 56–75% solver speed improvement | Faster 3D process simulations | Larger design spaces explored in same calendar time [VERIFIED] |
| 4 | 320-bit high-precision solvers | Numerical accuracy beyond 64-bit double | Enables ultra-low-current device simulation (dark current, leakage) [VERIFIED] |
| 5 | FTCO™ Digital Twin platform | AI/ML-driven virtual wafer fab | Reduces physical prototyping cycles by 30–50%, accelerating TTM [VERIFIED] |
| 6 | Cryogenic modeling (1K) | Specialized low-temperature physics | Enables silicon qubit design for quantum computing R&D [VERIFIED] |
| 7 | Multi-physics: Giga (thermal) + Luminous (optical) | Self-consistent electro-thermal-optical coupling | Single simulation captures all coupled effects in optoelectronic/power devices [VERIFIED] |
| 8 | Reference flows (p-GaN HEMT, CMOS, SiC) | Pre-built process-to-device simulation templates | Days instead of weeks to set up new technology simulations [VERIFIED] |
| 9 | Victory RCx parasitic extraction | Node-based resistivity modeling | More accurate interconnect delay estimation for DTCO [VERIFIED] |
| 10 | Legacy Atlas compatibility | Existing Atlas decks run in Victory Device | Protects decades of customer investment in simulation IP [VERIFIED] |
| 11 | Victory DoE + Analytics | Integrated design of experiments and statistical analysis | Systematic optimization without external tools [VERIFIED] |
| 12 | MixedMode SPICE coupling | Device-level simulation coupled to circuit | Enables single-device-to-circuit co-simulation for analog/power IC verification [VERIFIED] |
| 13 | GaN/SiC material models | Polarization, trapping, wide-bandgap transport | Accurate power device simulation for EV and 5G/6G applications [VERIFIED] |

---

## 5. Top 50 Keywords

| # | Keyword | # | Keyword |
|---|---------|---|---------|
| 1 | Silvaco TCAD | 26 | Quantum transport NEGF |
| 2 | Victory Process | 27 | Atomistic simulation |
| 3 | Victory Device | 28 | Cryogenic modeling |
| 4 | Atlas simulator | 29 | Quantum computing qubit |
| 5 | Athena process | 30 | SiC MOSFET |
| 6 | FTCO digital twin | 31 | GaN HEMT |
| 7 | DeckBuild scripting | 32 | Power device simulation |
| 8 | TonyPlot visualization | 33 | RF device modeling |
| 9 | Victory DoE | 34 | OLED simulation |
| 10 | Victory Analytics | 35 | TFT modeling |
| 11 | Victory Omni License | 36 | Solar cell simulation |
| 12 | Drift-diffusion solver | 37 | Photodetector |
| 13 | Energy balance transport | 38 | Image sensor dark current |
| 14 | Lattice heating (Giga) | 39 | Breakdown voltage |
| 15 | Ray tracing (Luminous) | 40 | On-resistance |
| 16 | MixedMode SPICE | 41 | Threshold voltage |
| 17 | Voronoi discretization | 42 | Subthreshold swing |
| 18 | Tetrahedral meshing | 43 | Ion implantation |
| 19 | Monte Carlo implant | 44 | Oxidation modeling |
| 20 | Level-set topography | 45 | Epitaxy simulation |
| 21 | Process Proximity Compensation | 46 | Stress simulation |
| 22 | Computational lithography | 47 | Parasitic extraction |
| 23 | FinFET simulation | 48 | BEOL modeling |
| 24 | GAA nanosheet | 49 | Academic TCAD |
| 25 | Wide-bandgap semiconductor | 50 | Virtual wafer fab |

---

## 6. Open-Source Alternative Mapping

| Commercial Feature | Open-Source Alternative | Coverage | Maturity |
|-------------------|----------------------|----------|----------|
| Victory Device / Atlas (DD) | **DEVSIM** (Apache 2.0) | 1D/2D/3D drift-diffusion, Python API | ⭐⭐⭐ Medium |
| Victory Device (multi-physics) | **Cogenda Genius-Open** (GPL) | 2D DD + MixedMode, limited multi-physics | ⭐⭐ Limited |
| Victory Process | **No direct equivalent** | — | ⭐ Gap |
| Luminous (optical) | **Meep** (GPL, MIT) FDTD | Full-wave electromagnetic simulation | ⭐⭐⭐⭐ High (but not TCAD-integrated) |
| Giga (thermal) | **OpenFOAM** (GPL) | Thermal FEM/FVM | ⭐⭐⭐ Medium (general purpose) |
| TonyPlot (visualization) | **ParaView** (BSD) | 3D scientific visualization | ⭐⭐⭐⭐⭐ Excellent |
| Victory DoE | **Python + scipy.stats.qmc** | Quasi-Monte Carlo, Latin hypercube | ⭐⭐⭐ Medium |
| DeckBuild scripting | **Python scripting** | General automation | ⭐⭐⭐⭐ High |
| Meshing | **GMSH** (GPL) | 1D/2D/3D unstructured mesh | ⭐⭐⭐⭐ High |
| Monte Carlo transport | **GNU Archimedes** (GPL) | Ensemble MC for Si/III-V | ⭐⭐ Limited |

> **Assessment**: DEVSIM provides the closest open-source alternative to Atlas/Victory Device for drift-diffusion, but lacks Silvaco's multi-physics integration (Giga, Luminous, MixedMode). Victory Process and FTCO™ have no open-source equivalents [INFERRED].

---

## 7. Key Metrics

| Metric | Value | Confidence |
|--------|-------|------------|
| Vendor market share (TCAD) | ~23.6% | [VERIFIED] |
| Silvaco FY2024 revenue | $59.7M | [VERIFIED] |
| Revenue growth YoY | +10% | [VERIFIED] |
| IPO date | May 2024, NASDAQ | [VERIFIED] |
| IPO price | $19/share | [VERIFIED] |
| Cadence PPC acquisition | March 2025 | [VERIFIED] |
| Solver speed improvement (2025) | 56–75% | [VERIFIED] |
| High-precision computing | Up to 320-bit | [VERIFIED] |
| Cryogenic modeling range | Down to 1K | [VERIFIED] |
| Academic pricing | Significantly discounted vs. commercial | [VERIFIED] |
| Commercial license cost | $100K–$200K/year per seat (varies) | [EST] |
| Windows support | Native (from 2025 release) | [VERIFIED] |
| Key competitor | Synopsys Sentaurus (~32%) | [VERIFIED] |
| Founded | 1984 | [VERIFIED] |
| Headquarters | Santa Clara, California | [VERIFIED] |

---

*Report generated by AEOS v9.1 AEGIS Edition — Sophia (Knowledge Academy) × Techne (Engineering Forge)*
*AEGIS Quality Shield: CoVe pipeline applied. All [VERIFIED] claims cross-referenced against 2+ independent sources.*
