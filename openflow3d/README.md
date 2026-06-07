# OpenFlow3D 🌊

> **Open-Source Web-Based CAE Platform for Injection Molding Simulation with PINN Acceleration**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11+-green.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://react.dev/)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v12-orange.svg)](https://openfoam.org/)

OpenFlow3D is an open-source, web-based, Python-driven 3D injection molding simulation and digital twin calibration platform. It aims to democratize CAE (Computer-Aided Engineering) for the plastics manufacturing industry.

## 🏗️ Architecture

```
openflow3d/
├── client/                  # React + Vite + Three.js frontend
│   ├── src/
│   │   ├── components/      # UI components (WorkflowStepper, ParamPanel, etc.)
│   │   ├── renderer/        # Three.js 3D rendering engine
│   │   ├── workers/         # Web Workers (Wasm mesh, ONNX inference)
│   │   ├── ai/              # ONNX Runtime Web PINN inference
│   │   ├── hooks/           # React hooks (useProgress, useWebSocket)
│   │   ├── locales/         # i18n language files (zh-TW, en)
│   │   └── styles/          # CSS design system
│   └── public/
├── server/                  # FastAPI + Celery backend
│   ├── api/                 # RESTful API routers
│   ├── ws/                  # WebSocket endpoints
│   ├── tasks/               # Celery async tasks
│   ├── db/                  # PostgreSQL + SQLite models
│   ├── solver_bridge/       # OpenFOAM Docker bridge
│   └── config/              # Environment & logging
├── ai/                      # PyTorch PINN & surrogate models
│   ├── pinn/                # Physics-Informed Neural Networks
│   ├── surrogate/           # DOE + XGBoost surrogate models
│   ├── hpo/                 # Optuna hyperparameter optimization
│   ├── export/              # ONNX model export
│   └── transfer/            # Transfer learning pipelines
├── twin/                    # Digital Twin calibration pipeline
│   ├── filters/             # Savitzky-Golay, noise filtering
│   ├── alignment/           # Keyframe + DTW time alignment
│   ├── calibration/         # LM inverse solver
│   ├── anomaly/             # Z-score anomaly detection
│   ├── recipe/              # EUROMAP 77 recipe generation
│   ├── synthetic/           # Synthetic data generator
│   └── reporting/           # Auto calibration reports
├── iot/                     # Edge IoT data ingestion
│   ├── opcua_bridge.py      # OPC UA → MQTT bridge
│   └── mqtt_ingester.py     # MQTT → InfluxDB writer
├── solver/                  # OpenFOAM solver customizations
│   ├── openInjMoldSim/      # Modified injection molding solver
│   ├── rheology/            # Cross-WLF viscosity model
│   ├── thermophysical/      # Tait PVT equation of state
│   ├── crystallization/     # Dual Nakamura model
│   └── control/             # V/P switch logic
├── wasm/                    # WebAssembly mesh engine
│   ├── bindings.cpp         # Emscripten C++ bindings
│   ├── blm_config.h         # BLM mesh parameters
│   └── mesh_quality.cpp     # Jacobian quality checker
├── tests/                   # Comprehensive test suite
├── e2e/                     # Playwright E2E tests
├── docker/                  # Docker & docker-compose
├── k8s/                     # Kubernetes manifests
├── infra/                   # Terraform IaC
├── labs/                    # 12 Jupyter PBL labs
├── docs/                    # Sphinx API docs + ADRs + User Guide
└── website/                 # Docusaurus project site
```

## 🚀 Quick Start

### Prerequisites
- Node.js 20+ & npm 10+
- Python 3.11+
- Docker & Docker Compose
- (Optional) CUDA 12+ for PINN GPU training

### Development
```bash
# Clone the repository
git clone https://github.com/openflow3d/openflow3d.git
cd openflow3d

# Install frontend dependencies
cd client && npm install && cd ..

# Install backend dependencies
cd server && pip install -r requirements.txt && cd ..

# Start all services
docker-compose up -d  # Redis, PostgreSQL, InfluxDB
npm run dev            # Frontend + Backend dev servers
```

## 🔬 Core Technologies

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | React 19, Vite 6, Three.js r170 | SPA UI + WebGL 3D rendering |
| **Meshing** | Gmsh (Wasm) + OpenCASCADE.js | Client-side BLM mesh generation |
| **Backend** | FastAPI, Celery, Redis | API + async task dispatch |
| **Solver** | OpenFOAM v12 (Docker) | 3D FVM N-S + Cross-WLF + Tait PVT |
| **AI/ML** | PyTorch, ONNX Runtime Web | PINN, surrogate models, browser inference |
| **Digital Twin** | SciPy LM, DTW, MQTT | Curve alignment + viscosity calibration |
| **Database** | PostgreSQL, SQLite, InfluxDB | Projects, materials, time-series |
| **Deploy** | Docker, Kubernetes, Helm | Container orchestration |

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

## 🙏 Acknowledgments

- [OpenFOAM](https://openfoam.org/) — Open-source CFD platform
- [openInjMoldSim](https://github.com/krebeljk/openInjMoldSim) — Injection molding solver
- [Gmsh](https://gmsh.info/) — 3D finite element mesh generator
- [PyVista](https://pyvista.org/) — 3D scientific visualization
- [Moldex3D](https://www.moldex3d.com/) — Industry reference for injection molding CAE
