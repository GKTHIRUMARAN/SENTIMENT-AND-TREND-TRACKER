import axiosClient from "./axiosClient";

// ============================
// Visualization API (Frontend)
// Trend Tracker — React App
// ============================

// Sentiment distribution (value counts)
export async function fetchSentimentChart() {
  return axiosClient.get("/visualize/sentiment");
}

// Emotion distribution
export async function fetchEmotionChart() {
  return axiosClient.get("/visualize/emotion");
}

// Trend topics visualization
export async function fetchTrendTopics() {
  return axiosClient.get("/visualize/trends");
}

// Forecast chart visualization
export async function fetchForecastChart() {
  return axiosClient.get("/visualize/forecast");
}

// Wordcloud data (keywords & weights)
export async function fetchWordCloud() {
  return axiosClient.get("/visualize/wordcloud");
}

// Dashboard summary KPIs
export async function fetchDashboardStats() {
  return axiosClient.get("/visualize/dashboard");
}
