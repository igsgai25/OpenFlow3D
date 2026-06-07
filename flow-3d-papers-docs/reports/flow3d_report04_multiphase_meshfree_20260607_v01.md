# Report 4: Multiphase & Meshfree Methods — LBM, SPH, FAVOR

**PhD-Level Deep Research Report** | **Theory 4** | Generated: 2026-06-07

---

## Executive Summary

Beyond traditional grid-based methods (FVM, FEM, FDM), alternative computational paradigms have emerged for 3D flow simulation. The Lattice Boltzmann Method (LBM) operates at the mesoscopic kinetic level, Smoothed Particle Hydrodynamics (SPH) adopts a Lagrangian meshfree approach, and FAVOR (Fractional Area/Volume Obstacle Representation) provides a unique geometry-decoupled approach on structured grids. This report analyzes these paradigms, their theoretical foundations, advantages, limitations, and cutting-edge developments.

---

## 1. Lattice Boltzmann Method (LBM)

### 1.1 Theoretical Foundation

Instead of discretizing the Navier-Stokes equations directly, LBM discretizes the **Boltzmann transport equation** in a simplified lattice space:

```
f_i(x + c_i*dt, t + dt) = f_i(x, t) + Omega_i(f)
```

where:
- f_i = particle distribution function for velocity direction i
- c_i = discrete lattice velocity
- Omega_i = collision operator

**BGK (Bhatnagar-Gross-Krook) simplification**:
```
Omega_i = -(f_i - f_i^eq) / tau
```

where tau is the relaxation time related to kinematic viscosity: nu = c_s^2 * (tau - dt/2)

### 1.2 Key LBM Models

| Model | Type | Application | Year |
|:---|:---|:---|:---:|
| D3Q19 | 3D, 19 velocities | Standard incompressible flows | 1992 |
| D3Q27 | 3D, 27 velocities | Higher accuracy, more isotropic | 1992 |
| Shan-Chen | Pseudopotential | Multiphase flows (simple) | 1993 |
| Free Energy | Thermodynamic | Multiphase with correct thermodynamics | 1995 |
| Color Gradient | Interface | Immiscible two-phase flows | 1991 |
| MRT | Multi-relaxation | Improved stability | 2002 |
| Cumulant | Central moments | Best stability & accuracy | 2015 |
| Regularized | Pre-collision | Reduced memory, stable | 2006 |

### 1.3 Strengths and Limitations

**Strengths**:
- Inherently parallel (explicit local updates only)
- Natural handling of complex geometries (bounce-back boundaries)
- Multiphase flows without explicit interface tracking
- Efficient for porous media (no mesh generation needed)

**Limitations**:
- Restricted to low Mach number (Ma < 0.3 for standard models)
- Memory intensive (distribution function stored at each node)
- Surface tension modeling less mature than VOF
- Limited for high Reynolds number turbulence

---

## 2. Smoothed Particle Hydrodynamics (SPH)

### 2.1 Theoretical Foundation

SPH discretizes the NS equations using Lagrangian particles, each carrying fluid properties:

```
<A(r)> = integral A(r') * W(r - r', h) dr'
```

Particle approximation:
```
<A(r_a)> = sum_b (m_b / rho_b) * A(r_b) * W(r_a - r_b, h)
```

where W is the smoothing kernel (e.g., cubic spline, Wendland C2) and h is the smoothing length.

### 2.2 Key SPH Variants

| Variant | Feature | Application |
|:---|:---|:---|
| WCSPH | Weakly compressible (equation of state) | Free-surface flows, wave breaking |
| ISPH | Truly incompressible (pressure Poisson) | Low-speed internal flows |
| delta-SPH | Density diffusion term for stability | General free-surface |
| delta+-SPH | Enhanced particle shifting | Improved particle distribution |
| DualSPHysics | GPU-accelerated open-source | Coastal engineering |

### 2.3 Strengths and Limitations

**Strengths**:
- No mesh generation required (truly meshfree)
- Natural handling of free surfaces and large deformations
- Naturally captures topology changes (fragmentation, coalescence)
- Lagrangian tracking of material properties (history-dependent)

**Limitations**:
- Inconsistency at boundaries (tensile instability)
- Particle disorder and noise in pressure field
- Higher computational cost per degree of freedom vs grid methods
- Difficulty enforcing boundary conditions accurately

---

## 3. FAVOR (Fractional Area/Volume Obstacle Representation)

