import axiosClient from "./axiosClient";

// ============================
// Analysis API (Frontend)
// Trend Tracker — React App
// ============================

// Trigger full analysis run (ETL + sentiment + emotion + trend)
export async function runFullAnalysis() {
  return axiosClient.post("/analyze/run");
}

// Get processed sentiment data
export async function getSentimentResults() {
  return axiosClient.get("/analyze/sentiment");
}

// Get emotion results
export async function getEmotionResults() {
  return axiosClient.get("/analyze/emotion");
}

// Get trend topics
export async function getTrendTopics() {
  return axiosClient.get("/analyze/trends");
}

// Get forecast results
export async function getForecastResults() {
  return axiosClient.get("/analyze/forecast");
}
