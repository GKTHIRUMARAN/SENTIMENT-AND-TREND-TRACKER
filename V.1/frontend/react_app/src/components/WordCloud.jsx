import ReactWordcloud from "react-wordcloud";

export default function WordCloud({ words }) {
  const options = {
    rotations: 2,
    rotationAngles: [-45, 0],
    fontSizes: [18, 60],
    scale: "sqrt",
    enableTooltip: true,
    fontFamily: "system-ui",
    colors: ["#38BDF8", "#34D399", "#F87171", "#A78BFA", "#FBBF24"],
  };

  return (
    <div className="bg-gray-950 border border-gray-800 rounded-xl p-5 shadow-md hover:border-sky-500/40 transition-all h-80">
      <ReactWordcloud options={options} words={words} />
    </div>
  );
}
