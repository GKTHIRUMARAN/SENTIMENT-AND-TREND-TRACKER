# 🧩 SENTIMENT-AND-TREND-TRACKER — V.0 Prototype Build

> **End-to-End Sentiment Analysis & Trend Visualization (Streamlit + scikit-learn Prototype)**  
> The foundation of the *Intelligent Build — Real-Time Sentiment & Trend Tracker.*

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=yellow&style=for-the-badge)

---

## 🧠 Overview

**SENTIMENT-AND-TREND-TRACKER (V.0)** marks the **first working prototype** of the full-scale *Intelligent Sentiment & Trend Tracking System.*  
This version demonstrates the complete **end-to-end pipeline** — from **data ingestion and cleaning** to **model training, prediction, and visualization** — implemented in **Python + Streamlit**.

The prototype establishes the **technical backbone** for the upcoming intelligent build that will integrate real-time APIs, database automation, and advanced trend analytics.

---

## 🎯 Objective

To build a **portfolio-grade, offline functional prototype** capable of:

- Ingesting and cleaning textual datasets (reviews, notes, or feedback).
- Training and deploying sentiment analysis models locally.
- Predicting and visualizing emotion/sentiment trends interactively.
- Logging and tracing every stage in a reproducible workflow.

---

## ⚙️ Tech Stack

| Layer | Tool / Library | Description |
| :---- | :-------------- | :----------- |
| **Language** | Python 3.10+ | Core scripting |
| **Data Handling** | pandas, numpy | Data manipulation |
| **Preprocessing** | nltk, regex | Text cleaning & tokenization |
| **ML / NLP** | scikit-learn, joblib | Sentiment classification |
| **Visualization** | Streamlit, matplotlib, plotly | Interactive dashboard |
| **Logging** | Python `logging` | Stage-wise pipeline logging |
| **Config** | dotenv, JSON | Environment and configuration setup |

---

## 🧩 Core Features

- ⚙️ **ETL Pipeline:** Raw data → Cleaned dataset → Model-ready inputs  
- 🧠 **Machine Learning:** TF-IDF vectorization + Logistic Regression  
- 💾 **Persistent Artifacts:** Saves processed data and trained model (`model.pkl`)  
- 📊 **Interactive Dashboard:** Streamlit interface for real-time insight display  
- 🧰 **Traceability:** Logs every operation across ingestion, cleaning, and modeling  
- 🚀 **Modular Design:** Each component runs independently for testing or extension  

---

## 🧱 Prototype Architecture

```mermaid
flowchart LR
    A[User / CSV File] --> B[Data Ingestion]
    B --> C[Data Cleaning & Preprocessing]
    C --> D[Model Training]
    D --> E[Prediction & Labeling]
    E --> F[Streamlit Dashboard]
    F -->|Visual Output| G[Sentiment & Trend Insights]
````

---

## 📂 Folder Structure

```
│   .env
│   .gitignore
│   app.py
│   requirements.txt
│
├───config
│       db_config.json
│
├───data
│       raw_data.csv
│       cleaned_dataset.csv
│
├───logs
│       data_cleaning.log
│       ingestion.log
│       model_training.log
│       model_prediction.log
│
├───models
│       model.pkl
│
├───pipeline
│       run_pipeline.py
│
└───scripts
    ├───ingestion
    │       data_ingestion.py
    ├───preprocessing
    │       data_cleaning.py
    └───model
            model_training.py
            model_prediction.py
```

---

## 💡 Workflow Steps

1. **Data Ingestion**

   * Loads raw CSV dataset into `/data/raw_data.csv`.
   * Logs ingestion steps and dataset info.

2. **Preprocessing**

   * Cleans text (stopwords, punctuation, case normalization).
   * Outputs `/data/cleaned_dataset.csv`.

3. **Model Training**

   * Uses TF-IDF + Logistic Regression for classification.
   * Saves model to `/models/model.pkl`.

4. **Prediction & Evaluation**

   * Runs predictions using the trained model.
   * Logs accuracy metrics in `/logs/model_prediction.log`.

5. **Visualization (Streamlit Dashboard)**

   * Displays sentiment breakdown, trend charts, and data filters.
   * Offers CSV upload and analysis refresh options.

---

## 🧰 Key Scripts

| File                  | Role                                                         |
| :-------------------- | :----------------------------------------------------------- |
| `app.py`              | Streamlit dashboard; connects data, model, and visualization |
| `data_ingestion.py`   | Loads and saves raw datasets                                 |
| `data_cleaning.py`    | Prepares and cleans text data                                |
| `model_training.py`   | Trains and serializes sentiment model                        |
| `model_prediction.py` | Generates predictions and logs output                        |
| `run_pipeline.py`     | Automates ingestion → preprocessing → training sequence      |

---

## 🧠 Example Code Snippet

```python
import streamlit as st
import pandas as pd
import joblib

# Load trained model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("Sentiment & Trend Tracker — Prototype (V.0)")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    text = data["review_text"]
    X = vectorizer.transform(text)
    data["predicted_sentiment"] = model.predict(X)
    st.write(data.head())
    st.bar_chart(data["predicted_sentiment"].value_counts())
```

---

## 📊 Dashboard Output Example

> **Sentiment Breakdown (Sample):**
>
> * Positive: 61%
> * Neutral: 27%
> * Negative: 12%

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/V.0/demo/Screenshot%202025-09-21%20084602.png" alt="Sentiment & Trend Tracker Dashboard" width="800">
</p>

---

## 🧠 Internal Logic

1. **Initialize pipeline:** Run `run_pipeline.py` for end-to-end execution.
2. **Load configuration:** `.env` and `db_config.json` for environment setup.
3. **Run Streamlit dashboard:** Launch `app.py` for visualization and interaction.
4. **Monitor logs:** Review `/logs` for traceable workflow stages.
5. **Model reuse:** Use `model.pkl` for retraining or API integration in future builds.

---

## 🚀 Future Goals (Towards V.1)

| Feature        | Upgrade Path                                                  |
| :------------- | :------------------------------------------------------------ |
| **Backend**    | Integrate FastAPI for real-time analysis                      |
| **Database**   | Add MySQL for persistent trend data                           |
| **Frontend**   | React-based rich visualization layer                          |
| **Retrieval**  | Introduce RAG or semantic search for insights                 |
| **Automation** | Streamline ingestion and scheduling via pipeline orchestrator |

---

## ✅ Outcome

The **V.0 prototype** validates a fully operational, modular data science workflow — combining:

* Data engineering (ETL)
* NLP preprocessing and sentiment modeling
* Visual analytics via Streamlit
* Structured, logged, and reproducible workflow

This version serves as the **foundation** for the *Intelligent Build (V.1)* — where real-time data, APIs, and dynamic dashboards will be introduced.

---

## 🔗 Project Links

| Resource               | Link                                                                                                |
| :--------------------- | :-------------------------------------------------------------------------------------------------- |
| 🏠 **Main Repository** | [SENTIMENT-AND-TREND-TRACKER](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER)          |
| ⚡ **License**          | [MIT License](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/LICENSE)        |

---

## 🧩 How It Fits in the Whole Project

This **V.0 module** is the **foundation layer** of the full system — establishing data flow, model logic, and visualization design.
It feeds directly into the **Intelligent Build (V.1)**, where automation, APIs, and live trend analysis will evolve.

> 🪴 Think of this version as the seed — everything after it grows from here.

[⬅ Back to Main README](../README.md)

---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech — Artificial Intelligence & Data Science*  
🌍 *Coimbatore, India*  
💼 *Full-Stack AI Developer | Data Scientist | System Architect*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)
