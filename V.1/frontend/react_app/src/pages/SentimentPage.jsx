import ChartCard from "../components/ChartCard";
import KPICard from "../components/KPICard";
import sentimentIcon from "../assets/icons/sentiment.svg";
import emptyState from "../assets/images/empty-state.png";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function SentimentPage() {
  // Placeholder data (replace with API soon)
  const sentimentData = [
    { name: "Positive", value: 58 },
    { name: "Negative", value: 22 },
    { name: "Neutral", value: 20 }
  ];

  const colors = ["#38bdf8", "#f87171", "#a3a3a3"];

  return (
    <div className="flex flex-col gap-10">

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Positive"
          value="58%"
          icon={sentimentIcon}
          change="+2%"
        />
        <KPICard
          title="Negative"
          value="22%"
          icon={sentimentIcon}
          change="-1%"
        />
        <KPICard
          title="Neutral"
          value="20%"
          icon={sentimentIcon}
          change="0%"
        />
      </div>

      {/* Sentiment Pie Chart */}
      <ChartCard
        title="Sentiment Distribution"
        subtitle="Breakdown of processed data"
      >
        <ResponsiveContainer width="100%" height="100%">
          {sentimentData.length > 0 ? (
            <PieChart>
              <Pie
                data={sentimentData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={90}
              >
                {sentimentData.map((entry, index) => (
                  <Cell key={index} fill={colors[index % colors.length]} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  background: "#0f172a",
                  border: "1px solid #334155",
                  color: "#fff"
                }}
              />
            </PieChart>
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
