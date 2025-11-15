import { NavLink } from "react-router-dom";

import logo from "../assets/icons/logo.svg";
import trendIcon from "../assets/icons/trend.svg";
import sentimentIcon from "../assets/icons/sentiment.svg";
import emotionIcon from "../assets/icons/emotion.svg";
import forecastIcon from "../assets/icons/forecast.svg";
import memoryIcon from "../assets/icons/memory.svg";

export default function Sidebar() {
  const navItems = [
    { name: "Dashboard", path: "/dashboard", icon: logo },
    { name: "Sentiment", path: "/sentiment", icon: sentimentIcon },
    { name: "Emotion", path: "/emotion", icon: emotionIcon },
    { name: "Trend", path: "/trend", icon: trendIcon },
    { name: "Forecast", path: "/forecast", icon: forecastIcon },
    { name: "Memory", path: "/memory", icon: memoryIcon }
  ];

  return (
    <aside className="w-60 bg-gray-950 text-gray-300 border-r border-gray-800 min-h-screen p-4 flex flex-col">

      {/* Logo */}
      <div className="flex items-center gap-3 mb-8 px-3">
        <img src={logo} alt="Trend Logo" className="w-10 h-10 rounded-md" />
        <h2 className="text-2xl font-bold">Trend</h2>
      </div>

      {/* Navigation */}
      <nav className="flex flex-col gap-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-3 rounded-lg transition-all ${
                isActive
                  ? "bg-gray-800 text-white shadow-md"
                  : "text-gray-400 hover:bg-gray-800 hover:text-white"
              }`
            }
          >
            <img src={item.icon} alt="" className="w-6 h-6" />
            <span className="text-sm font-medium">{item.name}</span>
          </NavLink>
        ))}
      </nav>

      {/* Bottom footer label */}
      <div className="mt-auto text-xs text-gray-600 px-3 py-4">
        v1.0 • Trend Tracker
      </div>
    </aside>
  );
}
