"""
preprocess.py — Text Cleaning & Normalization
=============================================
Handles:
- URL removal
- HTML stripping
- Lowercasing
- Removing numbers/symbols
- Tokenizing
- Stopword removal
- Lemmatization
Saves cleaned CSV → data/cleaned/cleaned_data.csv
"""

import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from loguru import logger
import os
from dotenv import load_dotenv

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
CLEAN_DATA_PATH = os.getenv("DATA_CLEAN_PATH", "data/cleaned/")
os.makedirs(CLEAN_DATA_PATH, exist_ok=True)

# ---------------------------------------------------------
# Ensure NLTK data is available
# ---------------------------------------------------------
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

# ---------------------------------------------------------
# Setup NLP Tools
# ---------------------------------------------------------
STOPWORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

# ---------------------------------------------------------
# Helper: Clean a single text string
# ---------------------------------------------------------
def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Keep only alphabets & whitespace
    text = re.sub(r"[^A-Za-z\s]", " ", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Lowercase
    text = text.lower()

    # Tokenize + remove stopwords + lemmatize
    tokens = [
        LEMMATIZER.lemmatize(word)
        for word in text.split()
        if word not in STOPWORDS
    ]

    return " ".join(tokens)


# ---------------------------------------------------------
# Pipeline: Clean an entire dataset
# ---------------------------------------------------------
def preprocess_data(input_path: str, output_path: str = None):
    """
    Reads raw CSV → cleans column 'text' → saves cleaned file.
    Expected input CSV must have a column named 'text'.
    """
    try:
        logger.info(f"🧼 Loading raw dataset → {input_path}")
        df = pd.read_csv(input_path)

        if "text" not in df.columns:
            raise Exception("Input CSV must contain a 'text' column.")

        logger.info("🧹 Cleaning text column...")
        df["clean_text"] = df["text"].astype(str).apply(clean_text)

        # Output path
        if output_path is None:
            output_path = os.path.join(CLEAN_DATA_PATH, "cleaned_data.csv")

        df.to_csv(output_path, index=False)
        logger.info(f"✨ Cleaned data saved → {output_path}")
        return output_path

    except Exception as e:
        logger.error(f"❌ Preprocessing failed: {e}")
        raise
