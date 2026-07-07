// ====== Circle progress ring ======
export function CircleProgress({ value, max, size = 130, label, sublabel }) {
  const r = (size - 16) / 2;
  const circ = 2 * Math.PI * r;
  const pct = Math.min(value / max, 1);
  return (
    <div style={{ position: "relative", width: size, height: size }}>
      <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="rgba(255,255,255,0.25)" strokeWidth={8} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="white" strokeWidth={8}
          strokeDasharray={`${circ * pct} ${circ}`} strokeLinecap="round"
          style={{ transition: "stroke-dasharray 0.5s ease" }} />
      </svg>
      <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
        <div style={{ fontSize: 26, fontWeight: 800, color: "white", lineHeight: 1 }}>{Math.round(value)}</div>
        <div style={{ fontSize: 11, color: "rgba(255,255,255,0.85)", marginTop: 2 }}>{label}</div>
        {sublabel && <div style={{ fontSize: 10, color: "rgba(255,255,255,0.7)" }}>{sublabel}</div>}
      </div>
    </div>
  );
}

export function MacroBar({ label, current, max }) {
  const pct = Math.min((current / max) * 100, 100);
  return (
    <div style={{ flex: 1 }}>
      <div style={{ fontSize: 11, color: "rgba(255,255,255,0.7)", marginBottom: 4 }}>{label}</div>
      <div style={{ height: 4, background: "rgba(255,255,255,0.2)", borderRadius: 4, overflow: "hidden" }}>
        <div style={{ width: `${pct}%`, height: "100%", background: "white", borderRadius: 4, transition: "width 0.4s ease" }} />
      </div>
      <div style={{ fontSize: 11, color: "rgba(255,255,255,0.9)", marginTop: 4 }}>{Math.round(current)}/{max}g</div>
    </div>
  );
}
