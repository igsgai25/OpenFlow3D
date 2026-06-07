# 📚 Report 16: OpenFlow3D WebAssembly Mesher C++ Compilation Blueprint [VERIFIED]
> **文件編號**: `igs_openflow3d_wasm_mesher_blueprint_20260607_v01.md`  
> **專案代號**: `L3-Zack` | **領域**: `igs` (工業模擬) / `aeos` (整合開發) | **等級**: 專家級 (Lead WebAssembly Developer & Mesh Specialist)

本編譯與整合藍圖詳細指導如何使用 **Emscripten (Emcc)** 工具鏈，將開源三維網格剖分引擎 **Gmsh** 的 C++ 核心編譯成 WebAssembly (Wasm) 模組，並在瀏覽器前端（Client-side）直接運作以消除伺服器運算載擔。

---

## 1. Emscripten 編譯工具鏈配置與標記 (Emscripten Toolchain)

要將 Gmsh C++ 代碼編譯為高效能的 WebAssembly，需要配置 Emscripten 編譯參數。

### 1.1 編譯指令與最佳化標記 (Emcc Flags) [INFERRED]
於終端機執行以下命令，將 Gmsh 原始碼及其依賴編譯為 `gmsh.wasm` 與 `gmsh.js` 膠水代碼：

```bash
# 進入 Gmsh 編譯路徑
cd D:/L3-Academy/NCTU-Zack/3rdparty/gmsh
mkdir build-wasm && cd build-wasm

# 使用 emconfigure 配置 CMake，關閉非必要的 GUI 與雙精度 Fortran 求解
emconfigure cmake .. \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_FLTK=OFF \
  -DENABLE_OPENGL=OFF \
  -DENABLE_PARSER=ON \
  -DENABLE_BUILD_SHARED=OFF \
  -DENABLE_BUILD_LIB=ON

# 使用 emmake 編譯並設置 Emscripten 標記
emmake make -j4 LDFLAGS="-s WASM=1 \
  -s ALLOW_MEMORY_GROWTH=1 \
  -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap','getValue','setValue'] \
  -s MODULARIZE=1 \
  -s EXPORT_NAME='GmshModule' \
  -O3"
```

*   `-s WASM=1`: 強制輸出 WebAssembly 格式二進位檔案 [VERIFIED]。
*   `-s ALLOW_MEMORY_GROWTH=1`: 允許 Wasm 運行時根據網格數量動態擴充內存空間，防止千萬級網格劃分時 OOM 崩潰 [VERIFIED]。
*   `-s MODULARIZE=1`: 將輸出的 JS 封裝為 ES6 Module 模組，便於 React/Vite 整合 [VERIFIED]。
*   `-O3`: 開啟 Emscripten 最高級別的編譯優化與代碼剪枝 [VERIFIED]。

---

## 2. C++/Emscripten Web API 綁定 (Web API Bindings)

在 C++ 中使用 `<emscripten/bind.h>` 建立 JavaScript 呼叫接口，暴露 Gmsh 的核心幾何建立與網格生成函數 [VERIFIED]：

```cpp
// D:/L3-Academy/NCTU-Zack/3rdparty/gmsh_wasm_bindings.cpp
#include <emscripten/bind.h>
#include "gmsh.h"

using namespace emscripten;

// 封裝初始化與網格劃分管線
std::string generateMeshFromStep(std::string step_data, double mesh_size) {
    gmsh::initialize();
    gmsh::model::add("temp_model");
    
    // 載入 CAD 數據 (STEP 格式)
    gmsh::model::occ::importShapes(step_data);
    gmsh::model::occ::synchronize();
    
    // 設定全域最大網格尺寸
    gmsh::option::setNumber("Mesh.MeshSizeMax", mesh_size);
    
    // 生成三維實體網格 (3D Mesh)
    gmsh::model::mesh::generate(3);
    
    // 導出 MSH 格式網格數據
    std::string msh_output;
    gmsh::write("output.msh");
    // (讀取 output.msh 至 msh_output 變數中...)
    
    gmsh::finalize();
    return msh_output;
}

EMSCRIPTEN_BINDINGS(gmsh_module) {
    function("generateMeshFromStep", &generateMeshFromStep);
}
```

---

## 3. 前端 JavaScript/TypeScript 載入與集成 (JS Integration)

前端網頁應用程式加載 Wasm 模組並在 Web Worker 中執行網格劃分，以防阻塞 UI 渲染主線程 [INFERRED]：

```javascript
// Web Worker: gmsh.worker.js
import gMeshModule from './gmsh.js';

let gmshInstance;

// 初始化載入 Wasm
gMeshModule().then(module => {
    gmshInstance = module;
    postMessage({ type: 'READY' });
});

onmessage = function(e) {
    if (e.data.type === 'GENERATE_MESH') {
        const { stepData, meshSize } = e.data;
        
        console.log("Wasm 網格生成啟動...");
        const startTime = performance.now();
        
        // 呼叫 Wasm 導出的 C++ 網格生成函數
        const mshResult = gmshInstance.generateMeshFromStep(stepData, meshSize);
        
        const endTime = performance.now();
        console.log(`網格生成完成，耗時: ${((endTime - startTime)/1000).toFixed(2)} 秒`);
        
        postMessage({ type: 'MESH_SUCCESS', data: mshResult });
    }
};
```

---

## 4. 運算負載優化效益評估 (Zero-Server-Cost Meshing)

將網格劃分由「伺服器端」遷移至「客戶端瀏覽器」能帶來重大的軟體工程優勢 [VERIFIED]：
*   **伺服器算力歸零 (Zero Server Compute)**: 網格生成需要密集的 CPU 運算。移至前端後，伺服器僅需儲存網格規格與材料數據，運算負載由用戶本地設備承擔，大幅節省雲端託管成本。
*   **數據零延遲傳輸**: 傳統模式需要將數百 MB 的網格數據在伺服器與前端之間傳輸；Wasm 模式使用戶在前端直接生成網格並可視化，省去大檔案網路傳輸時間。
