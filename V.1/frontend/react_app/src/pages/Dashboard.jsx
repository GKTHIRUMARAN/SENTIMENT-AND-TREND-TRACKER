import KPICard from "../components/KPICard";
import ChartCard from "../components/ChartCard";
import sentimentIcon from "../assets/icons/sentiment.svg";
import emotionIcon from "../assets/icons/emotion.svg";
import trendIcon from "../assets/icons/trend.svg";
import heroImg from "../assets/images/hero-dashboard.png";

import {
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function Dashboard() {
  // Placeholder data (replace with API later)
  const sentimentData = [
    { name: "Positive", value: 55 },
    { name: "Negative", value: 25 },
    { name: "Neutral", value: 20 }
  ];

  const colors = ["#38bdf8", "#f87171", "#a3a3a3"];

  const trendData = [
    { name: "Mon", value: 20 },
    { name: "Tue", value: 40 },
    { name: "Wed", value: 35 },
    { name: "Thu", value: 50 },
    { name: "Fri", value: 60 }
  ];

  return (
    <div className="flex flex-col gap-10">

      {/* Hero Banner */}
      <div className="w-full h-64 rounded-xl overflow-hidden shadow-xl">
        <img
          src={heroImg}
          alt="Dashboard Hero"
          className="w-full h-full object-cover"
        />
      </div>

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Sentiment Score"
          value="62%"
          icon={sentimentIcon}
          change="+4%"
        />
        <KPICard
          title="Top Emotion"
          value="Joy"
          icon={emotionIcon}
          change="+2%"
        />
        <KPICard
          title="Trending Strength"
          value="High"
          icon={trendIcon}
          change="-1%"
        />
      </div>

      {/* Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

        {/* Sentiment Pie */}
        <ChartCard title="Sentiment Distribution" subtitle="Latest processed data">
          <ResponsiveContainer width="100%" height="100%">
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
            </PieChart>
          </ResponsiveContainer>
        </ChartCard>

        {/* Trend Bar Chart */}
        <ChartCard title="Weekly Trend Activity" subtitle="Keyword engagement levels">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={trendData}>
              <XAxis dataKey="name" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip
                contentStyle={{
                  background: "#0f172a",
                  border: "1px solid #334155",
                  color: "#fff"
                }}
              />
              <Bar dataKey="value" fill="#38bdf8" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </ChartCard>

      </div>
    </div>
  );
}
