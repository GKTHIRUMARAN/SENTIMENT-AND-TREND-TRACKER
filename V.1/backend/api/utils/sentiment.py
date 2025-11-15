"""
sentiment.py — Sentiment Analysis Module
========================================
Hybrid sentiment engine:
1. VADER (rule-based, fast)
2. TextBlob fallback (optional)
3. Compound score normalization
Outputs:
- sentiment label (Positive / Neutral / Negative)
- numeric sentiment score (compound)
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from loguru import logger

# ---------------------------------------------------------
# Initialize VADER analyzer
# ---------------------------------------------------------
vader_analyzer = SentimentIntensityAnalyzer()

# ---------------------------------------------------------
# Core: Analyze sentiment with VADER (primary)
# ---------------------------------------------------------
def _vader_score(text: str) -> float:
    try:
        return vader_analyzer.polarity_scores(text)["compound"]
    except Exception as e:
        logger.error(f"❌ VADER sentiment failed: {e}")
        return 0.0


# ---------------------------------------------------------
# Fallback: TextBlob sentiment (used when VADER fails)
# ---------------------------------------------------------
def _textblob_score(text: str) -> float:
    try:
        blob = TextBlob(text)
        return float(blob.sentiment.polarity)
    except Exception as e:
        logger.error(f"❌ TextBlob sentiment failed: {e}")
        return 0.0


# ---------------------------------------------------------
# Label assignment
# ---------------------------------------------------------
def _score_to_label(score: float) -> str:
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    return "Neutral"


# ---------------------------------------------------------
# Public API: Get sentiment label + score
# ---------------------------------------------------------
def get_sentiment(text: str) -> dict:
    """
    Input: single text string
    Output:
        {
            "label": "Positive",
            "score": 0.76
        }
    """
    if not isinstance(text, str):
        return {"label": "Neutral", "score": 0.0}

    # 1. Try VADER first
    score = _vader_score(text)

    # 2. If VADER gives zero → optional TextBlob fallback
    if score == 0.0:
        score = _textblob_score(text)

    label = _score_to_label(score)

    logger.debug(f"📝 Sentiment — '{text[:50]}...' → {label} ({score})")

    return {"label": label, "score": score}
