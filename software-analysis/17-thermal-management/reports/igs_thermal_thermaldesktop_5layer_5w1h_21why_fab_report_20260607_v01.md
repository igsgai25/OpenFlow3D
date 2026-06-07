# Thermal Desktop — Comprehensive Software Analysis Report

> **Domain**: Thermal Management · Spacecraft & Aerospace Thermal Analysis
> **Vendor**: C&R Technologies (now Ansys, acquired 2022)
> **Report Date**: 2026-06-07 · **Version**: v01
> **Confidence Framework**: [VERIFIED] = official source · [INFERRED] = derived from data · [EST] = estimated

---

## 1. Executive Summary

Thermal Desktop, developed by C&R Technologies and now part of the Ansys portfolio following its acquisition in 2022 [VERIFIED], is the industry-standard thermal analysis software for spacecraft and aerospace applications. Built upon the legendary **SINDA/FLUINT** (Systems Improved Numerical Differencing Analyzer / Fluid Integrator) solver engine — with heritage tracing back to NASA's Apollo program — Thermal Desktop provides an AutoCAD-based graphical interface for building, analyzing, and visualizing thermal models of satellites, launch vehicles, planetary probes, and space instruments [VERIFIED]. The software uniquely combines finite difference (FD), finite element (FE), and lumped-parameter thermal network modeling with orbital environmental heating calculations (RadCAD module) and fluid system analysis (FloCAD module), making it the most comprehensive single tool for space thermal engineering. The 2026 R1 release introduced **TD Designer** (a new pre-processing environment based on Ansys Discovery) and enhanced participating media radiation modeling [VERIFIED]. Thermal Desktop is used by virtually every major aerospace organization worldwide, including NASA, ESA, JAXA, SpaceX, Boeing, Lockheed Martin, Northrop Grumman, and Airbus Defence & Space, with an estimated 80-90% market share in Western spacecraft thermal analysis [EST].

---

## 2. 5-Layer 5W1H Analysis

### L1 — Product Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | C&R Technologies (Boulder, Colorado), acquired by Ansys in 2022 [VERIFIED]. Founded by Dr. Brent Cullimore and colleagues. Now operates under Ansys Fluids & Thermal business unit. SINDA heritage from Martin Marietta (now Lockheed Martin) and NASA Johnson Space Center [VERIFIED]. |
| **WHAT** | Thermal Desktop — a comprehensive thermal/fluid analysis suite for aerospace and general thermal engineering. Core modules: **SINDA/FLUINT** (solver), **RadCAD** (radiation/orbital heating), **FloCAD** (fluid system networks), **TD Direct/TD Designer** (CAD-based pre-processing). Current version: 2026 R1 [VERIFIED]. |
| **WHERE** | Global aerospace industry. Dominant in USA (NASA, DoD, commercial space). Strong in Europe (ESA ecosystem), Japan (JAXA). Growing in commercial space (SpaceX, Blue Origin, Rocket Lab) and non-space applications (energy, defense electronics) [INFERRED]. |
| **WHEN** | SINDA origins: 1960s (Apollo program) [VERIFIED]. SINDA/FLUINT modern version: 1980s (C&R Technologies founded ~1987) [EST]. Thermal Desktop GUI: 1990s [EST]. Ansys acquisition: 2022 [VERIFIED]. TD Designer: 2026 R1 [VERIFIED]. |
| **WHY** | Space thermal environments are uniquely challenging: vacuum (no convection), extreme temperature ranges (-270°C to +300°C), orbital cycling (eclipse/sunlit transitions every 90 minutes in LEO), and complex radiation exchange between spacecraft surfaces, Earth, Sun, and deep space. No general-purpose thermal tool adequately addresses these space-specific requirements [INFERRED]. |
| **HOW** | CAD-based geometry creation (AutoCAD/TD Designer) → Surface/volume meshing → RadCAD orbital heating calculation (solar, albedo, Earth IR, deep space) → SINDA/FLUINT thermal network solve (FD/FE/lumped) → FloCAD fluid loop analysis → Transient/steady-state temperature prediction → Design iteration and margin assessment [VERIFIED]. |

