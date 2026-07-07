import { useState, useEffect } from "react";
import { api } from "../lib/api";

const MEAL_LABELS = { breakfast: "Bữa sáng", lunch: "Bữa trưa", dinner: "Bữa tối", snack: "Ăn vặt" };

export function FoodSearchModal({ meal, onClose, onAdded, dateKey }) {
  const [q, setQ] = useState("");
  const [foods, setFoods] = useState([]);
  const [qty, setQty] = useState({});
  const [showCreate, setShowCreate] = useState(false);

  useEffect(() => {
    const t = setTimeout(() => { api.searchFoods(q).then(setFoods).catch(() => {}); }, 250);
    return () => clearTimeout(t);
  }, [q]);

  async function add(food) {
    await api.addEntry({
      log_date: dateKey, meal, food_name: food.name, qty: qty[food.id] || 1,
      unit: food.unit, cal: food.cal, carbs: food.carbs, protein: food.protein, fat: food.fat,
    });
    onAdded();
  }

  return (
    <Sheet color="linear-gradient(135deg,#4ade80,#22c55e)" title={MEAL_LABELS[meal]} onClose={onClose}>
      <div style={{ padding: "0 20px 12px", background: "linear-gradient(135deg,#4ade80,#22c55e)" }}>
        <div style={{ background: "white", borderRadius: 12, padding: "10px 16px", display: "flex", alignItems: "center", gap: 8 }}>
          <span>🔍</span>
          <input value={q} onChange={e => setQ(e.target.value)} autoFocus
            placeholder="Tìm món (phở, cơm tấm, bánh mì...)"
            style={{ border: "none", outline: "none", flex: 1, fontSize: 15 }} />
        </div>
        <button onClick={() => setShowCreate(true)}
          style={{ marginTop: 10, background: "rgba(255,255,255,0.25)", border: "none", color: "white",
            borderRadius: 10, padding: "8px 14px", fontSize: 13, fontWeight: 600, cursor: "pointer" }}>
          ＋ Không tìm thấy? Tạo món mới
        </button>
      </div>

      {showCreate && <CreateFoodForm onClose={() => setShowCreate(false)} onCreated={f => { setShowCreate(false); setQ(f.name); }} />}

      <div style={{ overflowY: "auto", flex: 1 }}>
        {foods.length === 0 && (
          <div style={{ padding: 40, textAlign: "center", color: "#9ca3af" }}>
            Không có món nào khớp.<br />Bấm "Tạo món mới" để thêm.
          </div>
        )}
        {foods.map(food => (
          <div key={food.id} style={{ padding: "12px 20px", display: "flex", alignItems: "center", gap: 10, borderBottom: "1px solid #f3f4f6" }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 600, fontSize: 15 }}>{food.name}</div>
              <div style={{ fontSize: 12, color: "#6b7280", marginTop: 2 }}>
                {food.cal} kcal/{food.unit} · C{food.carbs} P{food.protein} F{food.fat}
              </div>
            </div>
            <Stepper value={qty[food.id] || 1} onChange={v => setQty(p => ({ ...p, [food.id]: v }))} />
            <button onClick={() => add(food)}
              style={{ background: "#22c55e", color: "white", border: "none", borderRadius: 10, padding: "8px 14px", fontSize: 13, fontWeight: 600, cursor: "pointer" }}>
              Thêm
            </button>
          </div>
        ))}
      </div>
    </Sheet>
  );
}

function CreateFoodForm({ onClose, onCreated }) {
  const [f, setF] = useState({ name: "", cal: "", carbs: "", protein: "", fat: "", unit: "phần" });
  const s = (k, v) => setF(p => ({ ...p, [k]: v }));
  async function save() {
    const food = await api.createFood({
      name: f.name, cal: +f.cal || 0, carbs: +f.carbs || 0,
      protein: +f.protein || 0, fat: +f.fat || 0, unit: f.unit, category: "custom",
    });
    onCreated(food);
  }
  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", zIndex: 1100, display: "flex", alignItems: "center", justifyContent: "center", padding: 20 }}>
      <div style={{ background: "white", borderRadius: 16, padding: 20, width: "100%", maxWidth: 360 }}>
        <h3 style={{ margin: "0 0 16px" }}>Tạo món mới</h3>
        <input placeholder="Tên món" value={f.name} onChange={e => s("name", e.target.value)}
          style={inputStyle} />
        <div style={{ display: "flex", gap: 8, marginTop: 10 }}>
          <input placeholder="Kcal" type="number" value={f.cal} onChange={e => s("cal", e.target.value)} style={inputStyle} />
          <input placeholder="Đơn vị" value={f.unit} onChange={e => s("unit", e.target.value)} style={inputStyle} />
        </div>
        <div style={{ display: "flex", gap: 8, marginTop: 10 }}>
          {["carbs", "protein", "fat"].map(k => (
            <input key={k} placeholder={k[0].toUpperCase() + k.slice(1) + "(g)"} type="number"
              value={f[k]} onChange={e => s(k, e.target.value)} style={inputStyle} />
          ))}
        </div>
        <div style={{ display: "flex", gap: 8, marginTop: 16 }}>
          <button onClick={onClose} style={{ flex: 1, padding: 12, borderRadius: 10, border: "1.5px solid #e5e7eb", background: "white", cursor: "pointer" }}>Hủy</button>
          <button onClick={save} disabled={!f.name || !f.cal}
            style={{ flex: 1, padding: 12, borderRadius: 10, border: "none", background: "#22c55e", color: "white", fontWeight: 600, cursor: "pointer", opacity: (!f.name || !f.cal) ? 0.5 : 1 }}>Lưu</button>
        </div>
      </div>
    </div>
  );
}

