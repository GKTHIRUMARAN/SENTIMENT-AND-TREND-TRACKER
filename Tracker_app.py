import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import numpy as np
import altair as alt
import pickle

st.set_page_config(page_title="Sentiment & Trend Tracker", layout="wide")

# =========================
# DB CONNECTION
# =========================
engine = create_engine("mysql+mysqlconnector://root:goku..123@localhost/trend_tracker")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_sql("SELECT * FROM trend_data", con=engine)
    return df

df = load_data().copy()

# =========================
# ADD RANDOM DATE COLUMN (only once)
# =========================
if "date" not in df.columns or df["date"].isnull().all():
    df["date"] = pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-03-01", "2025-09-01"), 
            size=len(df)
        )
    )

# =========================
# PAGE CONFIG
# =========================
st.title("📊 Real-Time Sentiment & Trend Tracker")

# =========================
# FILTERS
# =========================
lands = st.multiselect("🌍 Select Land", options=df['land'].unique(), default=df['land'].unique())
df_filtered = df[df['land'].isin(lands)].copy()

# =========================
# DASHBOARD VISUALS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Distribution (ML Prediction)")
    fig, ax = plt.subplots()
    sns.countplot(x="ml_predicted_emotion", data=df_filtered, palette="coolwarm", ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Dataset vs ML Predictions")
    fig, ax = plt.subplots()
    sns.countplot(x="emotion", hue="ml_predicted_emotion", data=df_filtered, ax=ax)
    st.pyplot(fig)

# =========================
# Sentiment Trend Over Time
# =========================
st.subheader("📈 Sentiment Trend Over Time")

df_filtered["date"] = pd.to_datetime(df_filtered["date"], errors="coerce")
df_filtered = df_filtered.sort_values("date")

trend_chart = (
    alt.Chart(df_filtered)
    .mark_line(point=True)
    .encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("count()", title="Count"),
        color=alt.Color("ml_predicted_emotion", title="Sentiment"),
        tooltip=["date:T", "ml_predicted_emotion:N", "count()"]
    )
    .properties(width=700, height=400)
    .interactive()
)

st.altair_chart(trend_chart, use_container_width=True)

# =========================
# RAW DATA
# =========================
st.subheader("🔎 Raw Data Preview")
st.dataframe(df_filtered.head(20))

# =========================
# PREDICTION BOX
# =========================
st.subheader("✍️ Try Your Own Text")

try:
    vectorizer, model = pickle.load(open("model.pkl", "rb"))

    user_input = st.text_area("Enter text for sentiment analysis:")

    if st.button("Predict Sentiment"):
        if user_input.strip():
            vec = vectorizer.transform([user_input])
            prediction = model.predict(vec)[0]
            st.success(f"Predicted Emotion: **{prediction}**")
        else:
            st.warning("Please enter some text before predicting.")

except Exception as e:
    st.error("⚠️ Model file not found. Please train model in Jupyter Notebook and save as 'model.pkl'.")
    st.code("pickle.dump((vectorizer, model), open('model.pkl','wb'))")