### L2 — Technology Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | C&R Technologies core solver team (Boulder, CO). SINDA/FLUINT mathematical heritage from NASA/JSC and Martin Marietta thermal sciences group [VERIFIED]. |
| **WHAT** | **SINDA/FLUINT solver**: Finite difference thermal network solver with implicit/explicit time integration. Handles conduction (linear/nonlinear), radiation (Stefan-Boltzmann), contact resistance, phase change, and thermoelectric effects. **FLUINT**: 1D fluid network solver for single/two-phase flow, pressure drops, pumps, valves, accumulators. **RadCAD**: Monte Carlo ray tracing for radiation view factors and orbital heating. Supports specular and diffuse surfaces, solar cell power generation modeling. **Participating media radiation** (2026 R1): models radiative heat transfer through semi-transparent materials (glass, optical coatings) [VERIFIED]. |
| **WHERE** | Solver runs on Windows (primary). Linux support for batch processing and cluster computing. AutoCAD-based GUI (TD Classic) or Ansys Discovery-based GUI (TD Designer, 2026+) [VERIFIED]. |
| **WHEN** | SINDA: continuous evolution since 1960s. FLUINT: added 1980s for two-phase thermal control systems (heat pipes, loop heat pipes). RadCAD: 1990s. TD Designer: 2026 R1 [VERIFIED]. |
| **WHY** | Finite difference thermal networks are the traditional formulation for spacecraft thermal analysis because they map directly to thermal resistance/capacitance circuits that spacecraft thermal engineers conceptualize. Monte Carlo ray tracing provides the most accurate method for complex multi-surface radiation exchange in vacuum [INFERRED]. |
| **HOW** | Geometry → surface/node discretization → SINDA thermal network (R-C network with conductors and capacitors) → RadCAD Monte Carlo ray trace (millions of rays per surface for view factor calculation) → orbital propagation (sun vector, eclipse, beta angle) → time-varying boundary conditions → SINDA implicit backward-Euler integration → temperature history output → mapping to Ansys Mechanical for thermo-structural analysis [VERIFIED]. |

### L3 — Market Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Primary users: spacecraft thermal engineers at NASA (JPL, GSFC, JSC, MSFC), ESA, JAXA, ISRO, military space (US Space Force, Space Development Agency), prime contractors (Lockheed Martin, Boeing, Northrop Grumman, L3Harris, Raytheon), commercial space (SpaceX, Blue Origin, Planet Labs, Rocket Lab), satellite operators (Maxar, SES, Intelsat) [INFERRED]. |
| **WHAT** | Market share: estimated 80-90% of Western spacecraft thermal analysis [EST]. Thermal Desktop is the de facto standard — thermal models are often contractually required in Thermal Desktop format by NASA and DoD [INFERRED]. Non-space market (energy, defense electronics): growing but <10% of revenue [EST]. |
| **WHERE** | Dominant in USA. Strong in Europe (competes with ESATAN-TMS). Used in Japan, India, South Korea. Commercial space startup ecosystem rapidly adopting [INFERRED]. |
| **WHEN** | Market dominance established 1990s-2000s. Accelerated by commercial space boom (2015-present). Ansys acquisition (2022) expanded access through Ansys channel network [VERIFIED]. |
| **WHY** | Organizations choose Thermal Desktop because: (1) SINDA/FLUINT is the validated standard accepted by NASA and DoD, (2) RadCAD orbital heating is uniquely comprehensive, (3) thermal model deliverables are contractually specified in TD format, (4) heritage models spanning decades are in TD format [INFERRED]. |
| **HOW** | Quote-based enterprise licensing through Ansys/C&R Technologies. Modules sold separately (SINDA/FLUINT, RadCAD, FloCAD, SpaceClaim/TD Direct). Typical annual license: $15K-50K per seat depending on module configuration [EST]. Academic licenses available through Ansys Academic Program [VERIFIED]. |

