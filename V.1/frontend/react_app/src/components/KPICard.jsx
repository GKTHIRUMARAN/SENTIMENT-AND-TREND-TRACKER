export default function KPICard({ title, value, icon, change }) {
  return (
    <div className="p-5 bg-gray-950 rounded-xl border border-gray-800 shadow-md flex items-center gap-4 hover:border-sky-500/40 transition-all">

      {/* Icon */}
      {icon && (
        <img
          src={icon}
          alt=""
          className="w-10 h-10 rounded-md bg-gray-800 p-2"
        />
      )}

      {/* Text Content */}
      <div className="flex flex-col">
        <p className="text-gray-400 text-sm">{title}</p>

        <h2 className="text-2xl font-semibold text-white">
          {value}
        </h2>

        {/* Change (optional) */}
        {change && (
          <span
            className={`text-sm mt-1 ${
              change.startsWith("+") ? "text-green-400" : "text-red-400"
            }`}
          >
            {change}
          </span>
        )}
      </div>
    </div>
  );
}
