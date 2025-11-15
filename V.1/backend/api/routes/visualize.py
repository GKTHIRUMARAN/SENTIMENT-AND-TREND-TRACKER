"""
visualize.py — Analytics Data → Frontend APIs
=============================================
Serves:
    - Sentiment counts
    - Emotion counts
    - Trend labels distribution
    - Forecast data
    - Wordcloud data
    - Dashboard summary KPIs
"""

from fastapi import APIRouter, HTTPException
import pandas as pd
import os
import json
from dotenv import load_dotenv
from loguru import logger

# ---------------------------------------------------------
# Correct Router (NO PREFIX — added in main.py)
# ---------------------------------------------------------
router = APIRouter(tags=["Visualization"])


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
RESULT_DATA_PATH = os.getenv("DATA_RESULT_PATH", "data/results/")
RESULTS_FILE = os.path.join(RESULT_DATA_PATH, "results.csv")
FORECAST_FILE = os.path.join(RESULT_DATA_PATH, "forecast.csv")


# ---------------------------------------------------------
# Helper: Load results.csv
# ---------------------------------------------------------
def load_results_df():
    if not os.path.exists(RESULTS_FILE):
        raise HTTPException(
            400, "results.csv not found. Run the analysis pipeline first."
        )
    return pd.read_csv(RESULTS_FILE)


# ---------------------------------------------------------
# Key Fillers (Fix undefined keys)
# ---------------------------------------------------------
def fill_missing_sentiment_keys(data: dict):
    base = {"Positive": 0, "Negative": 0, "Neutral": 0}
    base.update(data)
    return base


def fill_missing_emotion_keys(data: dict):
    base = {
        "Joy": 0,
        "Sadness": 0,
        "Anger": 0,
        "Fear": 0,
        "Surprise": 0,
        "Love": 0,
        "Neutral": 0
    }
    base.update(data)
    return base


def fill_missing_trend_keys(data: dict):
    if not data:
        return {"general": 0}
    return data


# ---------------------------------------------------------
# 1️⃣ Sentiment Distribution
# GET /api/visualize/sentiment
# ---------------------------------------------------------
@router.get("/sentiment")
def sentiment_distribution():
    try:
        df = load_results_df()
        counts = df["sentiment"].value_counts().to_dict()
        return fill_missing_sentiment_keys(counts)
    except Exception as e:
        logger.error(f"❌ Sentiment visualization failed: {e}")
        raise HTTPException(500, str(e))


# ---------------------------------------------------------
# 2️⃣ Emotion Distribution
# GET /api/visualize/emotion
# ---------------------------------------------------------
@router.get("/emotion")
def emotion_distribution():
    try:
        df = load_results_df()
        counts = df["emotion"].value.value_counts().to_dict()
        return fill_missing_emotion_keys(counts)
    except Exception as e:
        logger.error(f"❌ Emotion visualization failed: {e}")
        raise HTTPException(500, str(e))


# ---------------------------------------------------------
# 3️⃣ Trend Label Distribution
# GET /api/visualize/trends
# ---------------------------------------------------------
@router.get("/trends")
def trend_label_distribution():
    try:
        df = load_results_df()
        counts = df["trend_label"].value_counts().to_dict()
        return fill_missing_trend_keys(counts)
    except Exception as e:
        logger.error(f"❌ Trends visualization failed: {e}")
        raise HTTPException(500, str(e))


# ---------------------------------------------------------
# 4️⃣ Forecast Data
# GET /api/visualize/forecast
# ---------------------------------------------------------
@router.get("/forecast")
def forecast_data():
    try:
        if not os.path.exists(FORECAST_FILE):
            raise HTTPException(400, "forecast.csv not found. Run analysis first.")

        df = pd.read_csv(FORECAST_FILE)
        return df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"❌ Forecast visualization failed: {e}")
        raise HTTPException(500, str(e))


# ---------------------------------------------------------
# 5️⃣ Wordcloud Data
# GET /api/visualize/wordcloud
# ---------------------------------------------------------
@router.get("/wordcloud")
def wordcloud_data(limit: int = 30):
    try:
        df = load_results_df()

        df["keyword"] = df["text"].astype(str).str[:255]

        freq = (
            df["keyword"]
            .value_counts()
            .head(limit)
            .reset_index()
        )

        freq.columns = ["text", "value"]
        return freq.to_dict(orient="records")

    except Exception as e:
        logger.error(f"❌ Wordcloud generation failed: {e}")
        raise HTTPException(500, str(e))


# ---------------------------------------------------------
# 6️⃣ Dashboard KPIs
# GET /api/visualize/dashboard
# ---------------------------------------------------------
@router.get("/dashboard")
def dashboard_stats():
    try:
        df = load_results_df()

        sentiment_counts = fill_missing_sentiment_keys(
            df["sentiment"].value_counts().to_dict()
        )

        emotion_counts = fill_missing_emotion_keys(
            df["emotion"].value_counts().to_dict()
        )

        trend_counts = fill_missing_trend_keys(
            df["trend_label"].value_counts().to_dict()
        )

        return {
            "sentiment": sentiment_counts,
            "emotion": emotion_counts,
            "trend": trend_counts,
            "records": len(df)
        }

    except Exception as e:
        logger.error(f"❌ Dashboard KPI load failed: {e}")
        raise HTTPException(500, str(e))
