import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import emptyState from "../assets/images/empty-state.png";

export default function EmotionBarChart({ data = [] }) {
  return (
    <div className="w-full h-full flex items-center justify-center">
      {data.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
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
