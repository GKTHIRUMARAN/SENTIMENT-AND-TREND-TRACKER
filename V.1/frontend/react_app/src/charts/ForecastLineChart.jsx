import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import emptyState from "../assets/images/empty-state.png";

export default function ForecastLineChart({ data = [] }) {
  return (
    <div className="w-full h-full flex items-center justify-center">
      {data.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
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
        </ResponsiveContainer>
      ) : (
        <img
          src={emptyState}
          alt="No Data"
          className="opacity-40 w-40"
        />
      )}
    </div>
  );
}
