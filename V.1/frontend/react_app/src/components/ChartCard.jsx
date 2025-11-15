export default function ChartCard({ title, subtitle, children }) {
  return (
    <div className="bg-gray-950 border border-gray-800 rounded-xl p-5 shadow-md hover:border-sky-500/40 transition-all">

      {/* Title Section */}
      <div className="mb-4">
        <h2 className="text-lg font-semibold text-white">{title}</h2>

        {subtitle && (
          <p className="text-sm text-gray-400 mt-1">{subtitle}</p>
        )}
      </div>

      {/* Chart Content */}
      <div className="h-72 w-full flex items-center justify-center">
        {children}
      </div>
    </div>
  );
}
