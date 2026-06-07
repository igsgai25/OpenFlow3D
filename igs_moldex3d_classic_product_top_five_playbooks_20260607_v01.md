# 📚 Report 8: Moldex3D iMolding Top 5 Playbooks (SOP) [VERIFIED]
> **文件編號**: `igs_moldex3d_classic_product_top_five_playbooks_20260607_v01.md`  
> **專案代號**: `L3-OpenFlow3D` | **領域**: `igs` (工業模擬) | **等級**: 專家級 (Operations & Quality Assurance Director)

本報告為 **Moldex3D iMolding (機台特徵化與壓力曲線校準引擎)** 提供 5 套在工業現場與研發端運行的標準作業劇本 (Standard Operating Playbooks, SOP)。

---

## 📖 劇本 1：新射出機台物理特徵化導入劇本 (Machine Onboarding Playbook)

*   **目的**: 將一台新的實體射出成型機納入數位分身範疇，測量其動力學特徵。
*   **觸發條件**: 廠區引進新機台，或機台進行重大維護（更換螺桿、油壓泵）後 [VERIFIED]。
*   **執行步驟**:
    1.  **機台空射測試 (Dry Run Test)**: 在不裝模具的情況下，控制螺桿以不同設定速度（$10\text{ mm/s}$ 至 $150\text{ mm/s}$）前進，採集螺桿真實加速度與位置曲線。
    2.  **動態特徵識別 (Characteristics Identification)**: 計算螺桿從靜止加速到設定速度的「時間常數 $\tau_s$」與「制動慣性距離」[INFERRED]。
    3.  **特性參數打包**: 將上述物理參數寫入 `machine_profile.json` 格式檔，上傳至 iMolding Hub 資料庫。
    4.  **CAE 連接驗證**: 在 Moldex3D Studio 中選擇該機台 Profile，執行測試流動計算，驗證機台響應延遲是否已被物理嵌入 [VERIFIED]。

---

## 📖 劇本 2：新模具首次試模壓力校準劇本 (Mold Trial Calibration Playbook)

*   **目的**: 在新模具開發完成、進行首次試模時，校準模流模擬的絕對誤差。
*   **觸發條件**: T0/T1 試模階段啟動 [VERIFIED]。
*   **執行步驟**:
    1.  **感測器自檢**: 確認模穴內壓力與溫度感測器接線正確，信號放大器輸出零點校準。
    2.  **基準參數射出**: 使用 Moldex3D 推薦的初始工藝設定（速度、保壓、模溫）射出 5 模，丟棄前 2 模不穩定件，採集後 3 模的模穴壓力時間序列。
    3.  **觸發 iMolding 校準**: 將數據匯入 [chu_digitaltwin_curve_aligner_lab_20260607_v01.py](file:///D:/L3-Academy/OpenFlow3D/chu_digitaltwin_curve_aligner_lab_20260607_v01.py) 運算。
    4.  **品質門檻門禁 (Quality Gate)**: 比對對齊後的 RMSE 誤差。
        *   若 $\text{RMSE} \le 5\text{ MPa}$，則通過驗證，鎖定數位分身模型 [VERIFIED]；
        *   若 $\text{RMSE} > 5\text{ MPa}$，則自動修正 Cross-WLF 材料參數與介面傳熱係數 (HTC)，重新計算直到達標。

---

## 📖 劇本 3：塑料批次物性波動自適應調整劇本 (Material Drift Adaptation Playbook)

*   **目的**: 當使用回收料、或不同批次的塑料導致黏度波動時，快速自動調整製程參數以維持質量。
*   **觸發條件**: 量產過程中成品重量或尺寸超差，或更換原料批次 [VERIFIED]。
*   **執行步驟**:
    1.  **缺陷特徵採集**: 自動檢測成品重量與翹曲變形量。
    2.  **誤差流變反算**: 利用壓力感測器監測波峰壓力的跌落值，觸發黏度反算演算法，判定當前批次塑料的黏度指數漂移量 $\Delta \eta$ [INFERRED]。
    3.  **AI 代理求解**: 調用神經網路 Surrogate Model，在成型窗口內快速搜索能補償該黏度漂移的最優速度與保壓配方。
    4.  **一鍵優化更新**: 將新配方派發至機台，使良率快速回到綠色生產區間。

---

## 📖 劇本 4：產品成型缺陷異常診斷劇本 (Defect Diagnosis Playbook)

*   **目的**: 透過虛實對照曲線，快速定位射出缺陷（如短射或收縮凹陷）的物理根因。
*   **觸發條件**: 生產現場出現缺陷零件 [VERIFIED]。
*   **執行步驟**:
    1.  **曲線提取**: 從 iMolding Hub 拉取當前缺陷模次的壓力和速度實測曲線。
    2.  **理論比對**: 將實測曲線與 Moldex3D 的理論最佳充填壓力曲線進行疊加。
    3.  **根因定位**:
        *   若實測壓力在充填中段急劇上升，但速度骤降 $\rightarrow$ 診斷為模溫過低導致固化層提前封鎖（Frozen Layer Blockage）。
        *   若實測壓力波峰與模擬一致，但後半段保壓壓力大幅滑落 $\rightarrow$ 診斷為澆口過早凍結（Gate Freeze-off）或保壓時間設定不足。
    4.  **處置指令下達**: 依據診斷結果調整模溫控制器設定，或修改螺桿保壓切換位置。

---

## 📖 劇本 5：異常失控防範與安全回滾劇本 (Emergency Rollback Playbook)

*   **目的**: 防止因感測器失效、通訊中斷或演算法出錯，導致派發錯誤配方損壞昂貴的模具或機台。
*   **觸發條件**: 自動校準計算超時、虛實壓力偏差大於 $30\%$、或通訊中斷 [VERIFIED]。
*   **執行步驟**:
    1.  **自動切斷派發鏈 (Interlock Trigger)**: iMolding Hub 立即將配方下傳功能置於鎖定狀態（Lockdown）。
    2.  **控制權交還**: 工業閘道器發送中斷訊號，將射出機控制權完全移交回機台 PLC 本地控制板面。
    3.  **基線配方恢復 (Safety Rollback)**: PLC 自動載入存儲於唯讀記憶體中的安全生產基線配方（Baseline Recipe），確保機台以保守的安全夾模力與低射速低壓運行。
    4.  **人工警報啟動**: 發送 SMS 與電郵通知現場工程師，要求進行硬體排查與人工作業審核。
