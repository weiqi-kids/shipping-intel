# Shipping Intel - 航運供應鏈情報追蹤

## 專案概述

產業：航運
追蹤公司：14 家
追蹤主題：4 個

### 追蹤範圍

**上游** (4 家)
- HD Korea Shipbuilding 韓國造船海洋, HD한국조선해양 (009540.KS)
- Samsung Heavy Industries 三星重工, 삼성중공업 (010140.KS)
- Hanwha Ocean 韓華海洋, 한화오션 (042660.KS)
- China State Shipbuilding 中國船舶, 中船 (600150.SS)

**中游** (10 家)
- Evergreen Marine 長榮海運, 長榮 (2603.TW)
- Yang Ming Marine 陽明海運, 陽明 (2609.TW)
- Wan Hai Lines 萬海航運, 萬海 (2615.TW)
- A.P. Moller-Maersk 馬士基, 快桅 (MAERSK-B.CO)
- Hapag-Lloyd 赫伯羅特 (HLAG.DE)
- ZIM Integrated Shipping (ZIM)
- COSCO Shipping 中遠海控, 中遠 (1919.HK)
- U-Ming Marine 裕民航運, 裕民 (2606.TW)
- Wisdom Marine Lines 慧洋海運, 慧洋 (2637.TW)
- Star Bulk Carriers (SBLK)

### 主題
- 貨櫃運價
- 散裝運價
- 造船訂單
- 港口壅塞

---

## 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **新聞爬蟲** | 涵蓋 14 家公司 | 待建置 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | ✅ 從模板複製 |
| **報告生成** | 每日報告、7 日報告 | ✅ 從模板複製 |
| **前端** | Dashboard | ✅ 從模板複製 |

---

## 資料夾結構

```
shipping-intel/
├── lib/                        # 規則引擎
│   ├── __init__.py
│   ├── matcher.py              # 關鍵字匹配
│   ├── sentiment.py            # 情緒分析
│   ├── scorer.py               # 重要性評分
│   └── anomaly.py              # 異常偵測
│
├── scripts/                    # 執行腳本
│   ├── fetch_news.py           # 整合抓取
│   ├── fetch_stocks.py         # 股價抓取
│   ├── enrich_event.py         # 事件標註
│   ├── generate_metrics.py     # 每日指標
│   ├── detect_anomalies.py     # 異常偵測
│   ├── generate_daily.py       # 每日報告
│   ├── generate_7d_report.py   # 7 日報告
│   ├── sync_to_frontend.py     # 同步事件到前端
│   └── update_baselines.py     # 更新基準線
│
├── configs/                    # 設定檔
│   ├── companies.yml           # 公司 + 上下游關係
│   ├── topics.yml              # 主題 + 關鍵字
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   └── anomaly_rules.yml       # 異常偵測規則
│
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件 (JSONL)
│   ├── metrics/                # 每日指標
│   ├── normalized/             # 股價資料
│   ├── baselines/              # 歷史基準線
│   ├── financials/             # 財務數據
│   ├── holders/                # 股東資料
│   └── fund_flow/              # 資金流向
│
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
│
├── site/
│   ├── index.html              # Dashboard
│   └── data/                   # 前端資料
│
└── CLAUDE.md
```

---

## 標準流程

```
fetch_news.py
    │
    ├─→ data/raw/{date}/news.jsonl    (原始抓取資料)
    │
    └─→ enrich_event.py
            │
            └─→ data/events/{date}.jsonl  (標準格式，唯一資料源)
                    │
            ┌───────┴───────────────┐
            │                       │
      sync_to_frontend.py     generate_metrics.py
            │                       │
            │                 data/metrics/{date}.json
            │                       │
            │                 generate_7d_report.py
            │                       │
            │                 reports/7d/{date}.json
            │                       │
      site/data/events.json   site/data/reports/7d/{date}.json
```

---

## 快速啟動

```bash
cd repos/shipping-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 8000 -d site

# 瀏覽器開啟
open http://localhost:8000
```

## 手動執行流程

```bash
source .venv/bin/activate
python scripts/fetch_news.py           # 抓取新聞
python scripts/enrich_event.py         # 標註事件
python scripts/generate_metrics.py     # 計算指標
python scripts/generate_7d_report.py   # 7 日報告
python scripts/sync_to_frontend.py     # 同步前端
```