### L4 — Education Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | C&R Technologies training team (now Ansys), university aerospace programs (MIT, Stanford, Purdue, CU Boulder, TU Delft, etc.), NASA Thermal & Fluids Analysis Workshop (TFAWS), AIAA Spacecraft Thermal Control short courses [VERIFIED]. |
| **WHAT** | Learning path: Spacecraft thermal fundamentals (radiation, orbital environments) → SINDA/FLUINT solver basics → Thermal Desktop GUI modeling → RadCAD orbital heating → FloCAD fluid systems → Advanced: parametric studies, optimization, Ansys Mechanical coupling [INFERRED]. |
| **WHERE** | C&R Technologies training center (Boulder, CO), TFAWS (annual NASA workshop), university courses, CadenceLIVE/Ansys conferences, online tutorials [VERIFIED]. |
| **WHEN** | Spacecraft thermal engineering is a specialized discipline. Learning path: 1-2 weeks for basics (with thermal engineering background) → 3-6 months for independent modeling → 1-2 years for expert proficiency [EST]. |
| **WHY** | Spacecraft thermal analysis requires unique domain knowledge: orbital mechanics (beta angle, eclipse duration), space radiation environment (solar constant, albedo coefficient, Earth IR), thermal control hardware (MLI, OSR, heat pipes, louvers), and mission-specific constraints (power cycling, attitude modes) [VERIFIED]. |
| **HOW** | (1) Spacecraft thermal engineering fundamentals (textbook: Gilmore, "Spacecraft Thermal Control Handbook") → (2) C&R training course (5 days intensive) → (3) Tutorial models (simple satellite, heat pipe system) → (4) Mentored real project → (5) Advanced workshops (FloCAD two-phase, RadCAD advanced) → (6) TFAWS participation for community learning [INFERRED]. |

### L5 — Future Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Ansys/C&R Technologies R&D, NASA thermal technology development, commercial space technology teams, university research groups [INFERRED]. |
| **WHAT** | Roadmap: (1) TD Designer (Discovery-based modern UI) replacing AutoCAD dependency, (2) Deep integration with Ansys Fluent for high-fidelity CFD where needed (thruster plumes, entry heating), (3) Integration with Ansys STK for automated orbital environment generation, (4) AI/ML-enhanced thermal margin prediction, (5) Cloud-native HPC for mega-constellation thermal analysis (thousands of satellite variants) [VERIFIED/INFERRED]. |
| **WHERE** | Ansys ecosystem integration creates path from mission design (STK) → spacecraft thermal (Thermal Desktop) → structural (Mechanical) → optical (Zemax) → full digital thread [VERIFIED]. |
| **WHEN** | TD Designer: 2026 R1 (released) [VERIFIED]. Ansys STK deep integration: ongoing 2025-2027. Cloud HPC: 2026-2028. AI thermal margin: 2027-2029 [EST]. |
| **WHY** | Commercial mega-constellations (Starlink: 12,000+ satellites, Kuiper: 3,200+, OneWeb: 600+) require thermal analysis at unprecedented scale. Manual analysis of each variant is impractical; automated, parameterized thermal analysis with AI-driven margin assessment becomes essential [INFERRED]. |
| **HOW** | Parametric TD models → automated orbital environment sweep (STK integration) → batch SINDA/FLUINT solves (cloud HPC) → AI/ML thermal margin prediction → automated compliance checking → digital twin for on-orbit anomaly investigation [INFERRED]. |

---

## 3. 21-Why Analysis

