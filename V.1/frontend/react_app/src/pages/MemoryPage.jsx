import { useState } from "react";
import ChartCard from "../components/ChartCard";
import KPICard from "../components/KPICard";

import memoryIcon from "../assets/icons/memory.svg";
import emptyState from "../assets/images/empty-state.png";

export default function MemoryPage() {
  // Placeholder memory logs (replace with API later)
  const [memoryLogs] = useState([
    {
      query: "What is today's sentiment?",
      summary: "Sentiment is mostly positive.",
      timestamp: "2025-01-12 10:15 AM"
    },
    {
      query: "Show emotion trend",
      summary: "Joy and surprise levels increased.",
      timestamp: "2025-01-11 09:40 AM"
    }
  ]);

  return (
    <div className="flex flex-col gap-10">

      {/* KPI Area */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Memory Entries"
          value={memoryLogs.length}
          icon={memoryIcon}
          change={memoryLogs.length > 1 ? "+1" : "0"}
        />
        <KPICard
          title="Last Query"
          value={
            memoryLogs.length
              ? memoryLogs[0].query.slice(0, 12) + "..."
              : "None"
          }
          icon={memoryIcon}
        />
        <KPICard
          title="Last Updated"
          value={
            memoryLogs.length
              ? memoryLogs[0].timestamp
              : "No Records"
          }
          icon={memoryIcon}
        />
      </div>

      {/* Memory Log Section */}
      <ChartCard
        title="Memory Log"
        subtitle="Query history and summary insights"
      >
        {memoryLogs.length > 0 ? (
          <div className="w-full h-full overflow-y-auto pr-2 space-y-4">
            {memoryLogs.map((log, index) => (
              <div
                key={index}
                className="bg-gray-900 border border-gray-800 rounded-xl p-4 hover:border-sky-500/40 transition-all"
              >
                <p className="text-gray-400 text-sm">{log.timestamp}</p>
                <p className="text-white text-lg font-semibold mt-1">
                  {log.query}
                </p>
                <p className="text-gray-300 mt-1">{log.summary}</p>
              </div>
            ))}
          </div>
        ) : (
          <div className="flex items-center justify-center h-full">
            <img
              src={emptyState}
              alt="No Memory"
              className="opacity-40 w-40"
            />
          </div>
        )}
      </ChartCard>
    </div>
	);
}