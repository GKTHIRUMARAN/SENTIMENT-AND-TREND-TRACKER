# 🧠 SENTIMENT-AND-TREND-TRACKER

> **End-to-End Real-Time Sentiment & Trend Tracker — Intelligent Build**

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=yellow&style=for-the-badge)

---

## 🧭 Overview

**SENTIMENT & TREND TRACKER** is a professional-grade **AI-driven analytics platform** that performs real-time **sentiment, emotion, and trend detection** across datasets or user inputs.  
It represents a complete **end-to-end data science system**, integrating **ETL**, **machine learning**, **dashboard visualization**, and **traceable logging** — all within one unified architecture.

This repository hosts the **Intelligent Build (v2 base)** of the system, evolved from the **V.0 prototype** that established the foundation of the ETL + ML pipeline.

---

## 🎯 Project Summary

| Version | Description | Key Tech |
| :------ | :----------- | :-------- |
| [V.0 — Prototype](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0) | Streamlit-based sentiment analysis dashboard demonstrating ETL, ML, and visualization. | Python, Streamlit, scikit-learn |
| V.1 / V.2 — Intelligent Build *(Planned)* | Real-time API integration with automated ingestion and trend analytics. | FastAPI, MySQL, Plotly, React *(future)* |

---

## 🧩 Core Features

- ⚙️ **End-to-End Pipeline:** Ingestion → Preprocessing → Modeling → Prediction → Visualization  
- 🧠 **ML-Powered Insights:** Detects sentiment and emotion from text data  
- 📊 **Interactive Dashboards:** Visualize sentiment distribution and temporal trends  
- 💾 **Structured Data Flow:** Clear raw → cleaned → processed → model stages  
- 🧰 **Traceable Logging:** Every operation logged for reproducibility  
- 🚀 **Modular Architecture:** Expandable into real-time and cloud-ready builds  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User / Data Source] -->|CSV / Input Stream| B[Data Ingestion]
    B --> C[Data Cleaning & Preprocessing]
    C --> D[ML Model Training]
    D --> E[Model Prediction]
    E --> F[Streamlit Dashboard]
    F -->|Visualization| G[Sentiment & Trend Insights]
````

---

## ⚙️ Technical Stack

| Layer             | Technology                    | Purpose                                  |
| :---------------- | :---------------------------- | :--------------------------------------- |
| **Language**      | Python 3.10+                  | Core scripting and orchestration         |
| **Data Handling** | pandas, numpy                 | Dataset management and preprocessing     |
| **ML / NLP**      | scikit-learn, nltk, joblib    | Sentiment model training and prediction  |
| **Visualization** | Streamlit, matplotlib, plotly | Dashboard and insights                   |
| **Logging**       | Python `logging` module       | Traceability across pipeline             |
| **Config / Env**  | dotenv, JSON                  | Configuration and credentials management |

---

## 📁 Repository Overview

| Folder / File      | Description                                                |
| :----------------- | :--------------------------------------------------------- |
| `config/`          | Database and configuration files                           |
| `data/`            | Contains raw and cleaned datasets                          |
| `logs/`            | Stage-wise log files (ingestion, cleaning, model training) |
| `models/`          | Trained model artifacts                                    |
| `pipeline/`        | Execution script to run full data + ML pipeline            |
| `scripts/`         | Modular ETL, preprocessing, and model scripts              |
| `app.py`           | Streamlit app for visualizing sentiment & trend insights   |
| `requirements.txt` | Dependencies list for reproducible setup                   |

---

## 🔍 Workflow Summary

1. **Data Ingestion** — Load raw text data from CSV or manual input.
2. **Preprocessing** — Clean, tokenize, and normalize textual data.
3. **Model Training** — Train Logistic Regression or Naive Bayes model.
4. **Prediction** — Generate sentiment or emotion labels.
5. **Visualization** — Present trends, sentiment breakdowns, and summaries.

---

## 📊 Example Output

> **Sentiment Overview:**
>
> * Positive: 62%
> * Neutral: 23%
> * Negative: 15%

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/V.0/demo/Screenshot%202025-09-21%20084602.png" alt="Sentiment & Trend Tracker Demo" width="800">
</p>

---

## 🧠 Prototype Foundation (V.0)

The **V.0 version** establishes the **complete offline ETL–ML–Visualization pipeline**, serving as the technical base for future intelligent builds.

Key functionalities:

* Local data ingestion and preprocessing.
* TF-IDF vectorization and ML classification.
* Streamlit-based visualization dashboard.
* Logging for each operational stage.

📦 **Access here:** [V.0 — Prototype Build](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0)

---

## 🪐 Project Ecosystem

| Module                                | Description                                                 | Link                                                                                    |
| :------------------------------------ | :---------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| 🧩 **Prototype Build (V.0)**          | Streamlit dashboard demonstrating ETL → ML → Visualization. | [Open → V.0](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0) |
| ⚡ **Intelligent Build (V.1 Planned)** | Real-time API + database + React-based frontend expansion.  | ⏳ Coming Soon                                                                           |

---

## 📜 License

Licensed under the [MIT License](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/LICENSE).

---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech — Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *Aspiring Data Scientist & Analyst | AIML Developer*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)
---
```
