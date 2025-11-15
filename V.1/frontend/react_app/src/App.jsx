import { Routes, Route, Navigate } from "react-router-dom";
import { lazy, Suspense } from "react";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";

import "./index.css";

// Lazy-loaded pages
const Dashboard = lazy(() => import("./pages/Dashboard"));
const SentimentPage = lazy(() => import("./pages/SentimentPage"));
const EmotionPage = lazy(() => import("./pages/EmotionPage"));
const TrendPage = lazy(() => import("./pages/TrendPage"));
const ForecastPage = lazy(() => import("./pages/ForecastPage"));
const MemoryPage = lazy(() => import("./pages/MemoryPage"));

export default function App() {
  return (
    <div className="flex min-h-screen bg-gray-900 text-white">

      {/* Sidebar */}
      <Sidebar />

      {/* Right section */}
      <div className="flex-1 flex flex-col">

        {/* Navbar */}
        <Navbar />

        {/* Page Content */}
        <main className="p-6 flex-1">
          <Suspense fallback={<div className="text-center p-10">Loading...</div>}>
            <Routes>
              <Route path="/" element={<Navigate to="/dashboard" />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/sentiment" element={<SentimentPage />} />
              <Route path="/emotion" element={<EmotionPage />} />
              <Route path="/trend" element={<TrendPage />} />
              <Route path="/forecast" element={<ForecastPage />} />
              <Route path="/memory" element={<MemoryPage />} />
              <Route path="*" element={<Navigate to="/dashboard" />} />
            </Routes>
          </Suspense>
        </main>

        {/* Footer (always at bottom) */}
        <Footer />
      </div>
    </div>
  );
}
