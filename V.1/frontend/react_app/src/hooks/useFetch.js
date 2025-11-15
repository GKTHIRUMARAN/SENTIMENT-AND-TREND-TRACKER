import { useEffect, useState } from "react";
import axiosClient from "../api/axiosClient";

/**
 * useFetch
 * Fetches data from backend API with loading + error handling
 *
 * @param {string} url - API endpoint (example: "/api/visualize/sentiment")
 * @param {any} defaultValue - initial data
 */
export default function useFetch(url, defaultValue = null) {
  const [data, setData] = useState(defaultValue);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;

    setLoading(true);
    setError(null);

    axiosClient
      .get(url)
      .then((res) => {
        if (mounted) setData(res.data);
      })
      .catch((err) => {
        if (mounted) setError(err.message || "Error fetching data");
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });

    return () => {
      mounted = false;
    };
  }, [url]);

  return { data, loading, error };
}
