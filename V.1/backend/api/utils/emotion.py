"""
emotion.py — Emotion Classification Utility
===========================================
Handles:
    - Loading fast DistilBERT emotion model
    - Predicting a single dominant emotion from text safely
"""

from transformers import pipeline
from loguru import logger

logger.info("🔄 Loading FAST Emotion Classification Model...")

try:
    # Fast + lightweight + single-label
    emotion_model = pipeline(
        "text-classification",
        model="bhadresh-savani/distilbert-base-uncased-emotion",
        return_all_scores=False
    )
    logger.info("✅ Fast DistilBERT emotion model loaded successfully.")
except Exception as e:
    logger.error(f"❌ Failed to load emotion model: {e}")
    raise


def get_emotion(text):
    """
    Predicts a single dominant emotion for the text.
    Safely handles None, NaN, numbers, blank strings, etc.
    Always returns:
        { "label": "...", "score": float }
    """
    try:
        # -----------------------------------------------------
        # 1️⃣ Normalize text input to avoid HF pipeline crashes
        # -----------------------------------------------------
        if text is None:
            text = ""
        else:
            text = str(text).strip()

        # If empty after cleaning → return neutral
        if text == "":
            return {"label": "neutral", "score": 0.0}

        # -----------------------------------------------------
        # 2️⃣ Run the model
        # -----------------------------------------------------
        result = emotion_model(text)

        # Expected HF output: [{'label': 'joy', 'score': 0.97}]
        if isinstance(result, list) and len(result) > 0:
            return {
                "label": result[0].get("label", "unknown"),
                "score": result[0].get("score", 0.0)
            }

        # -----------------------------------------------------
        # 3️⃣ Unexpected format fallback
        # -----------------------------------------------------
        logger.warning(f"⚠ Unexpected emotion output: {result}")
        return {"label": "unknown", "score": 0.0}

    except Exception as e:
        logger.error(f"❌ Emotion prediction failed: {e}")
        return {"label": "error", "score": 0.0}
