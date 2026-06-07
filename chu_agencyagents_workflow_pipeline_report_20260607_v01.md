# 📚 Report 2: Workflow Engineering & Execution Pipeline Design [VERIFIED]
> **文件編號**: `chu_agencyagents_workflow_pipeline_report_20260607_v01.md`  
> **專案代號**: `L3-Zack` | **領域**: `chu` (教學與實驗) | **等級**: 專家級 (Senior workflow & Process Engineer)

本報告對 `agency-agents` 的 60 個 Workflows、60 個 Skills 與 60 個 Playbooks 進行結構化分類，並提供一個標準的多智能體 Pipeline 執行管道設計藍圖。

---

## 1. Top 60×3 (Workflows, Skills, Playbooks) 系統化分類 [VERIFIED]

為了高效利用這套龐大的資產，我們將 180 個萃取項目歸納至以下結構矩陣中：

### 1.1 60 大工作流 (Workflows) 分類 [VERIFIED]
*   **A. 基礎架構工作流 (1-10)**: 包含 Git 分支規劃、環境容器化、安全稽核設定。
*   **B. 軟體工程工作流 (11-20)**: 前後端 API 對接、CI/CD 自動化部署、資料庫遷移。
*   **C. 產品設計工作流 (21-30)**: 用戶訪談反饋合成、Figma 變更追蹤、設計標記 (Tokens) 生成。
*   **D. 行銷推廣工作流 (31-40)**: 社群媒體排程、App Store 關鍵字優化、SEO 稽核。
*   **E. 邊緣與空間計算工作流 (41-50)**: macOS Metal 渲染、visionOS 空間交互建模。
*   **F. 團隊營運工作流 (51-60)**: Sprint 會議摘要、預算追蹤、合規報告生成。

### 1.2 60 大技能 (Skills) 分類 [VERIFIED]
*   **A. 技術實作技能 (1-15)**: Python/Rust 代碼改寫、Docker 鏡像優化、API 測試撰寫。
*   **B. 數據分析技能 (16-30)**: 流失率預測、日誌異常偵測、A/B 測試顯著性評估。
*   **C. 視覺創意技能 (31-45)**: Midjourney 提示詞生成、UI 微動畫設計、排版佈局。
*   **D. 管理協調技能 (46-60)**: 甘特圖繪製、專案阻礙 (Blockers) 排除、合規文件審查。

### 1.3 60 大劇本 (Playbooks) 週期分類 [VERIFIED]
對照 NEXUS 的 7 階段生命週期，定義標準作業劇本：
*   **Phase 0 (1-10)**: 新專案探索、市場痛點分析劇本。
*   **Phase 1 (11-20)**: 系統架構定義、技術選型評估劇本。
*   **Phase 2 (21-30)**: 代碼腳手架建立、API 規格書撰寫劇本。
*   **Phase 3 (31-40)**: 雙週 Sprint 敏捷衝刺、代碼重構劇本。
*   **Phase 4 (41-48)**: 大規模集成測試、回歸測試劇本。
*   **Phase 5 (49-54)**: 灰度發佈 (Canary)、上線監控劇本。
*   **Phase 6 (55-60)**: 災難復原、技術債務清理劇本。

---

## 2. 實戰：經典多智能體執行管道 (Multi-Agent Pipeline Case Study)

以下為實現 **「空間探索 visionOS App 開發與上線」** 的多智能體協同管道設計。

```mermaid
flowchart TD
    subgraph Phase_1_Strategize ["Phase 1: 策略與架構"]
        Arch["1. 系統架構師 (Backend Architect)"] -->|輸出 API Spec| UI_Des["2. XR 介面設計師 (XR Interface Architect)"]
    end
    subgraph Phase_3_Build ["Phase 3: 敏捷開發與測試環路"]
        UI_Des -->|輸出 Figma/Metal 規格| Dev["3. 空間編程專家 (visionOS Spatial Engineer)"]
        Dev -->|輸出 Swift 代碼| QA["4. 實效驗證器 (Reality Checker)"]
        QA -->|測試失敗 (Bug)| Dev
    end
    subgraph Phase_4_Harden ["Phase 4: 品保與部署"]
        QA -->|測試通過 (PASS)| DevOps["5. 自動化部署工程師 (DevOps Automator)"]
        DevOps -->|輸出 Docker/GitHub Actions| PM["6. 專案牧羊人 (Project Shepherd)"]
    end
    PM -->|驗證發佈條件| Deliver["正式上線交付"]
```

### 2.1 管道執行詳解 [INFERRED]

#### 步驟 1：系統架構與介面定義 (Phase 1)
*   **啟動 Agent**: `Backend Architect` 與 `XR Interface Architect` [VERIFIED]。
*   **輸入數據**: 專案需求書、3D 空間網格限制。
*   **過程**: 架構師定義後端 REST API 規範；空間介面設計師將 API 欄位對映至三維懸浮視窗組件。
*   **品質閘門 (Quality Gate)**: 產出之 API 規範必須通過 `API Tester` 模擬驗證，確保無語義漏洞 [VERIFIED]。

#### 步驟 2：空間開發與測試環路 (Phase 3)
*   **啟動 Agent**: `visionOS Spatial Engineer` 與 `Reality Checker` [VERIFIED]。
*   **輸入數據**: 對齊的 API 規格、3D 空間佈局圖。
*   **過程**: 編程工程師以 Swift / Metal 撰寫渲染與交互代碼；實效驗證器模擬手勢與眼動追踪輸入，進行崩潰測試。
*   **回饋機制**: 若出現渲染延遲 (Frame Drop > 10%)，驗證器拋回代碼並附帶基準報告，要求優化 Metal 緩衝區。

#### 步驟 3：自動化部署與專案驗收 (Phase 4)
*   **啟動 Agent**: `DevOps Automator` 與 `Project Shepherd` [VERIFIED]。
*   **過程**: 自動化工程師配置 GitHub Actions 管線，將程式包裝至 visionOS 模擬測試器中；專案牧羊人檢查所有相依任務 (WBS) 是否皆標註為已完成。
*   **最終輸出**: 通過安全性與合規性檢驗的 visionOS App 安裝包與上架清單。