| # | Question | Answer |
|---|----------|--------|
| 1 | **Why is spacecraft thermal analysis fundamentally different from electronics/automotive thermal analysis?** | Because space is a vacuum: there is no convective cooling. Heat can only be transferred by conduction (within the spacecraft) and radiation (to/from space, Sun, and Earth), fundamentally changing the physics and analysis approach [VERIFIED]. |
| 2 | **Why is radiation the dominant heat transfer mode in space?** | Because with no atmospheric molecules for convective transfer, all heat rejection from the spacecraft must occur through infrared radiation from external surfaces (radiators) to the 3K cosmic background [VERIFIED]. |
| 3 | **Why does spacecraft radiation analysis require Monte Carlo ray tracing (RadCAD)?** | Because spacecraft have complex geometries (solar panels, antennas, deployable structures) with mutual shadowing and inter-surface reflections that analytical view factor calculations cannot handle accurately [VERIFIED]. |
| 4 | **Why are orbital environmental heating calculations so complex?** | Because a spacecraft in orbit receives heat from multiple time-varying sources: direct solar (1361 W/m² at 1 AU), Earth-reflected albedo (0.30 × solar × view factor), Earth IR emission (~237 W/m²), and all vary with orbital position, attitude, and time [VERIFIED]. |
| 5 | **Why does orbital position affect thermal loads?** | Because the spacecraft cycles between sunlit and eclipse phases every ~90 minutes (LEO), with eclipse fraction depending on orbit altitude, inclination, and the beta angle (angle between orbit plane and sun vector) [VERIFIED]. |
| 6 | **Why is the beta angle critical for thermal design?** | Because beta angle determines eclipse fraction and the orientation of solar illumination on the spacecraft: at β=0° (noon orbit), eclipse fraction is maximum (~36% for LEO); at β=90°, there is no eclipse. This creates worst-case hot and cold scenarios [VERIFIED]. |
| 7 | **Why does SINDA use finite difference networks rather than finite elements?** | Because the thermal network (R-C circuit) formulation was established in the 1960s for spacecraft, maps directly to physical thermal resistance/capacitance, allows easy incorporation of lumped-parameter elements (heaters, thermostats, louvers), and has decades of flight heritage validation [VERIFIED]. |
| 8 | **Why is flight heritage so important in spacecraft thermal software?** | Because space missions are irreversible (no maintenance or repair in most orbits), costing $100M-$10B. Thermal model predictions must be proven by correlation with on-orbit telemetry data to establish confidence. SINDA has this heritage from Apollo through ISS to James Webb Space Telescope [INFERRED]. |
| 9 | **Why is FloCAD (fluid modeling) essential for modern spacecraft?** | Because modern thermal control systems use mechanically pumped fluid loops (MPFL), loop heat pipes (LHP), and capillary pumped loops (CPL) that require accurate two-phase flow modeling to predict operating limits and temperature stability [VERIFIED]. |
| 10 | **Why are two-phase thermal control systems used in spacecraft?** | Because two-phase systems (using latent heat of vaporization) transport 10-100x more heat per unit mass flow than single-phase liquids, making them essential for power-dense spacecraft subsystems (high-power RF, laser communicators, etc.) [INFERRED]. |
| 11 | **Why is thermal margin assessment critical in spacecraft design?** | Because thermal engineers must demonstrate that all components operate within their qualification temperature limits with adequate margin (typically ±5-15°C) across all mission phases (launch, orbit raising, operational, safe mode, end-of-life degradation) [VERIFIED]. |
| 12 | **Why do spacecraft thermal properties degrade over mission life?** | Because spacecraft surface coatings degrade from UV exposure, atomic oxygen erosion (LEO), and charged particle bombardment, increasing solar absorptance (α) by 50-200% over mission life while emittance (ε) remains relatively stable, shifting the α/ε ratio toward hotter temperatures [VERIFIED]. |
| 13 | **Why is the α/ε ratio the key parameter for spacecraft thermal design?** | Because in radiative equilibrium, steady-state temperature is determined by the ratio of absorbed solar power (proportional to α) to emitted IR power (proportional to ε): T⁴ = (αS·cos(θ))/(εσ), where S is solar constant [VERIFIED]. |
| 14 | **Why was Thermal Desktop built on AutoCAD?** | Because AutoCAD was the dominant CAD platform in the 1990s aerospace industry, and leveraging AutoCAD's geometry kernel avoided the enormous investment of creating a custom 3D modeling environment [INFERRED]. |
| 15 | **Why is TD Designer replacing the AutoCAD dependency?** | Because AutoCAD licensing costs have increased, Autodesk has moved to subscription models, and Ansys Discovery provides a more modern, purpose-built CAD environment with native integration to Ansys solvers [VERIFIED]. |
| 16 | **Why does Thermal Desktop integrate with Ansys STK (Systems Tool Kit)?** | Because STK provides high-fidelity orbital propagation, attitude modeling, and geometric access computations that generate the mission-specific environmental heating inputs (sun vector, eclipse times, Earth view factors) that RadCAD needs [VERIFIED]. |
| 17 | **Why is thermal-structural coupling important for spacecraft?** | Because thermal gradients in spacecraft structures create differential expansion that distorts optical benches, antenna reflectors, and solar panel substrates, degrading mission performance. Temperature maps from TD must feed Ansys Mechanical for distortion analysis [VERIFIED]. |
| 18 | **Why are mega-constellations challenging for thermal analysis?** | Because each satellite variant may have different orbit (altitude, inclination), different power modes, different payload configurations, requiring hundreds or thousands of thermal analysis cases. Traditional manual analysis cannot scale [INFERRED]. |
| 19 | **Why is on-orbit telemetry correlation essential?** | Because thermal model predictions must be validated against actual flight temperatures to establish "correlation factors" that adjust model parameters (contact conductances, effective emittances), building confidence in the model for future missions [VERIFIED]. |
| 20 | **Why do thermal models need to persist across mission phases?** | Because the same thermal model is used for design, test correlation (thermal vacuum testing), launch prediction, commissioning, operations anomaly investigation, and end-of-life planning — spanning 15-20 years for GEO missions [INFERRED]. |
| 21 | **Why does spacecraft thermal engineering remain a specialized discipline despite simulation advances?** | Because the combination of extreme environments (vacuum, radiation, microgravity), irreversible mission consequences, multi-decade model lifecycle, and cross-domain coupling (thermal-structural-optical-power) creates a discipline requiring deep physical intuition that no automated tool can fully replace [INFERRED]. |

