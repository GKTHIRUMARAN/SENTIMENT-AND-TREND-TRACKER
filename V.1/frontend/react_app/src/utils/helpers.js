// ============================
// Helper Functions
// Trend Tracker — React App
// ============================

// Delay utility (for loaders, demo, retry logic)
export const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Generate random ID (useful for lists / mock data)
export function uid(prefix = "id") {
  return `${prefix}_${Math.random().toString(36).slice(2, 10)}`;
}

// Sort array of objects by key
export function sortByKey(arr, key, asc = true) {
  if (!Array.isArray(arr)) return [];
  return [...arr].sort((a, b) =>
    asc ? a[key] - b[key] : b[key] - a[key]
  );
}

// Deep clone (safe structured clone)
export function clone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

// Validate if object has required keys
export function hasKeys(obj, keys = []) {
  if (!obj) return false;
  return keys.every((key) => Object.prototype.hasOwnProperty.call(obj, key));
}

// Merge objects safely
export function merge(obj1, obj2) {
  return { ...obj1, ...obj2 };
}

// Check if an object or array is empty
export function isEmpty(value) {
  if (Array.isArray(value)) return value.length === 0;
  if (typeof value === "object" && value !== null)
    return Object.keys(value).length === 0;
  return !value;
}
