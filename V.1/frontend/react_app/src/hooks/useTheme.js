import { useTheme } from "../context/ThemeContext";

/**
 * useTheme
 * Lightweight hook wrapper to access theme context
 */
export default function useThemeHook() {
  const { theme, toggleTheme, setTheme } = useTheme();
  return { theme, toggleTheme, setTheme };
}
