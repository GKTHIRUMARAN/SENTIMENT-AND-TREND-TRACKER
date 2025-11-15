import axios from "axios";
import { API_BASE_URL } from "../utils/constants";

// ============================
// Axios Client (Base Instance)
// Trend Tracker — React App
// ============================

const axiosClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 15000
});

// Request Interceptor
axiosClient.interceptors.request.use(
  (config) => {
    // Future: attach tokens or headers
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor
axiosClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const err = error.response?.data || { message: "API Error" };
    return Promise.reject(err);
  }
);

export default axiosClient;
