# 📚 Report 10: Moldex3D iMolding Calibrator 168-Hour Project Engineering Plan [VERIFIED]
> **文件編號**: `igs_moldex3d_classic_product_168h_engineering_plan_20260607_v01.md`  
> **專案代號**: `L3-Zack` | **領域**: `igs` (工業模擬) / `aeos` (專案工程) | **等級**: 專家級 (Director of Engineering & PMO Lead)

本專案工程計劃為在 168 小時（以目標為導向的長週期任務）內，利用 Google Antigravity IDE 協同建立 **Moldex3D iMolding (機台特徵化與壓力曲線校準引擎)** 的工程實現規劃。

---

## 📅 168 小時工程進度表 (168-Hour Master Schedule)

### 🏁 階段一：環境建置、SSOT 宣告與系統設計 (Hour 1 - 24)
*   **目標**: 完成工作區物理隔離、環境依賴安裝與底層架構設計。
    *   **Hour 1 - 4**: 於 Google Antigravity IDE 中建立專案目錄 `D:/L3-Academy/NCTU-Zack`，編寫基礎 [GEMINI.md](file:///D:/L3-Academy/NCTU-Zack/GEMINI.md) 確定單一事實來源 [VERIFIED]。
    *   **Hour 5 - 12**: 配置 Python 3.10 虛擬環境，安裝科學計算依賴（NumPy, SciPy, Pandas, paho-mqtt）並進行環境性能基準測試。
    *   **Hour 13 - 24**: 撰寫詳細的軟體需求說明書與數據流管道規格（包含 OPC UA 資料交換欄位定義格式）。
    *   **🛡️ 品質門禁 (Quality Gate 1)**: 執行 Antigravity 安全稽核，確認專案目錄內無衝突的全量 AST 掃描威脅，確保 `Topological Pruner` 配置生效。

---

### 📡 階段二：高頻數據採集與數位濾波模組 (Hour 25 - 72)
*   **目標**: 完成邊緣 MQTT 採集管道與數據降噪演算法的編寫。
    *   **Hour 25 - 40**: 撰寫 MQTT 數據接收訂閱器，支持異步接收高頻射出機台狀態遙測數據流（螺桿位置、射出壓力），並寫入快取資料庫。
    *   **Hour 41 - 56**: 實現 Savitzky-Golay 與滑動窗口平均 (Moving Average) 濾波器，針對原始數據進行平滑，濾除射出機液壓閥切換產生的電磁毛刺 [INFERRED]。
    *   **Hour 57 - 72**: 實作異常檢測機制（如檢測空射、感測器斷線等），輸出符合物理約束的標準化時間序列。
    *   **🛡️ 品質門禁 (Quality Gate 2)**: 運行單元測試，比對濾波前後壓力波峰的 RMSE，確保波峰壓力失真小於 **0.5%** [INFERRED]。

---

### ⏱️ 階段三：虛實時間軸自動對齊演算法 (Hour 73 - 120)
*   **目標**: 實現機台響應延遲補償與時間序列對齊演算法。
    *   **Hour 73 - 88**: 實作基礎「波峰-起點雙特徵點」時間軸對齊算法，識別系統性滯後時間 $\Delta t_{\text{delay}}$ [INFERRED]。
    *   **Hour 89 - 104**: 實作動態時間規整 (DTW) 進階對齊演算法，處理非線性充填速度波動引起的局部拉伸與壓縮 [INFERRED]。
    *   **Hour 105 - 120**: 開發對齊數據可視化模組（可於 Web 介面渲染 Sim2Real 對比圖線）。
    *   **🛡️ 品質門禁 (Quality Gate 3)**: 使用包含 0.354 秒隨機延遲的合成測試數據集，驗證對齊演算法在 $\pm 5\text{ ms}$ 精准度內精確尋回延遲參數 [VERIFIED]。

---

### 🔄 階段四：黏度漂移反算與閉環工藝派發 (Hour 121 - 144)
*   **目標**: 實作基於最小平方法的流變參數修正與自動配方生成。
    *   **Hour 121 - 132**: 建立基於 SciPy 優化庫的 Levenberg-Marquardt (LM) 反算求解器，反算 Cross-WLF 黏度修正值 $\Delta D_1$ [INFERRED]。
    *   **Hour 133 - 144**: 編寫 EUROMAP 77 / OPC UA 標準的配方封裝器，實作將最佳化參數轉化為機台製程設定值（包含保壓切換位置、速度段數），並部署配方安全回滾鎖定。
    *   **🛡️ 品質門禁 (Quality Gate 4)**: 執行爆炸半徑（Blast Radius）評估，確保此階段代碼變更不會破壞階段二的濾波模組。

---

### 🧪 階段五：系統整合、實機測試與教材編譯 (Hour 145 - 168)
*   **目標**: 完成系統端到端集成測試，驗證數位分身閉環，並編譯教學資源。
    *   **Hour 145 - 156**: 執行全鏈路集成測試：從模擬大數據讀取 $\rightarrow$ 模擬實體機台高頻採集 $\rightarrow$ 時間對齊 $\rightarrow$ 參數反算 $\rightarrow$ 生成配方檔 [VERIFIED]。
    *   **Hour 157 - 164**: 調用 `Jupyter PBL Lab Compiler` 技能，將開發的校準與對齊演算法編譯為標準課程實驗檔案，並注入 "Level Up" 挑戰 Scaffolding [VERIFIED]。
    *   **Hour 165 - 168**: 撰寫專案交付報告，將所有代碼提交至版本控制系統，完成 168 小時工程交付。
    *   **🛡️ 終極品質門禁 (Final Quality Gate)**: 確保所有 10 份超級報告已正確鏈接，且無代碼編譯或物理量測的事實層面不確定性標記漂移。