### 3.1 Core Concept

FAVOR defines obstacles within a fixed Cartesian grid by assigning:
- **Volume fraction** V_f: fraction of cell volume open to flow (0 = solid, 1 = fluid)
- **Area fractions** A_f: fraction of each cell face open to flow

### 3.2 Advantages Over Body-Fitted Meshes

| Feature | Body-Fitted Mesh | FAVOR (Cartesian + Fractions) |
|:---|:---|:---|
| Mesh generation time | Hours to weeks | Minutes |
| Geometry modification | Requires complete remesh | Only update V_f, A_f |
| Numerical accuracy | High (boundary-conforming) | Good (sub-grid geometry) |
| Parallelization | Complex (load balancing) | Simple (structured grid) |
| Moving geometry | Complex (ALE, morphing) | Moderate (recompute fractions) |

---

## 4. Five-Layer 5W1H Analysis

### Layer 1: Surface

| Q | Analysis |
|:---|:---|
| **What** | Alternative computational paradigms that bypass traditional mesh-based discretization of NS equations |
| **Who** | LBM: McNamara & Zanetti (1988); SPH: Gingold & Monaghan (1977); FAVOR: Hirt & Sicilian (1985) |
| **When** | LBM matured 2000s-present; SPH matured 2010s-present; FAVOR has been core to FLOW-3D since 1985 |
| **Where** | LBM: porous media, microfluidics, multiphase; SPH: coastal, geotechnics; FAVOR: casting, hydraulics |
| **Why** | Each method excels where traditional mesh methods struggle: complex geometry, free surfaces, multi-scale |
| **How** | LBM: kinetic theory on lattice; SPH: particles with smoothing kernels; FAVOR: fractions on Cartesian grid |

### Layer 2: Mechanism

| Q | Analysis |
|:---|:---|
| **What** | LBM: mesoscopic particle distributions recover NS via Chapman-Enskog expansion; SPH: Lagrangian kernel interpolation; FAVOR: blocked-cell fractions |
| **Who** | Chen & Doolen (1998, LBM review); Monaghan (2005, SPH review); Hirt (1993, FAVOR wind engineering) |
| **When** | LBM recovers NS at low Mach; SPH converges with sufficient particles; FAVOR accuracy depends on resolution |
| **Where** | LBM: lattice nodes; SPH: particle positions; FAVOR: Cartesian cell centers + face fractions |
| **Why** | Each encodes NS physics differently: LBM via kinetic theory, SPH via kernel approximation, FAVOR via volume blocking |
| **How** | LBM: stream-collide algorithm; SPH: neighbor search + kernel evaluation; FAVOR: modify NS fluxes by A_f, V_f |

### Layer 3: Mathematics

| Q | Analysis |
|:---|:---|
| **What** | LBM: Boltzmann eq. + BGK/MRT collision; SPH: integral interpolation theory; FAVOR: modified finite difference |
| **Who** | He & Luo (1997, LBM theory); Liu & Liu (2003, SPH theory); Hirt & Sicilian (1985, FAVOR theory) |
| **When** | LBM recovers NS to O(Ma^2); SPH converges as h/dx -> 0; FAVOR accuracy ~ dx (1st order at boundaries) |
| **Where** | LBM: discrete velocity space (D3Q19/27); SPH: continuous position space; FAVOR: Cartesian + fraction space |
| **Why** | LBM: kinetic equation simpler than NS for some physics; SPH: no mesh topology constraints; FAVOR: grid simplicity |
| **How** | Chapman-Enskog: f = f^eq + epsilon*f^(1) + ... recovers continuity + momentum at O(epsilon^2) |

### Layer 4: Computation

| Q | Analysis |
|:---|:---|
| **What** | LBM: stream-collide on lattice; SPH: particle interaction via neighbor lists; FAVOR: standard NS with modified stencils |
| **Who** | LBM: Palabos, waLBerla, OpenLB; SPH: DualSPHysics, GPUSPH; FAVOR: FLOW-3D exclusively |
| **When** | LBM: O(N) per time step (explicit); SPH: O(N*log(N)) with tree search; FAVOR: same as FDM/FVM |
| **Where** | LBM excels on GPU (data-parallel); SPH accelerated by GPU; FAVOR runs on standard CPU/GPU hardware |
| **Why** | LBM: massive parallelism from local operations; SPH: particle independence; FAVOR: structured grid efficiency |
| **How** | LBM: 1 copy + 1 collision per node per step; SPH: kernel sums over ~50-100 neighbors; FAVOR: modified Poisson solve |

