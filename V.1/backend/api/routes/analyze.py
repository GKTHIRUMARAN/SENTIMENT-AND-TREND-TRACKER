"""
analyze.py — Master Analysis Pipeline
=====================================
Runs:
    - Preprocessed data -> models -> results
Uses:
    - sentiment.py
    - emotion.py
    - trend.py
Saves:
    - results.csv
    - topics.json
    - forecast.csv
Writes:
    - DB entries (trends table)
"""

from fastapi import APIRouter, HTTPException, Depends
import pandas as pd
import os
from loguru import logger
from sqlalchemy.orm import Session
from sqlalchemy import text
from dotenv import load_dotenv

# ML utilities
from ..utils.sentiment import get_sentiment
from ..utils.emotion import get_emotion
from ..utils.trend import extract_topics, forecast_trend

# DB
from ..db.connector import get_db

# ---------------------------------------------------------
# Correct Router Configuration
# ---------------------------------------------------------
# DO NOT prefix here because main.py already adds "/api/analyze"
router = APIRouter(tags=["Analysis"])


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
CLEAN_DATA_PATH = os.getenv("DATA_CLEAN_PATH", "data/cleaned/")
RESULT_DATA_PATH = os.getenv("DATA_RESULT_PATH", "data/results/")
os.makedirs(RESULT_DATA_PATH, exist_ok=True)


# ---------------------------------------------------------
# DB helper
# ---------------------------------------------------------
def insert_trend_record(db: Session, keyword, sentiment_score, emotion, trend_label):
    sql = text("""
        INSERT INTO trends (keyword, sentiment_score, emotion, trend_label)
        VALUES (:keyword, :sentiment_score, :emotion, :trend_label)
    """)
    db.execute(sql, {
        "keyword": keyword,
        "sentiment_score": sentiment_score,
        "emotion": emotion,
        "trend_label": trend_label
    })
    db.commit()


# ---------------------------------------------------------
# Core analysis logic
# ---------------------------------------------------------
def _run_analysis_core(clean_file: str, result_folder: str):
    logger.info(f"🧪 Loading cleaned dataset: {clean_file}")

    if not os.path.exists(clean_file):
        raise FileNotFoundError("cleaned_data.csv not found.")

    df = pd.read_csv(clean_file)
    if df.empty:
        raise ValueError("Cleaned dataset is empty.")

    # 1️⃣ Sentiment
    logger.info("📝 Running sentiment...")
    df["sentiment"] = df["clean_text"].apply(lambda x: get_sentiment(x)["label"])
    df["sentiment_score"] = df["clean_text"].apply(lambda x: get_sentiment(x)["score"])

    # 2️⃣ Emotion
    logger.info("🎭 Running emotion...")
    df["emotion"] = df["clean_text"].apply(lambda x: get_emotion(x)["label"])

    # 3️⃣ Topic Modeling
    logger.info("🧠 Extracting topics...")
    texts = df["clean_text"].astype(str).tolist()  # FIXED: ensure string list
    topics_df = extract_topics(texts)

    if not topics_df.empty:
        topic_labels = topics_df["Name"].tolist()
        df["trend_label"] = topic_labels[0] if topic_labels else "general"
    else:
        df["trend_label"] = "general"

    # 4️⃣ Forecast
    logger.info("📈 Running forecast...")
    forecast_input = (
        df.groupby("sentiment")["sentiment"]
        .count()
        .reset_index(name="count")
    )
    forecast_input["created_at"] = pd.Timestamp.now()

    forecast_df = forecast_trend(
        forecast_input, 
        date_col="created_at", 
        value_col="count"
    )

    # SAVE RESULTS
    results_path = os.path.join(result_folder, "results.csv")
    df.to_csv(results_path, index=False)

    forecast_path = os.path.join(result_folder, "forecast.csv")
    forecast_df.to_csv(forecast_path, index=False)

    logger.info(f"📁 Saved results → {results_path}")
    logger.info(f"📁 Saved forecast → {forecast_path}")

    return {
        "results_path": results_path,
        "forecast_path": forecast_path,
        "status": "success"
    }


# ---------------------------------------------------------
# API: Run Full Analysis (Frontend calls POST /api/analyze/run)
# ---------------------------------------------------------
@router.post("/run")
def run_analysis(db: Session = Depends(get_db)):
    try:
        clean_file = os.path.join(CLEAN_DATA_PATH, "cleaned_data.csv")
        output = _run_analysis_core(clean_file, RESULT_DATA_PATH)

        df = pd.read_csv(output["results_path"])
        for _, row in df.iterrows():
            insert_trend_record(
                db=db,
                keyword=str(row.get("text", ""))[:255],
                sentiment_score=row["sentiment_score"],
                emotion=row["emotion"],
                trend_label=row["trend_label"]
            )

        logger.info("✅ Analysis completed via API.")
        return {"status": "success", **output}

    except Exception as e:
        logger.error(f"❌ Analysis API failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# API: Get Sentiment Results (GET /api/analyze/sentiment)
# ---------------------------------------------------------
@router.get("/sentiment")
def get_sentiment_results():
    try:
        path = os.path.join(RESULT_DATA_PATH, "results.csv")
        df = pd.read_csv(path)

        counts = df["sentiment"].value_counts().to_dict()
        return counts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# API: Get Emotion Results (GET /api/analyze/emotion)
# ---------------------------------------------------------
@router.get("/emotion")
def get_emotion_results():
    try:
        path = os.path.join(RESULT_DATA_PATH, "results.csv")
        df = pd.read_csv(path)

        counts = df["emotion"].value_counts().to_dict()
        return counts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# API: Trend Topic Labels (GET /api/analyze/trends)
# ---------------------------------------------------------
@router.get("/trends")
def get_trends():
    try:
        path = os.path.join(RESULT_DATA_PATH, "results.csv")
        df = pd.read_csv(path)

        topics = df["trend_label"].value_counts().to_dict()
        return topics

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# API: Forecast Data (GET /api/analyze/forecast)
# ---------------------------------------------------------
@router.get("/forecast")
def get_forecast():
    try:
        path = os.path.join(RESULT_DATA_PATH, "forecast.csv")
        df = pd.read_csv(path)

        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# ETL Sync Version (Used for automation)
# ---------------------------------------------------------
def run_analysis_sync(clean_file: str = None, result_folder: str = None):
    try:
        clean_file = clean_file or os.path.join(CLEAN_DATA_PATH, "cleaned_data.csv")
        result_folder = result_folder or RESULT_DATA_PATH

        logger.info("🧠 Running analysis (ETL sync mode)...")
        return _run_analysis_core(clean_file, result_folder)

    except Exception as e:
        logger.error(f"❌ run_analysis_sync failed: {e}")
        raise
