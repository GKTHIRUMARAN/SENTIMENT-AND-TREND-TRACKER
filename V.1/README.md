# ⚡ **SENTIMENT-AND-TREND-TRACKER — V.1 Full Build**

> **AI-Powered Real-Time Sentiment, Emotion & Trend Forecasting System (FastAPI + React + ML Models)**
> The evolution of the *Trend Tracker Prototype (V.0)* into a **full-scale analytics engine** with automated ETL, forecasting, memory, and a complete frontend dashboard.

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=brightgreen\&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=blue\&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=yellow\&style=for-the-badge)

---

## 🧠 Overview

**Trend Tracker (V.1)** is the **first complete production-ready version** of an AI-powered text analytics platform capable of transforming raw text into **sentiment**, **emotion**, **topics**, and **trend forecasts**.
Powered by **FastAPI**, **React**, **BERTopic**, **VADER**, **DistilRoBERTa**, and **Prophet**, this full-stack system delivers:

* **Real-time & manual ingestion (CSV/API)**
* **Automated ETL → preprocessing → ML analysis**
* **Sentiment & emotion classification**
* **Topic extraction + forecasting**
* **Memory system for historical summaries**
* **Dashboard UI with charts & KPIs**
* **Persistent logs, vector DB, and model storage**

This version expands the lightweight [V.0](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0) prototype into a **fully functional AI analytics engine**.

---

## 🎯 Core Vision

Build a **scalable, modular, data-driven analytics framework** that can:

* Ingest text from any source (manual, CSV, API)
* Clean, preprocess, and normalize text automatically
* Perform **sentiment**, **emotion**, and **topic modeling**
* Generate **forecasted trend curves**
* Store **history + embeddings** for semantic recall
* Provide a **modern, interactive React dashboard**
* Enable seamless upgrades to real-time social data in **V.2**

---

## ⚙️ System Architecture

```mermaid
flowchart TD
    A[User] -->|Input Text / CSV| B[React Dashboard]
    B -->|POST /api/analyze| C[FastAPI Backend]
    C -->|Ingest| D[Ingestion Module]
    D -->|Clean| E[Preprocessing Layer]
    E -->|Run Models| F[ML Models<br/>(Sentiment, Emotion, BERTopic, Prophet)]
    F -->|Save Results| G[Results Storage<br/>(CSV / DB)]
    G -->|Serve Data| H[Visualization API]
    H -->|Chart JSON| B
    F -->|Store Summary| I[Memory System<br/>(JSON + VectorDB)]
    D -->|Triggered Run| J[ETL Automation Engine]
```

---

## 🧩 Key Components

| Layer               | Technology       | Role                                               |
| :------------------ | :--------------- | :------------------------------------------------- |
| **Frontend**        | React            | Dashboard UI, charts, KPI cards                    |
| **Backend**         | FastAPI          | Ingestion, analysis pipeline, visualization routes |
| **Sentiment Model** | VADER            | Polarity scoring                                   |
| **Emotion Model**   | DistilRoBERTa    | Emotion classification (anger, joy, sadness, etc.) |
| **Topic Modeling**  | BERTopic         | Topic clusters + keywords                          |
| **Forecasting**     | Prophet          | 7-day textual trend prediction                     |
| **Memory Layer**    | JSON + VectorDB  | Query history + semantic recall                    |
| **Logs**            | Logging Module   | Tracks ETL, API errors, analysis steps             |
| **Database**        | SQLAlchemy + SQL | Result storage + optional DB integration           |

---

## 🧱 Folder Structure

```
V.1/
│
├── backend/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── ingest.py
│   │   │   ├── analyze.py
│   │   │   ├── memory.py
│   │   │   ├── visualize.py
│   │   ├── utils/
│   │   │   ├── preprocess.py
│   │   │   ├── sentiment.py
│   │   │   ├── emotion.py
│   │   │   ├── trend.py
│   │   ├── db/
│   │   │   ├── connector.py
│   │   │   └── queries.sql
│   ├── pipeline/
│   │   └── etl_automation.py
│   └── .env
│
├── frontend/
│   └── react_app/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── results/
│
├── models/
│   ├── sentiment_model.pkl
│   ├── emotion_model.pkl
│   └── trend_model.pkl
│
├── memory/
│   ├── memory_store.json
│   └── vector_db/
│
└── logs/
    ├── etl.log
    ├── analysis.log
    └── api.log
```

---

## 📸 Demo Snapshot

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/V.1/Demo/demo%20(1).png" alt="Trend Tracker Dashboard Demo" width="850">
</p>

