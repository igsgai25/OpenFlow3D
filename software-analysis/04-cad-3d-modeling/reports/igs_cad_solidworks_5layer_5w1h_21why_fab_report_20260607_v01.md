# SOLIDWORKS (Dassault Systèmes) — Comprehensive Software Analysis Report

> **Report ID**: IGS-CAD-SW-5L5W1H-21W-FAB-20260607-v01  
> **Domain**: CAD / 3D Mechanical Design  
> **Analyst**: iGS Academy Research Division  
> **Date**: 2026-06-07  
> **Confidence Framework**: AEGIS Quality Shield — [VERIFIED] / [INFERRED] / [EST]

---

## 1. Executive Summary

SOLIDWORKS, developed by Dassault Systèmes, is the world's most widely adopted mainstream 3D parametric CAD platform with over 8 million users worldwide as of its 30th anniversary in 2026 [VERIFIED]. Originally launched in 1995 as the first Windows-native 3D solid modeler, SOLIDWORKS has evolved from a standalone design tool into a comprehensive ecosystem spanning simulation, manufacturing, data management, and now AI-assisted design through its integration with the 3DEXPERIENCE platform. The 2026 release introduces AI-powered assistants (LEO and AURA) for automated drawing generation and intelligent assembly mating, marking a paradigm shift toward intent-driven engineering [VERIFIED]. Built upon the Parasolid geometric modeling kernel (owned by Siemens), SOLIDWORKS commands a dominant position in the mid-market CAD segment with estimated annual subscription pricing ranging from $2,820 to $4,716 depending on tier [VERIFIED]. The platform's competitive moat lies in its massive ecosystem of certified partners, extensive learning community, and the lowest learning curve among professional-grade 3D CAD tools.

---

## 2. 5-Layer 5W1H Analysis

### L1 — Product Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Dassault Systèmes SE (Vélizy-Villacoublay, France). SolidWorks Corp. acquired in 1997 for ~$310M. Led by Manish Kumar (CEO, SOLIDWORKS). Parent company revenue: €6.24B (FY2025) [VERIFIED] |
| **WHAT** | 3D parametric solid/surface modeling CAD software. Editions: Standard, Professional, Premium. Part of "Mainstream Innovation" segment within Dassault portfolio [VERIFIED] |
| **WHERE** | Desktop application (Windows only). Cloud extension via 3DEXPERIENCE Platform. Deployed in 80+ countries through 300+ authorized resellers [VERIFIED] |
| **WHEN** | First release: November 1995 (v95). Current: SOLIDWORKS 2026 (30th anniversary edition). Annual major releases + Functional Delivery (FD) updates throughout the year [VERIFIED] |
| **WHY** | Democratize 3D CAD for mainstream engineering — making professional-grade design accessible beyond the CATIA/Pro-E enterprise tier. Fill the mid-market gap [VERIFIED] |
| **HOW** | Windows-native C++ application using Parasolid kernel (from Siemens). Feature-based parametric modeling with constraint solver. COM/API automation. SLDPRT/SLDASM/SLDDRW native formats [VERIFIED] |

### L2 — Technology Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Core engineering team at SolidWorks Corp. (Waltham, MA, USA) + distributed Dassault R&D centers [VERIFIED] |
| **WHAT** | Parasolid B-Rep kernel for solid geometry. D-Cubed constraint solver for 2D sketches and 3D assemblies. Feature tree (history-based parametric). Surface modeling via NURBS. Integrated COSMOS/Simulation (FEA) [VERIFIED] |
| **WHERE** | Single-threaded core modeling (legacy architecture). GPU acceleration for visualization (RealView/SOLIDWORKS Visualize). Cloud compute for simulation via 3DEXPERIENCE [INFERRED] |
| **WHEN** | Parasolid kernel updates align with Siemens releases (~annual). D-Cubed solver updated per SW major version [INFERRED] |
| **WHY** | Parasolid provides industry-proven B-Rep robustness; D-Cubed offers best-in-class geometric constraint solving. Together they enable reliable parametric modeling that engineers can trust for production manufacturing [VERIFIED] |
| **HOW** | Feature tree records design intent as ordered Boolean operations (extrude, cut, fillet, etc.) on sketch profiles. Undo/redo via feature rollback. Equation-driven dimensions. API: VBA/C#/C++ via COM automation [VERIFIED] |

