"""
ingest.py — Data Ingestion Layer
================================
Handles:
- API ingestion (JSON endpoints)
- CSV ingestion (local file upload)
- Raw ingestion for ETL pipeline
- Saving raw data to: data/raw/raw_data.csv
"""

from fastapi import APIRouter, UploadFile, File, HTTPException, Form
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from loguru import logger

# ---------------------------------------------------------
# Correct Router
# ---------------------------------------------------------
# DO NOT prefix here — main.py already adds /api/ingest
router = APIRouter(tags=["Ingestion"])

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
RAW_DATA_PATH = os.getenv("DATA_RAW_PATH", "data/raw/")
os.makedirs(RAW_DATA_PATH, exist_ok=True)


# ---------------------------------------------------------
# Helper: Save DataFrame to /data/raw/
# ---------------------------------------------------------
def save_raw_data(df: pd.DataFrame):
    output_path = os.path.join(RAW_DATA_PATH, "raw_data.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"📥 Raw data saved → {output_path}")
    return {"status": "success", "path": output_path}


# ---------------------------------------------------------
# 1️⃣ Ingest From External API (POST /api/ingest/api)
# ---------------------------------------------------------
@router.post("/api")
async def ingest_from_api(api_url: str = Form(...), params: str = Form(None)):
    """
    Fetch JSON data from a remote API and save to raw_data.csv.
    Frontend sends:
        api_url: string
        params: JSON string (optional)
    """
    try:
        logger.info(f"🌐 Fetching API data from: {api_url}")

        parsed_params = None
        if params:
            try:
                import json
                parsed_params = json.loads(params)
            except:
                parsed_params = None

        response = requests.get(api_url, params=parsed_params, timeout=10)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)

        if df.empty:
            raise HTTPException(status_code=400, detail="API returned empty dataset.")

        return save_raw_data(df)

    except Exception as e:
        logger.error(f"❌ API ingestion failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# 2️⃣ Upload CSV File (POST /api/ingest/csv)
# ---------------------------------------------------------
@router.post("/csv")
async def ingest_from_csv(file: UploadFile = File(...)):
    """
    Upload a CSV file and save it to raw_data.csv.
    """
    try:
        logger.info(f"📄 Uploading CSV file: {file.filename}")

        df = pd.read_csv(file.file)
        if df.empty:
            raise HTTPException(status_code=400, detail="Uploaded CSV is empty.")

        return save_raw_data(df)

    except Exception as e:
        logger.error(f"❌ CSV ingestion failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# 3️⃣ Backend Sample Dataset Loader (POST /api/ingest/sample)
# ---------------------------------------------------------
@router.post("/sample")
async def ingest_sample():
    """
    Load example/sample data (useful for frontend testing).
    """
    try:
        sample_path = os.path.join("data", "sample", "sample_data.csv")

        if not os.path.exists(sample_path):
            raise HTTPException(404, "Sample dataset not found.")

        df = pd.read_csv(sample_path)
        if df.empty:
            raise HTTPException(400, "Sample dataset is empty.")

        return save_raw_data(df)

    except Exception as e:
        logger.error(f"❌ Sample ingestion failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------------------------------------
# 4️⃣ Used internally — file path ingestion (Not API)
# ---------------------------------------------------------
def ingest_from_local(path: str):
    """
    Used internally by ETL pipeline.
    """
    try:
        logger.info(f"📂 Loading local CSV: {path}")
        df = pd.read_csv(path)

        if df.empty:
            raise Exception("Local CSV file is empty.")

        return save_raw_data(df)

    except Exception as e:
        logger.error(f"❌ Local ingestion failed: {e}")
        raise


# ---------------------------------------------------------
# 5️⃣ SYNC ingestion (for ETL Automation)
# ---------------------------------------------------------
def ingest_from_csv_sync(path: str):
    """
    Synchronous CSV ingestion (backend internal).
    """
    try:
        logger.info(f"📂 [SYNC] Loading CSV for ETL: {path}")

        df = pd.read_csv(path)
        if df.empty:
            raise Exception("CSV file is empty.")

        return save_raw_data(df)

    except Exception as e:
        logger.error(f"❌ SYNC CSV ingestion failed: {e}")
        raise
