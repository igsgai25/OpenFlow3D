# 📚 Report 2: Core CAE Simulation Solver Physics & Tech [VERIFIED]
> **文件編號**: `igs_moldex3d_core_simulation_solver_report_20260607_v01.md`  
> **專案代號**: `L3-Zack` | **領域**: `igs` (工業模擬) | **等級**: 專家級 (Physics & Numerical Solver Specialist)

本報告將從偏微分方程 (PDE) 求解、高分子流變學以及離散數值方法的角度，深入剖析 Moldex3D 三維模流求解器的核心物理與數值計算技術。

---

## 1. 控制方程組 (Governing Equations for Polymer Flow)

射出成型過程中的熔融塑料被視為**非等溫、非牛頓、壓縮性黏性流體**。其物理流動在三維空間內由以下守恆定律（控制方程）描述 [VERIFIED]：

### 1.1 連續方程式 (Continuity Equation)
描述質量守恆，考量熔膠的壓縮性（比容隨壓力與溫度變化）：
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0$$
其中 $\rho$ 為熔膠密度，$\mathbf{u}$ 為三維速度向量。

### 1.2 動量方程式 (Momentum Equation / Navier-Stokes)
描述動量守恆，熔膠流動屬於極低 Reynolds 數（通常 $Re \ll 1$，高黏度），因此慣性項通常可忽略：
$$\frac{\partial}{\partial t}(\rho \mathbf{u}) + \nabla \cdot (\rho \mathbf{u} \mathbf{u}) = -\nabla p + \nabla \cdot \boldsymbol{\tau} + \rho \mathbf{g}$$
其中 $p$ 為靜水壓力，$\boldsymbol{\tau}$ 為剪切應力張量，$\mathbf{g}$ 為重力加速度。

### 1.3 能量方程式 (Energy Equation)
描述熱量傳遞，其中高分子流體流動時的**剪切生熱項 (Viscous Dissipation)** 極為關鍵，通常會造成局部溫度大幅上升：
$$\rho C_p \left( \frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T \right) = \nabla \cdot (k \nabla T) + \boldsymbol{\tau} : \nabla \mathbf{u}$$
其中 $C_p$ 為比熱，$T$ 為溫度，$k$ 為熱傳導率，$\boldsymbol{\tau} : \nabla \mathbf{u}$ 為黏滯生熱項（黏滯耗散率）。

---

## 2. 流變學與狀態方程式 (Rheology & Equations of State)

為求解上述方程組，必須引入材料的本構方程（黏度模型）與熱物理特性方程：

### 2.1 Cross-WLF 黏度模型 (Rheology Model) [VERIFIED]
剪切黏度 $\eta$ 隨剪切率 $\dot{\gamma}$、壓力 $p$ 與溫度 $T$ 變化，Moldex3D 常用的 Cross-WLF 模型公式如下：
$$\eta(T, p, \dot{\gamma}) = \frac{\eta_0(T, p)}{1 + \left( \frac{\eta_0 \dot{\gamma}}{\tau^*} \right)^{1-n}}$$
其中：
*   $\eta_0(T, p)$ 為零剪切黏度 (Zero-shear viscosity)。
*   $\tau^*$ 為剪切變稀過渡區的臨界應力特徵值。
*   $n$ 為剪切變稀指數 ($n < 1$)。
*   零剪切黏度 $\eta_0$ 使用 WLF 方程式描述：
$$\eta_0(T, p) = D_1 \exp \left[ \frac{-A_1 (T - T_c)}{A_2 + (T - T_c)} \right]$$
其中 $T_c = D_2 + D_3 p$，$A_2 = \tilde{A}_2 + D_3 p$。

### 2.2 改良型 Tait PVT 狀態方程式 (Equation of State) [VERIFIED]
比容 $v = 1/\rho$ 隨溫度 $T$ 與壓力 $p$ 變化的物理特性由改良型 Tait 方程定義：
$$v(T, p) = v_0(T) \left[ 1 - C \ln\left(1 + \frac{p}{B(T)}\right) \right] + v_t(T, p)$$
該方程精確定義了熔融態與固態之間的轉折點，是預測保壓收縮與變形量（Warpage）的基石。

---

## 3. 網格技術與數值離散法 (Meshing & Discretization)

### 3.1 邊界層網格技術 (Boundary Layer Mesh - BLM) [VERIFIED]
*   **物理背景**: 熔膠流動時，模壁邊界的速度梯度（剪切率）與溫度梯度極大。
*   **技術實現**: Moldex3D 採用稜柱體網格 (Prism Mesh) 或高品質六面體網格 (Hexahedral Mesh) 在模壁邊界堆疊 3 至 11 層薄網格（如圖 2.1 所示），精確捕捉 fountain flow（噴泉流）與固化層 (Frozen Layer) 的動態厚度。

### 3.2 有限體積法與有限元素法混合離散 (Hybrid FVM/FEM Solver) [INFERRED]
*   **流動分析 (Flow/Pack Solver)**: 主要使用有限體積法 (FVM)，具備優異的局部質量守恆性，適合追蹤熔膠前沿 (Melt Front) 的三維自由液面變化。
*   **結構應力與翹曲分析 (Warp Solver)**: 主要使用有限元素法 (FEM)，適合求解固體受力、彈塑性變形與微觀纖維配向產生的各向異性殘留應力。
