import { createContext, useContext, useState } from "react";

const AppContext = createContext();

export function AppProvider({ children }) {
  // Global states (expand later when API is connected)
  const [loading, setLoading] = useState(false);
  const [selectedKeyword, setSelectedKeyword] = useState("AI");
  const [theme, setTheme] = useState("dark"); // future use

  const value = {
    loading,
    setLoading,
    selectedKeyword,
    setSelectedKeyword,
    theme,
    setTheme
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useAppContext() {
  return useContext(AppContext);
}
