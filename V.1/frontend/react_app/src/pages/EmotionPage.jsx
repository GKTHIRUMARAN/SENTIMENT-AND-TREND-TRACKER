import ChartCard from "../components/ChartCard";
import KPICard from "../components/KPICard";
import emotionIcon from "../assets/icons/emotion.svg";
import emptyState from "../assets/images/empty-state.png";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function EmotionPage() {
  // Placeholder data (replace with API later)
  const emotionData = [
    { emotion: "Joy", value: 40 },
    { emotion: "Sadness", value: 18 },
    { emotion: "Anger", value: 12 },
    { emotion: "Fear", value: 8 },
    { emotion: "Surprise", value: 22 }
  ];

  return (
    <div className="flex flex-col gap-10">

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Top Emotion"
          value="Joy"
          icon={emotionIcon}
          change="+3%"
        />
        <KPICard
          title="Emotion Variety"
          value="5 Types"
          icon={emotionIcon}
        />
        <KPICard
          title="Dominant Level"
          value="High"
          icon={emotionIcon}
        />
      </div>

      {/* Emotion Bar Chart */}
      <ChartCard
        title="Emotion Frequency"
        subtitle="Distribution across processed text"
      >
        <ResponsiveContainer width="100%" height="100%">
          {emotionData.length > 0 ? (
            <BarChart data={emotionData}>
              <XAxis dataKey="emotion" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip
                contentStyle={{
                  background: "#0f172a",
                  border: "1px solid #334155",
                  color: "#fff"
                }}
              />
              <Bar dataKey="value" fill="#f472b6" radius={[6, 6, 0, 0]} />
            </BarChart>
          ) : (
            <img
              src={emptyState}
              alt="No Data"
              className="opacity-40 w-40"
            />
          )}
        </ResponsiveContainer>
      </ChartCard>

    </div>
  );
}
