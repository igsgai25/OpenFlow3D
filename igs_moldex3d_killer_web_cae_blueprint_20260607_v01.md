# 📚 Report 15: The Moldex3D Killer — Open-Source Python & Web-CAE Blueprint [VERIFIED]
> **文件編號**: `igs_moldex3d_killer_web_cae_blueprint_20260607_v01.md`  
> **專案代號**: `L3-Zack` | **領域**: `igs` (工業模擬) / `chu` (教學與實驗) | **等級**: 專家級 (Chief Technology Officer & CAE Founder)

本報告勾勒出一個具有破局意義的「Moldex3D Killer」開源、Web化、Python驅動之三維模流分析與數位分身系統 —— **OpenFlow3D** 的架構設計藍圖。報告內含 100 大領域關鍵字對照表與系統實作規劃。

---

## 1. 模流分析與數位分身 100 大領域關鍵字 (Top 100 Keywords Matrix)

以下為本專案核心領域的 100 個關鍵字對照表，分為 10 大關鍵類別，每類包含 10 個核心術語 [VERIFIED]：

| 類別 | #1 - #5 關鍵字 | #6 - #10 關鍵字 |
|---|---|---|
| **1. 流變學與高分子物理** | 剪切變稀 (Shear Thinning), 剪切率 (Shear Rate), 零剪切黏度 (Zero-shear Viscosity), 黏滯加熱 (Viscous Heating), Cross-WLF Model | Tait PVT Equation, 結晶動力學 (Crystallization Kinetics), 固化層 (Frozen Layer), 玻璃轉移溫度 ($T_g$), 熔融指數 (MFR) |
| **2. 射出成型工藝** | 充填階段 (Filling), 保壓階段 (Packing), 冷卻階段 (Cooling), 翹曲變形 (Warpage), 射出壓力 (Injection Pressure) | 鎖模力 (Clamp Force), 保壓切換點 (V/P Switch), 澆口凍結 (Gate Freeze), 短射 (Short Shot), 結合線/縫合線 (Weld Line) |
| **3. 控制偏微分方程** | 質量守恆 (Mass Conservation), 動量守恆 (Momentum Conservation), 能量方程式 (Energy Equation), 納維-斯托克斯 (Navier-Stokes), 黏性耗散 (Viscous Dissipation) | 剪切應力張量 (Stress Tensor), 熱傳導方程 (Heat Conduction), 纖維取向張量 (Fiber Orientation), 殘留應力 (Residual Stress), 兩相流前沿 (Melt Front) |
| **4. 數值離散與求解** | 有限體積法 (FVM), 有限元素法 (FEM), 代數多重網格 (AMG), 共軛梯度法 (PCG), 壓力修正法 (PISO/SIMPLE) | 自由液面追蹤 (VOF), 庫朗數 (Courant Number), 時間步長 (Time Step), 動態網格 (Dynamic Mesh), 多物理場耦合 (Multi-physics) |
| **5. 網格剖分技術** | 邊界層網格 (BLM), 四面體網格 (Tetra Mesh), 六面體網格 (Hex Mesh), 非匹配網格 (Non-matching), 表面重建 (Surface Triangulation) | 網格自適應 (AMR), 雅可比矩陣檢驗 (Jacobian), 五角錐過渡 (Pyramid Mesh), 網格修補 (Mesh Repair), 八叉樹剖分 (Octree) |
| **6. 數位分身與實機** | 虛實整合 (Sim2Real), 機器特徵化 (Machine Profiling), 螺桿動態響應 (Screw Response), 壓力傳遞損耗 (Pressure Loss), 模穴壓力感測 (Cavity Pressure) | 模溫動態監測 (Mold Temperature), 閉環優化 (Closed-loop), 參數校準 (Calibration), 批次自適應 (Batch Adaptation), 實物試模 (Mold Trial) |
| **7. 工業通訊與邊緣** | 工業物聯網 (IIoT), OPC UA, 邊緣運算閘道 (Edge Gateway), MQTT Protocol, Modbus TCP | 數據清洗 (Data Cleaning), 噪聲濾波 (Noise Filtering), 實時資料庫 (TSDB), 本地 PLC 控制, 配方下傳 (Recipe Dispatch) |
| **8. 圖形渲染與軟體** | OpenGL Core, 著色器 (Shader Program), VTK Library, Qt Framework, QML Interactive | 雙緩衝渲染 (Double Buffering), 視角裁剪 (Clipping Plane), 多線程 GUI (Multi-thread GUI), 異步渲染 (Async Render), WebGL |
| **9. 開源 CAE 生態** | OpenFOAM, openInjMoldSim, Gmsh Mesher, PyVista Wrapper, WebAssembly (Wasm) | FreeCAD Integration, FEniCS Project, Docker Containers, Kubernetes HPC, ParaView Web |
| **10. 人工智慧與優化** | 代理模型 (Surrogate Model), 物理神經網路 (PINN), 均方根誤差 (RMSE), 遺傳演算法 (Genetic Algorithm), 機器學習 (ML) | 梯度下降 (Gradient Descent), 損失函數 (Loss Function), 動態時間規整 (DTW), 貝氏優化 (Bayesian Opt), 超參數調優 (HPO) |