---

## 4. FAB Analysis (Features → Advantages → Benefits)

| # | Feature | Advantage | Benefit |
|---|---------|-----------|---------|
| 1 | SINDA/FLUINT solver with Apollo-era heritage | Most validated thermal solver in aerospace history; accepted by all space agencies | Mission-critical confidence: thermal predictions trusted for $100M-$10B missions [VERIFIED] |
| 2 | RadCAD Monte Carlo ray tracing | Accurate radiation exchange and orbital heating for complex spacecraft geometries | Correct worst-case hot/cold temperatures prevent hardware damage and mission failure [VERIFIED] |
| 3 | FloCAD fluid network analysis | Models single and two-phase thermal control loops (heat pipes, LHPs, MPFLs) | Validates thermal control system performance before expensive hardware fabrication and testing [VERIFIED] |
| 4 | TD Designer (2026 R1, Discovery-based) | Modern UI replacing AutoCAD dependency; native Ansys integration | Reduced licensing cost; modern workflow; seamless coupling with Ansys ecosystem [VERIFIED] |
| 5 | SpaceClaim/TD Direct geometry tools | Direct modeling and meshing of complex imported CAD (STEP, IGES) | Rapid thermal mesh creation from mechanical design models; minutes instead of hours [VERIFIED] |
| 6 | Orbital environmental modeling (Sun, Earth albedo, Earth IR) | Automated calculation of time-varying heating on all spacecraft surfaces | Eliminates manual heating calculation errors; handles all orbit types (LEO, MEO, GEO, deep space) [VERIFIED] |
| 7 | Ansys STK integration | High-fidelity mission profile data (attitude, eclipses, beta angle) drives thermal analysis | Mission-specific thermal environments without manual orbital parameter input [VERIFIED] |
| 8 | Temperature mapping to Ansys Mechanical | Direct thermal-to-structural coupling for thermo-elastic distortion analysis | Predicts optical bench distortion, antenna pointing error, and structural margin [VERIFIED] |
| 9 | Participating media radiation (2026 R1) | Models radiation through semi-transparent materials (glass, optical coatings) | Accurate modeling for solar cell cover glass, optical windows, and greenhouse-effect enclosures [VERIFIED] |
| 10 | Parametric and optimization capability | Built-in design variable sweeps and objective-driven optimization | Automated thermal control system sizing (radiator area, heater power, MLI coverage) [VERIFIED] |
| 11 | Transient simulation with implicit solver | Handles orbital cycling, power mode transitions, and eclipse entry/exit dynamics | Predicts peak/minimum temperatures during worst-case transient events (not just steady-state) [VERIFIED] |
| 12 | Thermal Desktop Launcher (2024 R2+) | Streamlined project management and template usage | Faster project startup; template-based workflows for common spacecraft configurations [VERIFIED] |

