// ============================
// Global Constants (Frontend)
// Trend Tracker — React App
// ============================

// Backend API Base
export const API_BASE_URL = "http://localhost:8000/api";

// Sentiment labels (used in charts & KPIs)
export const SENTIMENT_LABELS = ["Positive", "Negative", "Neutral"];

// Emotion labels (placeholder — update with backend model classes)
export const EMOTION_LABELS = [
  "Joy",
  "Sadness",
  "Anger",
  "Fear",
  "Surprise",
  "Love",
  "Neutral"
];

// Default Trend Keywords (UI suggestions)
export const DEFAULT_TREND_KEYWORDS = [
  "AI",
  "Technology",
  "Finance",
  "Sports",
  "Politics",
  "Health"
];

// Colors used across charts (Recharts)
export const COLORS = {
  positive: "#38bdf8",
  negative: "#f87171",
  neutral: "#a3a3a3",
  emotion: "#f472b6",
  forecast: "#fbbf24"
};

// Word cloud default config
export const WORDCLOUD_CONFIG = {
  minFont: 12,
  maxFont: 48,
  scale: 2
};

// App Info
export const APP_NAME = "Trend Tracker";
export const APP_VERSION = "1.0.0";
