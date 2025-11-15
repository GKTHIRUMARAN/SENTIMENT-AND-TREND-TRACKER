// ============================
// Formatters Utility
// Trend Tracker — React App
// ============================

// Format numbers (1,000 → 1k)
export function formatNumber(num) {
  if (num === null || num === undefined) return "0";
  if (num >= 1_000_000) return (num / 1_000_000).toFixed(1) + "M";
  if (num >= 1_000) return (num / 1_000).toFixed(1) + "k";
  return String(num);
}

// Format percentages (0.62 → 62%)
export function formatPercent(value) {
  if (value === null || value === undefined) return "0%";
  return `${Math.round(value)}%`;
}

// Capitalize first letter
export function capitalize(str) {
  if (!str) return "";
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// Format timestamps (ISO → readable)
export function formatTimestamp(ts) {
  if (!ts) return "N/A";
  const date = new Date(ts);
  return date.toLocaleString("en-US", {
    dateStyle: "medium",
    timeStyle: "short"
  });
}

// Shorten long text (ellipsis)
export function shorten(text, max = 20) {
  if (!text) return "";
  return text.length > max ? text.slice(0, max) + "..." : text;
}

// Safe number (avoid NaN in charts)
export function safeNumber(value) {
  return Number.isFinite(value) ? value : 0;
}
