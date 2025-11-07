# 🧠 SENTIMENT-AND-TREND-TRACKER

> **End-to-End AI-Powered Sentiment & Trend Analysis System**  
> Intelligent data pipeline integrating ETL, ML, and visualization.

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER?color=yellow&style=for-the-badge)

---

## 🧩 Overview

**SENTIMENT-AND-TREND-TRACKER** is a portfolio-grade **AI data system** demonstrating the full cycle of **text ingestion → cleaning → model prediction → visualization**.  
It transforms raw text data (reviews, feedback, notes) into clear, actionable **sentiment and trend insights** through a **Streamlit dashboard** powered by **Python & ML models**.

Version (**V.0**) establishes the **complete working prototype**, forming the foundation for the upcoming **real-time intelligent build (V.1)**.

---

## 🎯 Project Summary

| Version | Description | Key Tech |
| :------ | :----------- | :------- |
| [V.0 — Prototype](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0) | Full end-to-end sentiment analysis pipeline with ML + Streamlit UI. | Python, scikit-learn, Streamlit |
| V.1 — (Upcoming) | Real-time version with FastAPI backend and automated ingestion. | FastAPI, MySQL, Plotly, Docker |

---

## ⚙️ Core Features

- 🔹 **Data Pipeline:** Automated ingestion and cleaning with logs  
- 🔹 **ML Pipeline:** TF-IDF + Logistic Regression / Naive Bayes model  
- 🔹 **Interactive Dashboard:** Streamlit-based visualization layer  
- 🔹 **Modular Scripts:** Each step isolated for reuse and scaling  
- 🔹 **Logging System:** Full traceability across ETL and model stages  
- 🔹 **Expandable Design:** Prepped for real-time & API integration  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[Raw Text Data] -->|CSV Input| B[Data Ingestion]
    B -->|Clean & Normalize| C[Preprocessing]
    C -->|TF-IDF Vectorization| D[Model Training]
    D -->|model.pkl| E[Model Prediction]
    E -->|Sentiment Results| F[Streamlit Dashboard]
    F -->|Interactive Visualization| G[User Insights]
````

---

## 📚 Technical Stack

| Layer             | Tools / Libraries           | Purpose                       |
| :---------------- | :-------------------------- | :---------------------------- |
| **Language**      | Python 3.10+                | Core development              |
| **Data Handling** | pandas, numpy               | Data ingestion & manipulation |
| **Preprocessing** | nltk, re, string            | Text cleaning                 |
| **ML / NLP**      | scikit-learn, joblib        | Sentiment classification      |
| **Visualization** | matplotlib, seaborn, plotly | Data visualization            |
| **App Framework** | Streamlit                   | Interactive web UI            |
| **Logging**       | Python `logging`            | Process traceability          |
| **Config**        | dotenv, JSON                | Secure credentials & setup    |

---

## 📊 Workflow Summary

1. **Ingest Data** → Load raw CSVs
2. **Clean & Preprocess** → Tokenize, remove stopwords
3. **Train Model** → TF-IDF + classifier
4. **Predict Sentiment** → Generate labeled results
5. **Visualize Trends** → Streamlit dashboard

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/V.0/demo/Screenshot%202025-09-21%20084602.png" width="800" alt="Trend Tracker Dashboard Demo">
</p>

---

## 🧠 Example Output

| Input Text                             | Cleaned                    | Predicted Sentiment |
| :------------------------------------- | :------------------------- | :------------------ |
| “Service was great, I’ll return soon!” | service great return soon  | **Positive**        |
| “Food was average but slow delivery.”  | food average slow delivery | **Neutral**         |
| “Terrible experience.”                 | terrible experience        | **Negative**        |

---

## 🚀 Outcome

✅ Fully functional **end-to-end prototype** proving your ability to:

* Design data & ML pipelines
* Build reusable architecture
* Integrate app-level visualization
* Implement traceable logging

This serves as the **base layer** for your **V.1 intelligent build**, introducing real-time data flow, backend APIs, and database integration.

---

## 🪐 Project Ecosystem

| Module                       | Description                                                       | Link                                                                                    |
| :--------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| 🧩 **Prototype Build (V.0)** | Streamlit-based sentiment & trend tracker — foundational version. | [Open → V.0](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/tree/main/V.0) |

---

## 📜 License

Licensed under the [MIT License](https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER/blob/main/LICENSE).

---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech — Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *AI & Data Science Developer | End-to-End System Builder*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)