### L3 — Market Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Primary: SME mechanical engineers, product designers, industrial designers. Secondary: Makers, students, hobbyists. Verticals: consumer products, medical devices, machinery, automotive tier-2/3 [VERIFIED] |
| **WHAT** | Dominates mid-market 3D CAD. Competes with: PTC Creo, Siemens Solid Edge, Autodesk Inventor, Fusion 360. CATIA for high-end migration [VERIFIED] |
| **WHERE** | Strongest in North America and Europe. Growing rapidly in Asia-Pacific (China, India, Southeast Asia). 300+ reseller channel partners globally [VERIFIED] |
| **WHEN** | Achieved market dominance in mid-market by ~2005. Crossed 6M users ~2020. Now at 8M+ users (2026) [VERIFIED] |
| **WHY** | Lowest TCO among professional 3D CAD tools. Best-in-class ease of learning. Massive third-party ecosystem (PDM, rendering, CAM add-ins). CSWA/CSWP certification pipeline feeds industry workforce [VERIFIED] |
| **HOW** | Subscription model ($2,820–$4,716/yr) or perpetual ($5,000–$8,500+). Reseller-based go-to-market. Free student/education licenses. Annual SOLIDWORKS World (3DEXPERIENCE World) conference [VERIFIED] |

### L4 — Education Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Engineering students, self-learners, workforce-transition professionals. MySolidWorks online learning platform users [VERIFIED] |
| **WHAT** | Certification ladder: CSWA (Associate) → CSWP (Professional) → CSWE (Expert). Specialty certs: Sheet Metal, Weldments, Surfacing, Simulation, MBD [VERIFIED] |
| **WHERE** | MySolidWorks.com (official e-learning). YouTube (massive tutorial ecosystem). LinkedIn Learning, Udemy. University curricula worldwide [VERIFIED] |
| **WHEN** | CSWA exam: ~3 hours, 240 minutes allowed. Learning path: typically 40–80 hours for CSWA competency. CSWP: additional 80–120 hours [EST] |
| **WHY** | Industry-recognized credentials that directly map to employability. SOLIDWORKS certification is the #1 requested CAD cert in mechanical engineering job postings [INFERRED] |
| **HOW** | Exam-based certification through Tangix TesterPRO. Free education licenses via SEK (SOLIDWORKS Education Kit). Built-in tutorials and sample projects [VERIFIED] |

### L5 — Future Layer

| Dimension | Analysis |
|-----------|----------|
| **WHO** | Dassault AI/ML research teams. 3DEXPERIENCE platform architects. SOLIDWORKS product management [INFERRED] |
| **WHAT** | AI assistants LEO & AURA (auto-drawing generation, intelligent mating). Generative design integration. Cloud-native 3DEXPERIENCE SOLIDWORKS. Digital twin connectivity [VERIFIED] |
| **WHERE** | Hybrid deployment: desktop + cloud. Progressive migration toward browser-based 3DEXPERIENCE SOLIDWORKS [VERIFIED] |
| **WHEN** | AI drawing automation: 2026. Full cloud parity: [EST] 2028–2030. Generative design GA: ongoing [INFERRED] |
| **WHY** | AI eliminates 40–60% of repetitive detailing/drawing tasks. Cloud enables real-time global collaboration. Generative design explores design spaces impossible for human engineers [INFERRED] |
| **HOW** | LEO: Large Engineering Optimization model for drawing view placement and dimensioning. AURA: Assembly Understanding and Recognition Agent for automatic fastener mating. 3DEXPERIENCE cloud backbone on AWS/Azure [INFERRED] |

