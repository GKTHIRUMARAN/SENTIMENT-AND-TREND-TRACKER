export default function LoadingSpinner({ text = "Loading..." }) {
  return (
    <div className="flex flex-col items-center justify-center py-10 gap-4 text-center">

      {/* Spinner */}
      <div className="w-10 h-10 border-4 border-gray-700 border-t-sky-400 rounded-full animate-spin"></div>

      {/* Optional text */}
      <p className="text-gray-300 text-sm">{text}</p>
    </div>
  );
}
