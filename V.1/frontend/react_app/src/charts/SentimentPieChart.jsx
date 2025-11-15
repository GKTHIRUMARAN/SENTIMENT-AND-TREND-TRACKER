import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import emptyState from "../assets/images/empty-state.png";

export default function SentimentPieChart({ data = [] }) {
  const colors = ["#38bdf8", "#f87171", "#a3a3a3"]; // Positive / Negative / Neutral

  return (
    <div className="w-full h-full flex items-center justify-center">
      {data.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              outerRadius={90}
            >
              {data.map((entry, index) => (
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
        </ResponsiveContainer>
      ) : (
        <img src={emptyState} alt="No Data" className="opacity-40 w-40" />
      )}
    </div>
  );
}
