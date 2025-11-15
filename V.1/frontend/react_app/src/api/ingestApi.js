import axiosClient from "./axiosClient";

// ============================
// Ingestion API (Frontend)
// Trend Tracker — React App
// ============================

// Ingest CSV file (upload)
export async function ingestCSV(formData) {
  return axiosClient.post("/ingest/csv", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
}

// Ingest from external API URL
export async function ingestFromApi(apiUrl, params = {}) {
  return axiosClient.post("/ingest/api", {
    api_url: apiUrl,
    params
  });
}

// Trigger backend to ingest default sample source
export async function ingestSample() {
  return axiosClient.post("/ingest/sample");
}