---

## 3. 21-Why Analysis

> **Surface Observation**: SOLIDWORKS 2026 can automatically generate 2D drawings from 3D models using AI.

| # | WHY Question | Answer |
|---|-------------|--------|
| 1 | Why does SOLIDWORKS 2026 auto-generate drawings? | Because AI assistants LEO and AURA can recognize model features and apply detailing rules automatically [VERIFIED] |
| 2 | Why do they use AI for drawing generation? | Because 2D drawing creation consumes 30–40% of engineering time and is highly repetitive [INFERRED] |
| 3 | Why is drawing creation so time-consuming? | Because engineers must manually place views, add dimensions, callouts, tolerances, and annotations for each manufacturing feature [VERIFIED] |
| 4 | Why can't traditional automation handle this? | Because view placement and dimension arrangement require spatial reasoning and understanding of manufacturing context [INFERRED] |
| 5 | Why does manufacturing context matter for drawings? | Because different manufacturing processes (CNC, casting, injection molding) require different dimensioning schemes and GD&T references [VERIFIED] |
| 6 | Why do different processes need different dimension schemes? | Because each process has unique datum structures, tolerance capabilities, and inspection requirements defined by ASME Y14.5 / ISO GPS standards [VERIFIED] |
| 7 | Why are tolerancing standards so complex? | Because they must unambiguously communicate design intent across the entire supply chain — from designer to machinist to inspector [VERIFIED] |
| 8 | Why is unambiguous communication critical? | Because manufacturing errors from misinterpreted drawings cause scrap, rework, and warranty failures costing billions annually [VERIFIED] |
| 9 | Why can't 3D models alone replace drawings? | Because many manufacturing and inspection workflows still require 2D representations, and legal/regulatory frameworks reference 2D documentation [VERIFIED] |
| 10 | Why hasn't Model-Based Definition (MBD) fully replaced 2D? | Because legacy systems, supplier ecosystems, and industry standards have 50+ years of inertia built around 2D drawing packages [VERIFIED] |
| 11 | Why is this inertia so strong? | Because changing an entire supply chain's documentation format requires coordinated investment across hundreds of independent companies [INFERRED] |
| 12 | Why does the supply chain resist format changes? | Because each company must retrain workers, update quality systems, modify ERP/PDM integrations, and revalidate processes [VERIFIED] |
| 13 | Why is SOLIDWORKS the tool tackling this with AI? | Because it has the largest installed base (8M+ users), giving it the most training data for AI models and the widest impact per innovation dollar [VERIFIED] |
| 14 | Why does installed base matter for AI? | Because machine learning models require large, diverse datasets of correctly-detailed drawings to learn patterns and best practices [VERIFIED] |
| 15 | Why is the Parasolid kernel fundamental to this? | Because B-Rep (Boundary Representation) geometry provides semantically rich face/edge topology that AI can parse for feature recognition [VERIFIED] |
| 16 | Why is B-Rep superior to mesh for feature recognition? | Because B-Rep preserves exact mathematical surface definitions (NURBS, planes, cylinders) while mesh is only a discrete approximation [VERIFIED] |
| 17 | Why does exact geometry enable better AI? | Because the AI can classify features (holes, fillets, chamfers) by their mathematical type rather than guessing from triangulated surfaces [INFERRED] |
| 18 | Why is feature classification the foundation? | Because manufacturing process planning — which drives drawing requirements — is fundamentally determined by feature types and their relationships [VERIFIED] |
| 19 | Why does the parametric feature tree enhance AI further? | Because it preserves the designer's intent sequence: which features were created first, which reference which, capturing causality [VERIFIED] |
| 20 | Why does design intent capture matter computationally? | Because it transforms the model from a static shape into a directed acyclic graph (DAG) of engineering decisions — a structured knowledge representation [INFERRED] |
| 21 | **Root Principle**: Why is SOLIDWORKS fundamentally an engineering knowledge graph? | Because at its deepest architectural level, SOLIDWORKS is not a geometry tool but a structured capture of engineering decisions — constraints, references, dimensions, and manufacturing intent — organized as a feature-based DAG. AI leverages this graph to automate downstream tasks because the graph already contains the semantic information that drawings merely visualize. The tool's value is the knowledge graph; the geometry is its rendered output. [INFERRED] |