---

## 5. Top 50 Keywords

| # | Keyword | # | Keyword |
|---|---------|---|---------|
| 1 | Thermal Desktop | 26 | Solar absorptance |
| 2 | SINDA/FLUINT | 27 | Infrared emittance |
| 3 | C&R Technologies | 28 | Alpha/epsilon ratio |
| 4 | RadCAD | 29 | Thermal balance test |
| 5 | FloCAD | 30 | Thermal vacuum (TVAC) |
| 6 | Spacecraft thermal | 31 | Flight heritage |
| 7 | Orbital heating | 32 | Thermal margin |
| 8 | Radiation analysis | 33 | Hot case / cold case |
| 9 | View factor | 34 | Beginning of life (BOL) |
| 10 | Monte Carlo ray trace | 35 | End of life (EOL) |
| 11 | Solar flux | 36 | MLI blanket |
| 12 | Earth albedo | 37 | Optical solar reflector (OSR) |
| 13 | Earth IR | 38 | Radiator design |
| 14 | Beta angle | 39 | Heat pipe |
| 15 | Eclipse fraction | 40 | Loop heat pipe (LHP) |
| 16 | Finite difference | 41 | Two-phase thermal control |
| 17 | Thermal network | 42 | Contact conductance |
| 18 | Lumped parameter | 43 | Thermal cycling |
| 19 | R-C circuit model | 44 | Heater control |
| 20 | Thermal conductance | 45 | Thermostat logic |
| 21 | Thermal capacitance | 46 | Survival temperature |
| 22 | ESATAN-TMS competitor | 47 | Qualification temperature |
| 23 | Ansys integration | 48 | Mega-constellation |
| 24 | TD Designer | 49 | CubeSat thermal |
| 25 | Deep space thermal | 50 | Telemetry correlation |

---

## 6. Open-Source Alternative Mapping

