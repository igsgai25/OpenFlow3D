# 🌌 OpenFlow3D — Open-Source Web-CAE Educational Platform

<p align="center">
  <strong>Next-Gen 3D Injection Molding Simulation & Digital Twin Engine</strong><br>
  <em>Built with Three.js WebGL | PINN Physics Engine | 12-Stage Professional Workflow</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v3.0-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/engine-Three.js_r160-green?style=flat-square" alt="Three.js">
  <img src="https://img.shields.io/badge/license-MIT-orange?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/stages-12-purple?style=flat-square" alt="Stages">
</p>

<p align="center">
  <a href="https://igsgai25.github.io/OpenFlow3D/igs_openflow3d_interactive_dashboard_20260607_v03.html"><strong>🚀 Launch Live Demo →</strong></a>
</p>

---

## 🎯 What is OpenFlow3D?

OpenFlow3D is an **open-source, browser-based CAE (Computer-Aided Engineering) educational platform** for injection molding simulation. It demonstrates the complete simulation pipeline — from CAD geometry import to Digital Twin calibration — using modern web technologies.

> **Mission**: Democratize injection molding CAE knowledge through interactive, web-based learning.

### ▶️ Live Demo

**[🚀 Click here to launch the interactive 3D dashboard](https://igsgai25.github.io/OpenFlow3D/igs_openflow3d_interactive_dashboard_20260607_v03.html)**

Experience the full 12-stage injection molding workflow with 3D visualization, real-time physics equations, and guided tutorials — all running in your browser with zero installation.

---

## ✨ Top 3 Educational Features

### 📖 1. Knowledge Cards — [Learn More](docs/igs_moldex3d_core_simulation_solver_report_20260607_v01.md)

Each of the 12 stages has a dedicated **expandable knowledge card** containing:

| Component | Description |
|---|---|
| **Concept Explanation** | 2-3 sentence technical overview of the engineering principle |
| **Governing Equation** | Key formula rendered in monospace (Cross-WLF, Tait PVT, Fourier, etc.) |
| **Bloom's Taxonomy Level** | Cognitive level indicator: L1 Remember → L6 Create |
| **PBL Challenge** | Problem-Based Learning question to test understanding |

> Covers Bloom's Taxonomy from **L1 (Remember)** through **L6 (Create)** across all 12 stages, ensuring progressive cognitive development.

### 📊 2. Live Formula Dashboard — [Learn More](docs/igs_moldex3d_studio_5w1h_21why_report_20260607_v01.md)

A real-time equation panel showing **5 governing equations** that highlight dynamically based on the active stage:

| # | Formula | Equation | Active Stages |
|---|---|---|---|
| 1 | **Cross-WLF** | `η = η₀ / [1 + (η₀·γ̇/τ*)^(1-n)]` | S05, S06, S07, S08, S12 |
| 2 | **Tait PVT** | `v = v₀·[1 - C·ln(1 + p/B(T))]` | S05, S09, S11 |
| 3 | **Fourier Energy** | `ρCp·∂T/∂t = k·∇²T + η·γ̇²` | S08, S09, S10 |
| 4 | **PINN Loss** | `L = L_BC + λ·‖∇²p‖²` | S07 |
| 5 | **LM Solver** | `(JᵀJ + μI)·δp = -Jᵀr` | S12 |

> Parameter values update in real-time during PINN training (loss convergence) and Digital Twin calibration (RMSE optimization).

### 🎓 3. Tutorial Mode — [Learn More](docs/igs_moldex3d_killer_web_cae_blueprint_20260607_v01.md)

A **7-step guided walkthrough** activated via the 🎓 button in the header:

| Step | Topic | Key Concept |
|---|---|---|
| 1 | Welcome | Platform overview & learning objectives |
| 2 | Geometry & Runner | CAD B-Rep, Hagen-Poiseuille pressure drop |
| 3 | Meshing & Quality | BLM boundary layers, Jacobian metrics |
| 4 | Material & Process | Cross-WLF viscosity, process window |
| 5 | PINN & Filling | Physics-informed neural networks, melt front |
| 6 | Packing & Cooling | Tait PVT shrinkage, Biot number |
| 7 | Warpage & Digital Twin | Residual stress, Levenberg-Marquardt calibration |

> Features glassmorphism modal, progress dots, highlighted technical terms, and embedded equations.

---

## 🏭 12-Stage Professional Workflow

| Zone | Stage | Title | Description |
|---|---|---|---|
| **Pre-Processing** | S01 | CAD Geometry Import | STEP/IGES B-Rep parsing & validation |
| | S02 | Runner & Gate Design | Sprue, runner, gate placement & sizing |
| | S03 | Wasm BLM Mesh Generation | Gmsh WebAssembly boundary-layer meshing |
| | S04 | Mesh Quality Inspection | Jacobian, aspect ratio & skewness check |
| **Setup** | S05 | Material Database (WLF) | Cross-WLF viscosity & Tait PVT loading |
| | S06 | Machine & Process Setup | Injection pressure, speed & temperature |
| **Simulation** | S07 | PINN Physics Training | Laplace/N-S equation neural pre-training |
| | S08 | Melt Filling Analysis | 3D melt front propagation & weld lines |
| | S09 | Packing & Holding | Post-fill packing pressure & gate seal |
| | S10 | Cooling Channel Analysis | Conformal cooling efficiency & cycle time |
| **Post-Processing** | S11 | Warpage & Shrinkage | Residual stress & part deformation prediction |
| | S12 | Digital Twin Calibration | iMolding sensor-sim curve alignment |

---

## 🔬 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **3D Rendering** | Three.js r160 (WebGL 2.0) | PBR material rendering, particle systems |
| **Frontend** | Vanilla HTML/CSS/JS | Zero-dependency dashboard |
| **Physics** | Python (PyTorch) | PINN training, Cross-WLF, Tait PVT |
| **Backend** | FastAPI + Docker | Solver API & OpenFOAM orchestration |
| **Meshing** | Gmsh (WebAssembly) | Client-side BLM mesh generation |
| **Design** | Nebula Academy Theme | Glassmorphism, particle backgrounds |

## 📁 Project Structure

```
OpenFlow3D/
├── igs_openflow3d_interactive_dashboard_20260607_v03.html  ← 🌟 Main Dashboard (V3)
├── igs_openflow3d_pinn_melt_front_lab_20260607_v01.py      ← PINN training lab
├── docs/                                                    ← Research & analysis reports
│   ├── igs_moldex3d_core_simulation_solver_report.md        ← Solver architecture deep-dive
│   ├── igs_moldex3d_killer_web_cae_blueprint.md             ← Web-CAE system blueprint
│   ├── igs_moldex3d_studio_5w1h_21why_report.md             ← 5W1H & 21-Why analysis
│   ├── igs_moldex3d_twenty_one_why_analysis.md               ← 21-Why deep analysis
│   ├── igs_moldex3d_top_three_competitors_report.md          ← Market competitor analysis
│   └── ...                                                  ← Additional reports
├── openflow3d/                                              ← Backend monorepo
│   ├── server/                                              ← FastAPI backend
│   ├── solver/                                              ← Physics modules
│   │   ├── rheology/crosswlf.py                             ← Cross-WLF viscosity
│   │   └── thermophysical/tait_pvt.py                       ← Tait PVT EOS
│   └── docker-compose.yml                                   ← Docker orchestration
├── flow-3d-papers-docs/                                     ← Literature & papers
├── LICENSE                                                  ← MIT License
└── README.md                                                ← This file
```

## 🚀 Quick Start

### Option 1: Live Demo (Zero Install)
**[Launch Dashboard →](https://igsgai25.github.io/OpenFlow3D/igs_openflow3d_interactive_dashboard_20260607_v03.html)**

### Option 2: Run Locally
```bash
git clone https://github.com/igsgai25/OpenFlow3D.git
cd OpenFlow3D
python -m http.server 8000
# Open http://localhost:8000/igs_openflow3d_interactive_dashboard_20260607_v03.html
```

## 👥 Team

| Creator | Role |
|---|---|
| **iGS Horace** | Founder & Lead Architect — System design, domain expertise, CAE vision |
| **iGS AEOS Team** | AI Engineering — v9.1 AEGIS Edition, 31-expert Septagonal Forge |

## 📄 License

MIT License — Free for educational and commercial use.

---

<p align="center">
  <a href="https://igsgai25.github.io/OpenFlow3D/igs_openflow3d_interactive_dashboard_20260607_v03.html"><strong>🚀 Try the Live Demo Now →</strong></a>
</p>

<p align="center">
  <strong>Built with 🔥 by iGS & AEOS</strong><br>
  <em>OpenFlow3D — Making CAE Knowledge Accessible to Everyone</em>
</p>