const EXERCISES = [
  { name: "Đi bộ", cph: 280, icon: "🚶" }, { name: "Chạy bộ", cph: 560, icon: "🏃" },
  { name: "Đạp xe", cph: 450, icon: "🚴" }, { name: "Bơi lội", cph: 500, icon: "🏊" },
  { name: "Gym / Tạ", cph: 400, icon: "🏋️" }, { name: "Yoga", cph: 200, icon: "🧘" },
  { name: "Cầu lông", cph: 480, icon: "🏸" }, { name: "Bóng đá", cph: 600, icon: "⚽" },
  { name: "Pickleball", cph: 420, icon: "🏓" }, { name: "Nhảy dây", cph: 700, icon: "⚡" },
];

export function ExerciseModal({ onClose, onAdded, dateKey }) {
  const [mins, setMins] = useState({});
  async function add(ex, i) {
    const m = mins[i] || 30;
    await api.addExercise({ log_date: dateKey, name: ex.name, icon: ex.icon, mins: m, burned: Math.round(ex.cph * m / 60) });
    onAdded();
  }
  return (
    <Sheet color="linear-gradient(135deg,#f97316,#ef4444)" title="🏃 Thêm hoạt động" onClose={onClose}>
      <div style={{ overflowY: "auto", flex: 1 }}>
        {EXERCISES.map((ex, i) => {
          const m = mins[i] || 30;
          return (
            <div key={i} style={{ padding: "12px 20px", display: "flex", alignItems: "center", gap: 12, borderBottom: "1px solid #f3f4f6" }}>
              <span style={{ fontSize: 28 }}>{ex.icon}</span>
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: 600 }}>{ex.name}</div>
                <div style={{ fontSize: 12, color: "#ef4444" }}>🔥 ~{Math.round(ex.cph * m / 60)} kcal</div>
              </div>
              <Stepper value={m} step={10} min={10} suffix="p" onChange={v => setMins(p => ({ ...p, [i]: v }))} />
              <button onClick={() => add(ex, i)} style={{ background: "#f97316", color: "white", border: "none", borderRadius: 10, padding: "8px 12px", fontWeight: 600, cursor: "pointer" }}>＋</button>
            </div>
          );
        })}
      </div>
    </Sheet>
  );
}

// ---- shared bits ----
function Sheet({ color, title, onClose, children }) {
  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", zIndex: 1000, display: "flex", alignItems: "flex-end" }}>
      <div style={{ background: "white", borderRadius: "20px 20px 0 0", width: "100%", maxWidth: 430, margin: "0 auto", maxHeight: "85vh", display: "flex", flexDirection: "column", overflow: "hidden" }}>
        <div style={{ background: color, padding: "16px 20px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <button onClick={onClose} style={{ background: "rgba(255,255,255,0.2)", border: "none", borderRadius: "50%", width: 32, height: 32, color: "white", cursor: "pointer", fontSize: 18 }}>✕</button>
          <span style={{ color: "white", fontWeight: 700, fontSize: 18 }}>{title}</span>
          <div style={{ width: 32 }} />
        </div>
        {children}
      </div>
    </div>
  );
}

function Stepper({ value, onChange, step = 0.5, min = 0.5, suffix = "" }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
      <button onClick={() => onChange(Math.max(min, value - step))}
        style={{ width: 26, height: 26, borderRadius: "50%", border: "1.5px solid #e5e7eb", background: "white", cursor: "pointer", fontWeight: 700 }}>−</button>
      <span style={{ minWidth: 34, textAlign: "center", fontSize: 13, fontWeight: 600 }}>{value}{suffix}</span>
      <button onClick={() => onChange(value + step)}
        style={{ width: 26, height: 26, borderRadius: "50%", border: "none", background: "#22c55e", color: "white", cursor: "pointer", fontWeight: 700 }}>＋</button>
    </div>
  );
}

const inputStyle = { flex: 1, width: "100%", padding: "10px 12px", border: "1.5px solid #e5e7eb", borderRadius: 8, fontSize: 14, boxSizing: "border-box", outline: "none" };