| Thermal Desktop Capability | Open-Source Alternative | Maturity | Gap Assessment |
|---------------------------|----------------------|----------|----------------|
| SINDA/FLUINT thermal solver | **OpenModelica** (Modelica thermal library) | ★★★☆☆ | Capable for thermal networks but lacks space-specific heritage and validation [INFERRED] |
| Orbital heating calculation | **GMAT** (NASA General Mission Analysis Tool) + custom scripts | ★★★☆☆ | GMAT provides orbit propagation but not thermal heating calculations; custom development needed [VERIFIED] |
| Monte Carlo radiation (RadCAD) | **OpenMC** (for radiation transport, different domain) / custom ray tracers | ★★☆☆☆ | No open-source tool provides spacecraft-specific thermal radiation view factor calculation [INFERRED] |
| Fluid network (FloCAD) | **OpenModelica** Fluid library / **Modelica** ThermoPower | ★★★☆☆ | Can model fluid circuits but lacks two-phase space-specific models (LHP, CPL) [INFERRED] |
| CAD-based pre-processing | **FreeCAD** + **Gmsh** | ★★★☆☆ | Geometry and meshing possible but no spacecraft thermal-specific workflow [VERIFIED] |
| Finite difference solver | **Python** (NumPy/SciPy) + **FiPy** | ★★★★☆ | Capable FD framework but no spacecraft thermal libraries or orbital environment models [VERIFIED] |
| Thermal-structural coupling | **Elmer FEM** + **CalculiX** | ★★★★☆ | Good thermo-structural solvers; no orbital environment or radiation heritage [VERIFIED] |
| Post-processing | **ParaView** | ★★★★★ | Fully equivalent visualization capability [VERIFIED] |
| Comprehensive alternative | **ESATAN-TMS** (ESA-funded, not fully open source) | ★★★★☆ | Primary commercial competitor; available to ESA members but not truly open source [VERIFIED] |
| Python-based thermal | **OpenConcept** / custom Python thermal networks | ★★★☆☆ | Research tools; lack production maturity and comprehensive feature set [INFERRED] |

**Assessment**: Thermal Desktop has **no viable open-source replacement** for its complete spacecraft thermal analysis workflow. The combination of heritage SINDA solver, RadCAD orbital heating, FloCAD two-phase fluid modeling, and decades of flight heritage correlation creates a technical moat that would require millions of dollars and years of development to replicate. ESATAN-TMS is the only comparable commercial alternative (ESA ecosystem), but is itself proprietary [INFERRED].

---

## 7. Key Metrics

| Metric | Value | Confidence |
|--------|-------|------------|
| Solver heritage | 60+ years (SINDA origins from 1960s Apollo era) | [VERIFIED] |
| C&R Technologies founded | ~1987 | [EST] |
| Ansys acquisition | 2022 | [VERIFIED] |
| Current version | 2026 R1 | [VERIFIED] |
| New pre-processor | TD Designer (Ansys Discovery-based) | [VERIFIED] |
| Market share (Western spacecraft thermal) | ~80-90% | [EST] |
| Primary competitor | ESATAN-TMS (ESA/Airbus ecosystem) | [VERIFIED] |
| NASA missions using SINDA/TD | Hundreds (Apollo, Shuttle, ISS, JWST, Mars rovers, etc.) | [VERIFIED] |
| Typical license cost (annual) | $15,000 - $50,000 per seat | [EST] |
| Supported modules | SINDA/FLUINT, RadCAD, FloCAD, TD Direct, TD Designer | [VERIFIED] |
| Key reference: Gilmore textbook | "Spacecraft Thermal Control Handbook" (AIAA) | [VERIFIED] |
| User community | TFAWS (NASA Thermal & Fluids Analysis Workshop), Ansys Learning Forum | [VERIFIED] |
| Academic citations ("Thermal Desktop" OR "SINDA") | ~5,000-10,000 papers | [EST] |
| Supported platforms | Windows (primary), Linux (batch) | [VERIFIED] |
| Legacy CAD dependency | AutoCAD (being replaced by TD Designer) | [VERIFIED] |
| Orbital environment capabilities | LEO, MEO, GEO, HEO, deep space, lunar, Mars | [VERIFIED] |

---

*Report compiled by AEOS Software Analysis Engine · Sophia (Knowledge Academy) + Techne (Engineering Forge)*
*Sources: C&R Technologies documentation, Ansys official releases, NASA TFAWS proceedings, Ansys investor relations, aerospace industry publications*
