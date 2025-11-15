import { FaBell } from "react-icons/fa";
import logo from "../assets/icons/logo.svg";
import profileImg from "../assets/images/profile-placeholder.png";

export default function Navbar() {
  return (
    <header className="w-full h-16 border-b border-gray-800 flex items-center justify-between px-6 bg-gray-900">
      
      {/* Left: Logo + Title */}
      <div className="flex items-center gap-3">
        <img
          src={logo}
          alt="Trend Tracker Logo"
          className="w-10 h-10 rounded-md"
        />
        <h1 className="text-xl font-semibold">Trend Tracker</h1>
      </div>

      {/* Right: Notifications + Profile */}
      <div className="flex items-center gap-6">
        
        {/* Notification Icon */}
        <button className="text-gray-300 hover:text-white transition-all">
          <FaBell size={20} />
        </button>

        {/* Profile */}
        <div className="flex items-center gap-3">
          <img
            src={profileImg}
            alt="User"
            className="w-10 h-10 rounded-full border border-gray-700"
          />
        </div>
      </div>
    </header>
  );
}
