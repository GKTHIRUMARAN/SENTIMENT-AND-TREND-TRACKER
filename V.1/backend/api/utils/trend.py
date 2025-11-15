"""
trend.py — Topic Modeling + Trend Forecasting (NeuralProphet Version)
=====================================================================
Modules:
    - BERTopic for topic extraction
    - NeuralProphet for Windows-friendly forecasting
"""

from bertopic import BERTopic
from neuralprophet import NeuralProphet
import pandas as pd
from loguru import logger
import os
from dotenv import load_dotenv

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
RESULT_DATA_PATH = os.getenv("DATA_RESULT_PATH", "data/results/")
os.makedirs(RESULT_DATA_PATH, exist_ok=True)


# ---------------------------------------------------------
# 1️⃣ Topic Extraction (BERTopic)
# ---------------------------------------------------------
def extract_topics(text_list):
    try:
        logger.info("🧠 Running BERTopic topic modeling...")

        topic_model = BERTopic(verbose=False)
        topics, _ = topic_model.fit_transform(text_list)

        topics_info = topic_model.get_topic_info()

        topics_info.to_json(
            os.path.join(RESULT_DATA_PATH, "topics.json"),
            orient="records",
            indent=4
        )

        logger.info("📑 Topics saved → results/topics.json")
        return topics_info

    except Exception as e:
        logger.error(f"❌ Topic extraction failed: {e}")
        return pd.DataFrame()


# ---------------------------------------------------------
# 2️⃣ Trend Forecasting (NeuralProphet — Windows SAFE)
# ---------------------------------------------------------
def forecast_trend(df, date_col="created_at", value_col="count", periods=7):
    try:
        logger.info("📈 Running NeuralProphet forecasting...")

        df_np = df[[date_col, value_col]].rename(columns={date_col: "ds", value_col: "y"})

        model = NeuralProphet(
            n_forecasts=1,
            yearly_seasonality=False,
            weekly_seasonality=True,
            daily_seasonality=True
        )

        model.fit(df_np, freq="D")

        future = model.make_future_dataframe(df_np, periods=periods)
        forecast = model.predict(future)

        forecast_tail = forecast[["ds", "yhat1"]].tail(periods)
        forecast_tail.rename(columns={"yhat1": "yhat"}, inplace=True)

        forecast_tail.to_csv(
            os.path.join(RESULT_DATA_PATH, "forecast.csv"),
            index=False
        )

        logger.info("📊 Forecast saved → results/forecast.csv")
        return forecast_tail

    except Exception as e:
        logger.error(f"❌ Forecasting failed: {e}")
        return pd.DataFrame()
