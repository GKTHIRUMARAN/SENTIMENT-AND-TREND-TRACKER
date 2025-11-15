import axiosClient from "./axiosClient";

// ============================
// Memory API (Frontend)
// Trend Tracker — React App
// ============================

// Get all memory entries
export async function fetchMemoryLogs() {
  return axiosClient.get("/memory/logs");
}

// Add a new memory entry
export async function addMemoryEntry(query, summary) {
  return axiosClient.post("/memory/add", {
    query,
    summary
  });
}

// Clear memory history
export async function clearMemory() {
  return axiosClient.post("/memory/clear");
}
