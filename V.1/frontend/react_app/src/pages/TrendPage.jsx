import ChartCard from "../components/ChartCard";
import KPICard from "../components/KPICard";
import WordCloud from "../components/WordCloud";

import trendIcon from "../assets/icons/trend.svg";
import emptyState from "../assets/images/empty-state.png";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function TrendPage() {
  // Placeholder data (replace with API later)
  const keywordTrends = [
    { day: "Mon", score: 20 },
    { day: "Tue", score: 45 },
    { day: "Wed", score: 30 },
    { day: "Thu", score: 55 },
    { day: "Fri", score: 60 }
  ];

  const wordCloudData = [
    { text: "AI", value: 40 },
    { text: "Trend", value: 28 },
    { text: "Analytics", value: 22 },
    { text: "Forecast", value: 19 },
    { text: "Sentiment", value: 16 },
    { text: "Data", value: 10 }
  ];

  return (
    <div className="flex flex-col gap-10">

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Top Trending Keyword"
          value="AI"
          icon={trendIcon}
          change="+12%"
        />
        <KPICard
          title="Trend Strength"
          value="High"
          icon={trendIcon}
          change="+3%"
        />
        <KPICard
          title="Activity Score"
          value="60"
          icon={trendIcon}
          change="+5%"
        />
      </div>

      {/* Trend Line Chart */}
      <ChartCard
        title="Keyword Trend Over Time"
        subtitle="Daily trend score for selected keyword"
      >
        <ResponsiveContainer width="100%" height="100%">
          {keywordTrends.length > 0 ? (
            <LineChart data={keywordTrends}>
              <XAxis dataKey="day" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip
                contentStyle={{
                  background: "#0f172a",
                  border: "1px solid #334155",
                  color: "#fff"
                }}
              />
              <Line
                type="monotone"
                dataKey="score"
                stroke="#38bdf8"
                strokeWidth={3}
                dot={{ r: 5, stroke: "#38bdf8", strokeWidth: 2 }}
              />
            </LineChart>
          ) : (
            <img
              src={emptyState}
              alt="No Data"
              className="opacity-40 w-40"
            />
          )}
        </ResponsiveContainer>
      </ChartCard>

      {/* Word Cloud */}
      <ChartCard
        title="Trending Keywords Cloud"
        subtitle="Keyword weight based on frequency & relevance"
      >
        {wordCloudData.length > 0 ? (
          <WordCloud words={wordCloudData} />
        ) : (
          <img
            src={emptyState}
            alt="No Data"
            className="opacity-40 w-40 mx-auto"
          />
        )}
      </ChartCard>

    </div>
  );
}