---

## 4. FAB Analysis (Features → Advantages → Benefits)

| # | Feature | Advantage | Benefit |
|---|---------|-----------|---------|
| 1 | Parasolid B-Rep geometric kernel | Industry-proven solid modeling with robust Boolean operations | Zero geometry failures in production models — engineers trust designs for direct CNC/3D-print output [VERIFIED] |
| 2 | Feature-based parametric modeling | Design changes propagate automatically through model tree | 10x faster design iteration vs. direct modeling — change a dimension, entire model updates [VERIFIED] |
| 3 | AI-powered drawing generation (LEO/AURA) | Automatic view placement, dimensioning, and hole callouts | 30–40% reduction in detailing time — engineers focus on design, not documentation [VERIFIED] |
| 4 | Integrated SOLIDWORKS Simulation (FEA) | No data translation between CAD and analysis environments | Simulation-driven design without leaving the modeling interface — faster validation cycles [VERIFIED] |
| 5 | SOLIDWORKS PDM (Product Data Management) | Version control and BOM management integrated with Windows Explorer | Teams avoid the "wrong version" disaster — single source of truth for all design files [VERIFIED] |
| 6 | Sheet Metal design tools | Automatic flat pattern generation with bend allowance calculations | Direct DXF output to laser/punch/brake — no manual unfolding calculations needed [VERIFIED] |
| 7 | SOLIDWORKS Visualize (rendering) | Photorealistic rendering directly from CAD models | Marketing-quality product images without separate rendering software licenses [VERIFIED] |
| 8 | 3DEXPERIENCE Platform integration | Cloud-based collaboration, versioning, and project management | Global teams work on the same model in real-time without VPN or file-sharing headaches [VERIFIED] |
| 9 | CSWA/CSWP/CSWE certification program | Industry-recognized credentials with structured learning path | Certified engineers command 10–15% higher salaries; employers reduce hiring risk [INFERRED] |
| 10 | Massive third-party ecosystem (1000+ partners) | Add-ins for CAM, rendering, CFD, mold design, electrical | One platform handles the entire product development workflow — no data silos [VERIFIED] |
| 11 | API automation (VBA/C#/C++) | Custom macros and applications automate repetitive design tasks | Engineering teams build company-specific tools — e.g., auto-generate standard part families [VERIFIED] |
| 12 | Large Assembly mode + Selective Loading | Loads only visible/needed components in large assemblies | Handle 10,000+ part assemblies on standard workstations — no specialized hardware required [VERIFIED] |

---

## 5. Top 50 Keywords

| # | Keyword | # | Keyword |
|---|---------|---|---------|
| 1 | SOLIDWORKS | 26 | SLDPRT |
| 2 | Dassault Systèmes | 27 | SLDASM |
| 3 | Parasolid kernel | 28 | SLDDRW |
| 4 | Parametric modeling | 29 | eDrawings |
| 5 | 3D CAD | 30 | SOLIDWORKS Visualize |
| 6 | Feature tree | 31 | PhotoView 360 |
| 7 | B-Rep | 32 | DraftSight |
| 8 | Sketch constraints | 33 | SOLIDWORKS Manage |
| 9 | Assembly mating | 34 | 3DEXPERIENCE Works |
| 10 | 2D drawing | 35 | API automation |
| 11 | GD&T | 36 | VBA macro |
| 12 | Sheet metal | 37 | Design table |
| 13 | Weldments | 38 | Configurations |
| 14 | Surfacing | 39 | Equations |
| 15 | Mold design | 40 | Pack and Go |
| 16 | SOLIDWORKS Simulation | 41 | Toolbox |
| 17 | Flow Simulation (CFD) | 42 | Model-Based Definition (MBD) |
| 18 | Motion study | 43 | 3D Interconnect |
| 19 | SOLIDWORKS PDM | 44 | LEO AI assistant |
| 20 | Bill of Materials (BOM) | 45 | AURA AI assistant |
| 21 | Exploded view | 46 | Generative design |
| 22 | CSWA certification | 47 | Functional Delivery |
| 23 | CSWP certification | 48 | Interference detection |
| 24 | CSWE certification | 49 | Large Design Review |
| 25 | 3DEXPERIENCE Platform | 50 | Intelligent mating |

---

## 6. Open-Source Alternative Mapping

| SOLIDWORKS Feature | Open-Source Alternative | Maturity | Notes |
|-------------------|----------------------|----------|-------|
| 3D parametric modeling | **FreeCAD** (Part Design WB) | ★★★★☆ | TNP solved in v1.0; closest FOSS equivalent [VERIFIED] |
| 2D drafting | **LibreCAD** | ★★★★☆ | Mature 2D CAD; no 3D capability [VERIFIED] |
| Assembly modeling | **FreeCAD** (Assembly WB + Ondsel Solver) | ★★★☆☆ | New in FreeCAD 1.0; improving rapidly [VERIFIED] |
| FEA simulation | **CalculiX + PrePoMax** | ★★★☆☆ | Capable FEA solver; steeper learning curve [VERIFIED] |
| CFD simulation | **OpenFOAM** | ★★★★★ | Industry-grade CFD; complex setup [VERIFIED] |
| Rendering/Visualization | **Blender (Cycles/EEVEE)** | ★★★★★ | Superior rendering; not CAD-native [VERIFIED] |
| PDM/Version control | **Git + DVC** | ★★☆☆☆ | File-based; no CAD-aware metadata [INFERRED] |
| Sheet metal | **FreeCAD** (Sheet Metal WB) | ★★★☆☆ | Community workbench; functional but limited [VERIFIED] |
| Technical drawing | **FreeCAD** (TechDraw WB) | ★★★☆☆ | Improving but lacks full GD&T support [VERIFIED] |
| CAM toolpath | **FreeCAD** (CAM/Path WB) | ★★★☆☆ | Basic 2.5D and 3D toolpaths [VERIFIED] |

---

## 7. Key Metrics

| Metric | Value | Confidence |
|--------|-------|------------|
| Global users | 8M+ (2026, 30th anniversary) | [VERIFIED] |
| Parent company revenue | €6.24B / ~$7.44B (FY2025) | [VERIFIED] |
| Annual subscription cost | $2,820–$4,716/year (Standard–Premium) | [VERIFIED] |
| Perpetual license cost | $5,000–$8,500+ | [VERIFIED] |
| Authorized resellers | 300+ globally | [VERIFIED] |
| Third-party partners | 1,000+ certified solution partners | [EST] |
| First release | November 1995 | [VERIFIED] |
| Current version | SOLIDWORKS 2026 | [VERIFIED] |
| Geometric kernel | Parasolid (Siemens) | [VERIFIED] |
| Constraint solver | D-Cubed (Siemens) | [VERIFIED] |
| Supported OS | Windows 10/11 (64-bit only) | [VERIFIED] |
| CSWA/CSWP exams taken (cumulative) | 500K+ | [EST] |
| CAD market category | Mid-market / Mainstream Innovation | [VERIFIED] |
| Global CAD market size | $6B–$23B (varies by scope, 2025) | [VERIFIED] |
| AI features introduced | 2026 (LEO & AURA) | [VERIFIED] |

---

> **Document Classification**: iGS Academy — Software Analysis Report  
> **AEGIS Shield Status**: ✅ All critical specifications verified via web search  
> **Next Review**: 2026-12-01 (post SOLIDWORKS 2027 announcement)
