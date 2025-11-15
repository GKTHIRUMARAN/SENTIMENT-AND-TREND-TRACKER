import ChartCard from "../components/ChartCard";
import KPICard from "../components/KPICard";

import forecastIcon from "../assets/icons/forecast.svg";
import emptyState from "../assets/images/empty-state.png";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  AreaChart,
  Area
} from "recharts";

export default function ForecastPage() {
  // Placeholder forecast data (replace with API later)
  const forecastData = [
    { day: "Mon", value: 40 },
    { day: "Tue", value: 50 },
    { day: "Wed", value: 55 },
    { day: "Thu", value: 60 },
    { day: "Fri", value: 70 },
    { day: "Sat", value: 80 },
    { day: "Sun", value: 95 }
  ];

  return (
    <div className="flex flex-col gap-10">

      {/* KPI Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <KPICard
          title="Forecast Confidence"
          value="92%"
          icon={forecastIcon}
          change="+4%"
        />
        <KPICard
          title="Keyword Momentum"
          value="Strong"
          icon={forecastIcon}
        />
        <KPICard
          title="Projected Growth"
          value="+18%"
          icon={forecastIcon}
        />
      </div>

      {/* Forecast Line Chart */}
      <ChartCard
        title="7-Day Forecast"
        subtitle="Predicted keyword trend using Prophet model"
      >
        <ResponsiveContainer width="100%" height="100%">
          {forecastData.length > 0 ? (
            <LineChart data={forecastData}>
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
                dataKey="value"
                stroke="#fbbf24"
                strokeWidth={3}
                dot={{ r: 5, stroke: "#fbbf24", strokeWidth: 2 }}
              />
            </LineChart>
          ) : (
            <img
              src={emptyState}
              alt="No Data"
              className="opacity-40 w-40 mx-auto"
            />
          )}
        </ResponsiveContainer>
      </ChartCard>

      {/* Area Forecast Visualization */}
      <ChartCard
        title="Forecast Confidence Zone"
        subtitle="Shaded area indicates confidence interval"
      >
        <ResponsiveContainer width="100%" height="100%">
          {forecastData.length > 0 ? (
            <AreaChart data={forecastData}>
              <XAxis dataKey="day" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip
                contentStyle={{
                  background: "#0f172a",
                  border: "1px solid #334155",
                  color: "#fff"
                }}
              />
              <Area
                type="monotone"
                dataKey="value"
                stroke="#fbbf24"
                fill="#fbbf24"
                fillOpacity={0.2}
              />
            </AreaChart>
          ) : (
            <img
              src={emptyState}
              alt="No Data"
              className="opacity-40 w-40 mx-auto"
            />
          )}
        </ResponsiveContainer>
      </ChartCard>

    </div>
  );
}