### Layer 5: Application

| Q | Analysis |
|:---|:---|
| **What** | LBM: porous media, blood flow, emulsions; SPH: tsunamis, landslides, explosions; FAVOR: casting, hydraulics |
| **Who** | LBM: oil/gas (pore-scale), biomedical; SPH: coastal engineering, defense; FAVOR: foundries, water utilities |
| **When** | LBM: emerging in industry (2020s); SPH: established in coastal/defense; FAVOR: 40 years in casting/hydro |
| **Where** | LBM: micro/meso scales; SPH: macro with large deformations; FAVOR: any scale with complex geometry |
| **Why** | Each fills a niche: LBM for porous/micro, SPH for large-deformation free surface, FAVOR for rapid prototyping |
| **How** | Choose based on: scale (micro->LBM), deformation (large->SPH), geometry complexity (complex->FAVOR), cost (budget->FAVOR) |

---

## 5. Twenty-One Why Analysis

| # | Why Question | Answer |
|:---:|:---|:---|
| 1 | Why develop alternatives to FVM/FEM? | Because mesh generation for complex 3D geometries consumes 50-80% of total CFD project time |
| 2 | Why is mesh generation so time-consuming? | Complex geometries require body-fitted grids with quality constraints (skewness, aspect ratio, orthogonality) |
| 3 | Why does LBM avoid mesh problems? | LBM uses a uniform Cartesian lattice; geometry handled by bounce-back boundary conditions |
| 4 | Why is LBM inherently parallel? | Each node's stream-collide update depends only on immediate neighbors — perfect for GPU |
| 5 | Why is LBM limited to low Mach? | Standard LBM has O(Ma^2) compressibility error; high Ma causes numerical instability |
| 6 | Why does SPH not need a mesh? | SPH discretizes the fluid as particles; interactions are kernel-weighted sums over neighbors |
| 7 | Why is SPH good for free surfaces? | Particles naturally represent the fluid domain — no special treatment needed for the surface |
| 8 | Why does SPH have pressure noise? | Weakly-compressible SPH uses equation of state, which allows density fluctuations and pressure oscillations |
| 9 | Why was delta-SPH developed? | Adding density diffusion reduces pressure noise while maintaining conservation properties |
| 10 | Why is FAVOR unique to FLOW-3D? | It's a proprietary technology that gives FLOW-3D its competitive advantage in rapid setup |
| 11 | Why doesn't everyone use FAVOR? | It works best on structured Cartesian grids; unstructured grids (used by most other solvers) need different approaches |
| 12 | Why are GPU-accelerated methods important? | GPU provides 10-100x speedup for data-parallel algorithms like LBM and SPH |
| 13 | Why are hybrid methods emerging? | Each method has strengths/weaknesses; combining them captures the best of each (e.g., SPH-FEM coupling) |
| 14 | Why couple DEM with CFD? | Many industrial flows involve particles (fluidized beds, sediment transport); DEM models particle mechanics |
| 15 | Why is the Material Point Method gaining traction? | MPM handles solid-fluid transition (e.g., landslides, snow avalanche) that neither pure SPH nor FEM handles well |
| 16 | Why are phase-field methods an alternative to VOF? | Phase-field (Cahn-Hilliard/Allen-Cahn) provides smoother interface with thermodynamically consistent surface tension |
| 17 | Why not always use phase-field? | Phase-field requires resolving a diffuse interface (~5-10 cells wide); VOF maintains sharp (1-cell) interface |
| 18 | Why is LBM popular for porous media? | Complex pore geometries are naturally handled by bounce-back BC; no mesh generation needed for micro-CT data |
| 19 | Why is SPH the method of choice for DualSPHysics? | Open-source GPU-accelerated SPH solver has become the standard tool for coastal engineering simulations |
| 20 | Why are population balance equations (PBE) important? | For bubbly/dispersed flows, PBE tracks the size distribution of bubbles/droplets alongside the two-fluid model |
| 21 | Why will meshfree methods become more important? | As problems become more complex (AM, bio, multi-physics), the mesh generation bottleneck becomes the dominant cost driver |

---

*Report 4 of 10 | Flow in 3D PhD Research Project | AEOS Director Sigma v9.1*
