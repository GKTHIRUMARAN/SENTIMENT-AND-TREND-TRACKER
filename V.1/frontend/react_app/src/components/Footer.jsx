export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="w-full border-t border-gray-800 bg-gray-950 text-gray-400 text-center py-4 mt-6">
      <p className="text-sm">
        © {year} Trend Tracker • Built real-time insight & analytics
      </p>
    </footer>
  );
}