🔗 **More demo screenshots:**
[https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.1/Demo](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.1/Demo)

---

## ⚡ Backend — FastAPI Core

The backend is the **engine** powering ingestion, preprocessing, model execution, memory management, and visualization APIs.

### 🔧 Main Components

| File / Module       | Description                                            |
| :------------------ | :----------------------------------------------------- |
| `main.py`           | Initializes FastAPI and mounts all route modules       |
| `ingest.py`         | CSV/API ingestion → stored in `data/raw/`              |
| `preprocess.py`     | Text cleaning, normalization, stopwords, lemmatization |
| `sentiment.py`      | VADER sentiment classifier                             |
| `emotion.py`        | DistilRoBERTa-based emotion prediction                 |
| `trend.py`          | BERTopic → Prophet forecasting engine                  |
| `analyze.py`        | Full ML pipeline, saves `results.csv`                  |
| `memory.py`         | Manages memory store and embedding vector DB           |
| `visualize.py`      | Chart-ready JSON for dashboard                         |
| `etl_automation.py` | Complete automated ingestion → analysis cycle          |

### ✅ Backend Highlights

* Fully modular API architecture
* ML pipeline integrated end-to-end
* Persistent memory system
* Visualization-ready response formatting
* Logging for ETL, API, and model execution
* DB-ready structure with SQLAlchemy

---

## 💻 Frontend — React Dashboard

A clean, analytics-focused interface for interacting with the backend.

### ✨ UI Features

* Input text page
* KPI cards for sentiment & emotion
* Charts for emotion, sentiment, topics
* BERTopic clusters
* Prophet-based forecast graph
* History view (memory system)
* Responsive and modern layout

### 🧩 Directory Snapshot

```
frontend/
└── react_app/
    ├── src/
    ├── public/
    └── package.json
```

---

## 🧰 Environment Setup

### **.env (Backend)**

```bash
DB_URL=
API_KEYS=
MODEL_PATHS=
```

### **Backend Run**

```bash
uvicorn backend.api.main:app --reload
```

### **Frontend Run**

```bash
cd frontend/react_app
npm install
npm run dev
```

### **Access in Browser**

```
http://localhost:5173
```

---

## ✅ Current Capabilities

| Feature                   | Status        |
| :------------------------ | :------------ |
| Sentiment Analysis        | ✅ Complete    |
| Emotion Detection         | ✅ Complete    |
| Topic Modeling (BERTopic) | ✅ Complete    |
| Forecasting (Prophet)     | ✅ Working     |
| Automated ETL             | ✅ Functional  |
| Memory System             | ✅ Active      |
| FastAPI Backend           | ✅ Stable      |
| React Dashboard           | ✅ Live        |
| Logging System            | ✅ Enabled     |
| Vector DB Support         | ✅ Implemented |

---

## 🔮 Future Roadmap

| Goal                    | Description                                   |
| :---------------------- | :-------------------------------------------- |
| **Real-time API feeds** | Twitter/X, YouTube, Reddit integration        |
| **GPU acceleration**    | Faster ML inference                           |
| **RAG-based insights**  | Knowledge retrieval for contextual analysis   |
| **UI upgrades**         | More charts, animations, dark mode            |
| **Dockerization**       | Containerized deployment                      |
| **Cloud hosting**       | Backend → Render / Railway; Frontend → Vercel |

---

## 🧠 Lessons Learned

* BERTopic + Prophet gives lightweight yet powerful forecasting
* Logs dramatically improve debugging and pipeline monitoring
* Memory system increases user context awareness
* Modular code structure allows fast scaling to V.2
* React + FastAPI is ideal for dashboard-style ML apps

---

## 📜 Project Links

| Resource               | Link                                                                                                                                                           |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🏠 **Main Repository** | [https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER)                                     |
| 📂 **V.0 Folder**      | [https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0)         |
| ⚡ **V.1 Folder**       | [https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.1](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.1)         |
| 📜 **License**         | [https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/LICENSE](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/LICENSE) |

---

## 🧩 How It Fits in the Whole Project

**V.1** is the **first fully implemented version** of the Trend Tracker system, evolving from the foundational prototype of [V.0](../V.0/README.md).
It transforms an idea into a **production-ready multi-model analytics engine**, serving as the base for:

* Real-time social media tracking
* Multi-source data aggregation
* Live forecasting and alerting
* Full RAG + Vector DB integrations in V.2

> 🌱 The foundation is complete — V.2 will bring real-time intelligence.

[⬅ Back to Main README](../README.md)

---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *Aspiring Data Scientist & Analyst | AIML Developer*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)

---

