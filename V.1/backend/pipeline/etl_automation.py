"""
etl_automation.py — Full Automated Pipeline
===========================================
Runs:
    1. Ingestion  (CSV → data/raw/)
    2. Preprocessing (clean → data/cleaned/)
    3. Analysis (models → data/results/)
    4. Memory update (store summary)
    5. Logging every step

Run manually:
    python backend/pipeline/etl_automation.py
"""

import os
import sys
from loguru import logger
from dotenv import load_dotenv
from datetime import datetime

# ---------------------------------------------------------
# Add project ROOT directory to Python path
# ---------------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# ---------------------------------------------------------
# Absolute Imports (Fix for ImportError)
# ---------------------------------------------------------
from backend.api.routes.ingest import ingest_from_csv_sync   # FIXED: sync ingest
from backend.api.utils.preprocess import preprocess_data
from backend.api.routes.analyze import run_analysis_sync         # FIX: calling with no args
from backend.api.routes.memory import add_memory_entry       # working ETL memory function

# Load .env
load_dotenv()

RAW_PATH = os.getenv("DATA_RAW_PATH", "data/raw/")
CLEAN_PATH = os.getenv("DATA_CLEAN_PATH", "data/cleaned/")
RESULT_PATH = os.getenv("DATA_RESULT_PATH", "data/results/")

os.makedirs(RAW_PATH, exist_ok=True)
os.makedirs(CLEAN_PATH, exist_ok=True)
os.makedirs(RESULT_PATH, exist_ok=True)


# ---------------------------------------------------------
# Helper: Get or create raw_data.csv
# ---------------------------------------------------------
def _get_raw_file():
    raw_file_path = os.path.join(RAW_PATH, "raw_data.csv")

    # If raw_data.csv already exists → use it
    if os.path.exists(raw_file_path):
        return raw_file_path

    # Otherwise check sample_data.csv in root
    sample_path = "sample_data.csv"
    if os.path.exists(sample_path):
        import shutil
        shutil.copy(sample_path, raw_file_path)
        logger.info("📥 sample_data.csv found — copied to data/raw/raw_data.csv")
        return raw_file_path

    # Nothing exists → error
    return None


# ---------------------------------------------------------
# Generate Pipeline Summary
# ---------------------------------------------------------
def _generate_summary():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    summary = (
        f"ETL Pipeline Summary [{timestamp}]\n"
        f"- Raw file: raw_data.csv\n"
        f"- Cleaned: cleaned_data.csv\n"
        f"- Results: results.csv\n"
        f"- Status: Completed"
    )
    return summary


# ---------------------------------------------------------
# Main Pipeline Runner
# ---------------------------------------------------------
def run_full_pipeline():
    try:
        logger.info("🚀 Starting ETL + Analysis pipeline...")

        # ---------------- INGESTION -------------------
        raw_file = _get_raw_file()

        if not raw_file:
            raise FileNotFoundError(
                "❌ No raw_data.csv. Add sample_data.csv to project root or ingest via API."
            )

        logger.info(f"📥 Ingesting file: {raw_file}")
        ingest_from_csv_sync(raw_file)  # FIXED: sync ingestion

        # ---------------- PREPROCESSING -------------------
        clean_path = os.path.join(CLEAN_PATH, "cleaned_data.csv")
        logger.info("🧼 Running preprocessing...")
        preprocess_data(raw_file, clean_path)

        # ---------------- ANALYSIS -------------------
        logger.info("🧠 Running sentiment, emotion, topic, and forecast analysis...")
        run_analysis_sync(clean_path, RESULT_PATH)  # FIXED: call with no args

        # ---------------- MEMORY UPDATE -------------------
        summary = _generate_summary()
        add_memory_entry("ETL Pipeline Auto-Run", summary)
        logger.info("🧠 Memory updated with pipeline summary.")

        # ---------------- FINISHED -------------------
        logger.info("🎉 ETL + Analysis Pipeline Completed Successfully.")
        return {"status": "success", "summary": summary}

    except Exception as e:
        logger.error(f"❌ Pipeline Failed: {e}")
        return {"status": "error", "detail": str(e)}


# ---------------------------------------------------------
# Script Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    output = run_full_pipeline()
    print(output)
