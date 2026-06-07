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

---

## 🎯 What is OpenFlow3D?

OpenFlow3D is an **open-source, browser-based CAE (Computer-Aided Engineering) educational platform** for injection molding simulation. It demonstrates the complete simulation pipeline — from CAD geometry import to Digital Twin calibration — using modern web technologies.

> **Mission**: Democratize injection molding CAE knowledge through interactive, web-based learning.

## ✨ Key Features

### 🏭 12-Stage Professional Workflow
Complete injection molding pipeline covering:
1. **CAD Geometry Import** — STEP/IGES B-Rep parsing
2. **Runner & Gate Design** — Sprue/runner/gate placement
3. **Wasm BLM Mesh Generation** — Gmsh WebAssembly meshing
4. **Mesh Quality Inspection** — Jacobian/skewness validation
5. **Material Database (Cross-WLF)** — Polymer viscosity modeling
6. **Machine & Process Setup** — Injection parameters
7. **PINN Physics Training** — Neural network PDE constraints
8. **Melt Filling Analysis** — 3D flow front simulation
9. **Packing & Holding Pressure** — Tait PVT compensation
10. **Cooling Channel Analysis** — Conformal cooling optimization
11. **Warpage & Shrinkage** — Residual stress prediction
12. **Digital Twin Calibration** — iMolding sensor-sim alignment

### 📖 3 Critical Educational Features
| Feature | Description |
|---|---|
| **Knowledge Cards** | 12 expandable cards with Bloom's Taxonomy levels (L1→L6) and PBL challenges |
| **Live Formula Dashboard** | 5 governing equations (Cross-WLF, Tait PVT, Fourier, PINN Loss, LM Solver) with real-time parameter binding |
| **Tutorial Mode** | 7-step guided walkthrough with physics explanations |

### 🎨 3D Visualization
- **Three.js r160 WebGL** rendering with PBR materials
- **Real-time 3D model** of injection mold (ExtrudeGeometry + clearcoat)
- **Particle flow system** with temperature-based HSL coloring
- **Mouse orbit/zoom** interaction
- **Stage-specific visual effects** (emissive pulse, color transitions, flow particles)

## 🚀 Quick Start

### Option 1: Direct Browser (Zero Install)
```bash
# Just open the HTML file in any modern browser
open igs_openflow3d_interactive_dashboard_20260607_v03.html
```

### Option 2: Local Server
```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

Then navigate to `http://localhost:8000/igs_openflow3d_interactive_dashboard_20260607_v03.html`

## 📁 Project Structure

```
NCTU-Zack/
├── igs_openflow3d_interactive_dashboard_20260607_v03.html  ← 🌟 Main Dashboard (V3)
├── igs_openflow3d_interactive_dashboard_20260607_v02.html  ← V2 (Three.js upgrade)
├── igs_openflow3d_interactive_dashboard_20260607_v01.html  ← V1 (Canvas 2D original)
├── igs_openflow3d_pinn_melt_front_lab_20260607_v01.py      ← PINN training lab
├── openflow3d/                                              ← Backend monorepo
│   ├── server/                                              ← FastAPI backend
│   ├── solver/                                              ← Physics modules
│   │   ├── rheology/crosswlf.py                             ← Cross-WLF viscosity
│   │   └── thermophysical/tait_pvt.py                       ← Tait PVT EOS
│   ├── docker-compose.yml                                   ← Docker orchestration
│   └── nginx/                                               ← Reverse proxy config
├── notes/ & reports/                                        ← Research documentation
└── README.md                                                ← This file
```

## 🔬 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **3D Rendering** | Three.js r160 (WebGL 2.0) | PBR material rendering, particle systems |
| **Frontend** | Vanilla HTML/CSS/JS | Zero-dependency dashboard |
| **Physics** | Python (PyTorch) | PINN training, Cross-WLF, Tait PVT |
| **Backend** | FastAPI + Docker | Solver API & OpenFOAM orchestration |
| **Meshing** | Gmsh (WebAssembly) | Client-side BLM mesh generation |
| **Design** | Nebula Academy Theme | Glassmorphism, particle backgrounds |

## 📊 Version History

| Version | Date | Key Upgrade |
|---|---|---|
| **v1.0** | 2026-06-07 | Canvas 2D dashboard, 6-stage workflow |
| **v2.0** | 2026-06-07 | Three.js WebGL 3D, particle systems, mouse orbit |
| **v3.0** | 2026-06-07 | 12 stages, Knowledge Cards, Live Formulas, Tutorial Mode |

## 👥 Team

| Creator | Role |
|---|---|
| **iGS Horace** | Founder & Lead Architect — System design, domain expertise, CAE vision |
| **iGS AEOS Team** | AI Engineering — v9.1 AEGIS Edition, 31-expert Septagonal Forge |

## 📄 License

MIT License — Free for educational and commercial use.

---

<p align="center">
  <strong>Built with 🔥 by iGS & AEOS</strong><br>
  <em>OpenFlow3D — Making CAE Knowledge Accessible to Everyone</em>
</p>
