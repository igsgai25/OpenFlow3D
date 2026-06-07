# 📚 Report 13: Moldex3D Studio GitHub Open Source Research Report [VERIFIED]
> **文件編號**: `igs_moldex3d_studio_github_repos_report_20260607_v01.md`  
> **專案代號**: `L3-OpenFlow3D` | **領域**: `igs` (工業模擬) | **等級**: 專家級 (Open-Source CAE Researcher)

本報告對全球與塑膠射出成型模擬、三維有限元素網格生成、以及科學可視化相關的 Top 5 開源 GitHub 倉庫進行深度評析與技術架構探索，為打造自主產權之模流分析軟體奠定技術庫備份與代碼研讀基礎。

---

## 1. Top 5 關鍵開源專案技術特徵 (Top 5 GitHub Repos)

### 📂 1. openInjMoldSim — OpenFOAM 射出流阻求解器 [VERIFIED]
*   **倉庫位址**: [krebeljk/openInjMoldSim](https://github.com/krebeljk/openInjMoldSim)
*   **語言與基礎**: C++ (OpenFOAM C++ API)，建置於 `compressibleInterFoam` 雙相流求解器之上。
*   **核心物理**: 求解非等溫、可壓縮、剪切變稀的高分子熔體層流。內嵌 **Modified Tait PVT 狀態方程式** 與 **Cross-WLF 黏度模型**。
*   **軟體工程價值**: 提供了將高分子本構模型（Cross-WLF）寫入 OpenFOAM 場變數（Field Variables）計算的標準 C++ 示範，是開源模流求解器的核心基礎。

### 📂 2. openInjMoldDyMSimCr — 結晶與模具變形擴充求解器 [VERIFIED]
*   **倉庫位址**: [krebeljk/openInjMoldDyMSimCr](https://github.com/krebeljk/openInjMoldDyMSimCr)
*   **語言與基礎**: C++ (OpenFOAM 7 / 8)
*   **核心物理**: 基於 `openInjMoldSim`，引入了 **Kolmogorov-Avrami-Evans 結晶動力學模型**，並增加了動態網格（Dynamic Mesh, DyM）功能，以計算射出高壓下模具與鑲件的熱力耦合微小彈性變形。
*   **軟體工程價值**: 示範了如何在有限體積求解器中動態變形網格節點，對標 Moldex3D 2026 最新雙中村結晶模型 (Dual Nakamura) 與模具移動效應。

### 📂 3. injectionMoldingFoam — 纖維取向模流求解器 [VERIFIED]
*   **倉庫位址**: [fospald/injectionMoldingFoam](https://github.com/fospald/injectionMoldingFoam)
*   **語言與基礎**: C++ / OpenFOAM
*   **核心物理**: 專注於短玻纖與長玻纖強化材料在充填過程中的取向行為計算，內嵌 **Folgar-Tucker 玻纖取向張量方程** 及其各向異性流動修正項。
*   **軟體工程價值**: 說明了如何在流動場（Velocity Field）求解的同時，即時計算懸浮顆粒的旋轉張量，為結構強度分析（FEA Interface）提供取向特徵矩陣。

### 📂 4. Gmsh — 開源三維有限元素網格生成引擎 [VERIFIED]
*   **倉庫位址**: [gitlab.onelab.info/gmsh/gmsh](https://gitlab.onelab.info/gmsh/gmsh) (及 GitHub 各類鏡像)
*   **語言與基礎**: C++11 / Python API
*   **核心物理/網格**: 提供 Delaunay、Frontal-Delaunay 三維四面體與六面體网格算法。內建強大的 **邊界層網格 (Boundary Layer Mesh, BLM)** 生成演算法，可對壁面法向進行等比級數或自定義厚度的網格層堆疊。
*   **軟體工程價值**: Moldex3D 專利 BLM 網格的開源替代方案。其 Python API 綁定極為成熟，可輕易整合入自動化網格劃分管線中。

### 📂 5. PyVista — 3D 科學可視化與 VTK 封裝 [VERIFIED]
*   **倉庫位址**: [pyvista/pyvista](https://github.com/pyvista/pyvista)
*   **語言與基礎**: Python / VTK (C++)
*   **核心物理/渲染**: 基於 C++ 高性能科學可視化庫 **VTK (Visualization Toolkit)** 封裝的 Python 模組。支持在桌面端與 Web 端進行三維流動向量線 (Streamlines)、斷面雲圖 (Slicing) 與變形翹曲渲染。
*   **軟體工程價值**: 替代 Moldex3D Studio C++/OpenGL 渲染核心的絕佳方案，大幅降低了 3D 前後處理可視化的自研門檻，提供流暢的百萬網格渲染能力。

---

## 2. 代碼下載與研讀指令集 (Download & Read Instructions) [INFERRED]

為將上述庫載入 Horace 教授的先導工作區進行研讀，可於工作區終端機執行以下 Bash/PowerShell 下載與編譯探索腳本：

```bash
# 建立專案第三方依賴目錄
mkdir -p D:/L3-Academy/OpenFlow3D/3rdparty
cd D:/L3-Academy/OpenFlow3D/3rdparty

# 1. 克隆核心流動求解器 openInjMoldSim
git clone --depth 1 https://github.com/krebeljk/openInjMoldSim.git

# 2. 克隆網格生成引擎 Gmsh (唯讀鏡像)
git clone --depth 1 https://github.com/uberec/gmsh.git

# 3. 克隆可視化封裝 PyVista
git clone --depth 1 https://github.com/pyvista/pyvista.git
```
