# Sentiment-and-Trend-Tracker

## An **end-to-end data project** that integrates **MySQL, Jupyter, Power BI, and Streamlit** to track sentiment trends in real-time using AI/ML models. This project demonstrates a complete workflow — from **data ingestion, preprocessing, ML modeling, visualization, and deployment**.
---

## 🔹 Features
- **Database Integration**: Stores dataset in MySQL for structured access.
- **Data Preprocessing**: Jupyter Notebook workflows for cleaning and feature engineering.
- **Machine Learning**: Sentiment classification using a trained ML model.
- **Visual Analytics**:  
  - Power BI dashboard for business-friendly insights.  
  - Streamlit web app for interactive exploration.  
- **Trend Tracking**: Monitor sentiment trends over time with dynamic charts.  
- **Prediction Box**: Try your own text and get real-time sentiment prediction.
---

## ⚙️ Tech Stack
- Programming: Python (Pandas, Scikit-learn, Seaborn, Altair, Plotly)
- Database: MySQL (via SQLAlchemy)
- Visualization: Power BI, Matplotlib, Seaborn, Altair
- Web App: Streamlit
- Version Control: Git & GitHub

## 🚀 Getting Started
## 1️⃣ Clone the Repo
git clone https://github.com/GKTHIRUMARAN/SENTIMENT-AND-TREND-TRACKER.git  
cd trend-tracker

## 2️⃣ Setup Virtual Environment
python -m venv venv\
venv\Scripts\activate      # Windows\
pip install -r requirements.txt

## 3️⃣ Setup MySQL
Create database:\
CREATE DATABASE trend_tracker;\
Run SQL script:\
SOURCE sql/Track_data.sql;

## 4️⃣ Train the Model
Open the Jupyter Notebooks (notebooks/) step by step and generate model.pkl.

## 5️⃣ Run Streamlit App
streamlit run app.py

## 📊 Power BI Dashboard
- The Power BI dashboard provides:
- Sentiment distribution
- Land-based segmentation
- Temporal sentiment trends
- Dataset vs model prediction comparisons

## 🔮 Future Enhancements
- Integrate live Twitter/Reddit APIs for real-time streaming data.
- Deploy Streamlit app on cloud platforms (Heroku, Streamlit Cloud, or GCP).
- Experiment with transformer-based models (BERT, RoBERTa).
- Add CI/CD workflows for automated model retraining.

## 👤 Author
GK Thirumaran\
🎓 B.Tech Artificial Intelligence and Data Science\
🌍 Coimbatore, Tamil Nadu, India\
💼 Aspiring Data Scientist & Analyst | AIML Developer\
🔗 [Linkedin](https://www.linkedin.com/in/thirumarangk-ai) | [Porfolio](https://maranthiru180.wixsite.com/my-site)