---

## 2. OpenFlow3D — 模流分析破局軟體架構藍圖 (System Architecture)

**OpenFlow3D** 旨在利用開源、Python 與 Web 技術打破商業 CAE 軟體的壟斷，其架構分為四大核心層級 [INFERRED]：

```
                       ┌─────────────────────────────────────────┐
                       │  WEB 前端表現層 (React + Three.js / Wasm)│
                       └─────────────────────────────────────────┘
                                            │
                             WebSocket / RESTful API (FastAPI)
                                            │
                                            ▼
                       ┌─────────────────────────────────────────┐
                       │  PYTHON 中間件與 AI 優化層 (Celery/PINN)  │
                       └─────────────────────────────────────────┘
                                            │
                                  C++ / Fortran MPI 接口
                                            │
                                            ▼
                       ┌─────────────────────────────────────────┐
                       │  開源 3D 數值求解器核心 (OpenFOAM / FVM)  │
                       └─────────────────────────────────────────┘
```

### 2.1 Web 前端表現層 (SaaS Visual Frontend) [INFERRED]
*   **介面框架**: React + Vite + TailwindCSS 打造高質感極簡風格介面。
*   **3D Viewport**: 使用 **Three.js** 或 **VTK.js**，直接在瀏覽器中利用 GPU 渲染百萬網格，免除本地安裝負擔。
*   **前處理幾何編輯**: 透過 **WebAssembly** 移植開源 CAD 核心（如 OpenCASCADE.js），使用戶在瀏覽器內即可進行澆口位置拖動、流道半徑調整與網格修補。

### 2.2 Python 中間件與運算協調層 (Python Broker & AI Core) [INFERRED]
*   **Web API**: 基於 **FastAPI** 實現高並發 API，使用 **WebSocket** 實時推送求解進度與收斂殘差。
*   **任務調度**: 使用 **Celery + Redis** 異步佇列，支持將大規模運算分發至雲端運算叢集。
*   **AI 代理引擎**: 使用 **PyTorch** 訓練 PINN (物理資訊神經網路)，輸入產品 3D 幾何特徵，在 <100ms 內即時預測流動前沿與收縮變形，作為前置快速尋優手段。

### 2.3 運算引擎與數據管線 (Solver & Data Engine) [INFERRED]
*   **網格劃分**: 後端集成 **Gmsh**，支持自動生邊界層網格 (BLM)。
*   **FVM 求解器**: 基於 Docker 容器化的 **OpenFOAM (openInjMoldSim)** 求解器，求解 Navier-Stokes 與熱傳導方程，採用 Tait PVT 與 Cross-WLF 計算黏性阻力。
*   **數位分身數據鏈**: 邊緣端以 Python MQTT 客戶端訂閱射出機 OPC UA 數據，實時寫入 **InfluxDB** 時序資料庫，並由 **SciPy LM 優化演算法** 反向調校 Cross-WLF 黏度參數。

---

## 3. 性能驗證與實踐路徑 (Performance Verification Path)

為了向市場證明 OpenFlow3D 的精度與效率，我們制定了以下基準驗證路徑 [INFERRED]：

1.  **標準件比對 (ASTM D638 Dogbone 測試)**:
    *   以標準拉伸試片（Dogbone）作為基準模型。
    *   在相同成型條件下，對比 OpenFlow3D 與 Moldex3D 的**充填峰值壓力 (Peak Pressure)**、**保壓壓力變化曲線** 與 **最大翹曲量** 的 RMSE。目標設定為誤差小於 **$\pm 5\%$** 以內。
2.  **型腔流動平衡 A/B 測試**:
    *   使用多模穴熱流道模型，測試 1D/3D 流道耦合對齊速度，並比對各模穴流動不平衡度（Flow Unbalance %），證明運算效率提升與高精度的兼容性。
