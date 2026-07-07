import { useState, useEffect, useCallback } from "react";
import { api, hasToken, clearToken } from "./lib/api";
import AdminPage from "./pages/AdminPage";
import AuthPage from "./pages/AuthPage";
import { CircleProgress, MacroBar } from "./components/ui";
import { FoodSearchModal, ExerciseModal } from "./components/modals";

const FONT = "'Be Vietnam Pro', sans-serif";
const GREEN = "#16a34a";
const GREEN_LIGHT = "#dcfce7";
const GREEN_MID = "#22c55e";

const MEALS = [
  ["breakfast", "Bữa sáng"], ["lunch", "Bữa trưa"],
  ["dinner", "Bữa tối"], ["snack", "Ăn vặt"],
];

// Tính thứ Hai của tuần chứa ngày d
function getMondayOf(d) {
  const day = new Date(d);
  day.setDate(day.getDate() - day.getDay() + (day.getDay() === 0 ? -6 : 1));
  return day;
}
function toDateKey(d) { return d.toISOString().split("T")[0]; }
function fmtShort(d) {
  return d.toLocaleDateString("vi-VN", { day: "2-digit", month: "2-digit" });
}
function fmtFull(d) {
  return d.toLocaleDateString("vi-VN", { day: "2-digit", month: "2-digit", year: "numeric" });
}

export default function App() {
  const [authed, setAuthed] = useState(hasToken());
  const [profile, setProfile] = useState(null);
  const [needSetup, setNeedSetup] = useState(false);
  const [tab, setTab] = useState("home");
  const [day, setDay] = useState(null);
  const [week, setWeek] = useState(null);
  const [modal, setModal] = useState(null);
  const [offset, setOffset] = useState(0);
  // Stats: tuần hiện tại (0 = tuần này, -1 = tuần trước, ...)
  const [weekOffset, setWeekOffset] = useState(0);
  const [pickerDate, setPickerDate] = useState("");
  const [showAdmin, setShowAdmin] = useState(false);
  const [showChangePw, setShowChangePw] = useState(false);
  const [cpForm, setCpForm] = useState({ cur: "", n1: "", n2: "" });
  const [cpMsg, setCpMsg] = useState(null);

  const dateKey = (() => { const d = new Date(); d.setDate(d.getDate() + offset); return d.toISOString().split("T")[0]; })();
  const dateLabel = offset === 0 ? "Hôm nay" : new Date(Date.now() + offset * 86400000).toLocaleDateString("vi-VN", { day: "2-digit", month: "short" });

  // Tính monday của tuần đang xem trong stats
  const statsMonday = (() => {
    const base = getMondayOf(new Date());
    base.setDate(base.getDate() + weekOffset * 7);
    return base;
  })();
  const statsSunday = new Date(statsMonday);
  statsSunday.setDate(statsSunday.getDate() + 6);
  const statsWeekStart = toDateKey(statsMonday);

  const isCurrentWeek = weekOffset === 0;
  const weekLabel = isCurrentWeek ? "Tuần này" :
    weekOffset === -1 ? "Tuần trước" :
    `${fmtShort(statsMonday)} – ${fmtShort(statsSunday)}`;

  const loadProfile = useCallback(async () => {
    try {
      const p = await api.me();
      setProfile(p);
      if (!p.name || (p.height === 165 && p.weight === 60)) setNeedSetup(true);
    } catch { clearToken(); setAuthed(false); }
  }, []);

  const loadDay = useCallback(async () => {
    try { setDay(await api.day(dateKey)); } catch {}
  }, [dateKey]);

  const loadWeek = useCallback(async () => {
    try { setWeek(await api.week(statsWeekStart)); } catch {}
  }, [statsWeekStart]);

  useEffect(() => { if (authed) loadProfile(); }, [authed, loadProfile]);
  useEffect(() => { if (authed) loadDay(); }, [authed, loadDay]);
  useEffect(() => { if (authed && tab === "stats") loadWeek(); }, [authed, tab, loadWeek]);

  async function handleChangePw() {
    if (!cpForm.cur || !cpForm.n1 || !cpForm.n2)
      return setCpMsg({ type: "err", text: "Điền đủ các trường" });
    if (cpForm.n1 !== cpForm.n2)
      return setCpMsg({ type: "err", text: "Mật khẩu mới không khớp" });
    if (cpForm.n1.length < 6)
      return setCpMsg({ type: "err", text: "Mật khẩu phải từ 6 ký tự" });
    try {
      await api.changePassword(cpForm.cur, cpForm.n1);
      setCpMsg({ type: "ok", text: "Đổi mật khẩu thành công!" });
      setCpForm({ cur: "", n1: "", n2: "" });
      setTimeout(() => setShowChangePw(false), 1500);
    } catch (e) { setCpMsg({ type: "err", text: e.message }); }
  }

  if (!authed) return <AuthPage onAuthed={() => setAuthed(true)} />;
  if (!profile) return <Center>Đang tải...</Center>;
  if (needSetup) return (
    <ProfileSetup profile={profile} onDone={async d => {
      await api.updateProfile(d); await loadProfile(); setNeedSetup(false);
    }} />
  );

  const goalCarbs = Math.round(profile.target_cal * 0.5 / 4);
  const goalProtein = Math.round(profile.weight * 1.6);
  const goalFat = Math.round(profile.target_cal * 0.25 / 9);

  async function water(dir) {
    const next = Math.max(0, (day?.water || 0) + dir * 250);
    await api.setWater(next, dateKey);
    loadDay();
  }

  function handlePickerChange(e) {
    const val = e.target.value;
    setPickerDate(val);
    if (!val) return;
    const picked = getMondayOf(new Date(val));
    const thisMonday = getMondayOf(new Date());
    const diff = Math.round((picked - thisMonday) / (7 * 86400000));
    setWeekOffset(diff);
  }

  return (
    <div style={{ maxWidth: 430, margin: "0 auto", minHeight: "100vh", background: "#f0fdf4", fontFamily: FONT, paddingBottom: 80, position: "relative" }}>

      {/* ── HOME ── */}
      {tab === "home" && day && (
        <>
          <div style={{ background: `linear-gradient(160deg,#15803d,${GREEN_MID})`, padding: "calc(52px + env(safe-area-inset-top)) 20px 36px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 20 }}>
              <div>
                <div style={{ color: "rgba(255,255,255,0.75)", fontSize: 13, fontWeight: 500 }}>Xin chào,</div>
                <div style={{ color: "white", fontSize: 20, fontWeight: 700 }}>{profile.name || "Bạn ơi"} 👋</div>
              </div>
              <NavBtn onClick={() => setOffset(o => o - 1)}>‹</NavBtn>
            </div>
            <div style={{ textAlign: "center", marginBottom: 20 }}>
              <div style={{ color: "rgba(255,255,255,0.8)", fontSize: 13, marginBottom: 4 }}>{dateLabel}</div>
              <div style={{ display: "flex", justifyContent: "center" }}>
                <CircleProgress
                  value={day.remaining} max={profile.target_cal}
                  label="kcal còn lại" size={130}
                />
              </div>
            </div>
            <div style={{ display: "flex", justifyContent: "space-around" }}>
              <Stat label="Carbs" value={`${Math.round(day.carbs)}g`} />
              <Stat label="Protein" value={`${Math.round(day.protein)}g`} />
              <Stat label="Fat" value={`${Math.round(day.fat)}g`} />
            </div>
            <div style={{ display: "flex", justifyContent: "flex-end", marginTop: 8 }}>
              <NavBtn onClick={() => setOffset(o => Math.min(0, o + 1))}>›</NavBtn>
            </div>
          </div>

          <div style={{ padding: "16px 16px 0" }}>
            {/* macros */}
            <Card>
              <b style={{ fontSize: 14, color: "#166534" }}>Dinh dưỡng hôm nay</b>
              <div style={{ marginTop: 12, display: "flex", flexDirection: "column", gap: 8 }}>
                <MacroBar label="Carbs" current={day.carbs} max={goalCarbs} />
                <MacroBar label="Protein" current={day.protein} max={goalProtein} />
                <MacroBar label="Fat" current={day.fat} max={goalFat} />
              </div>
            </Card>

            {/* water */}
            <Card>
              <Row>
                <span style={{ fontSize: 14, fontWeight: 600, color: "#166534" }}>💧 Nước uống</span>
                <span style={{ fontSize: 13, color: "#6b7280" }}>{day.water} / {profile.water_goal} ml</span>
              </Row>
              <div style={{ display: "flex", alignItems: "center", gap: 10, marginTop: 10 }}>
                <RoundBtn onClick={() => water(-1)} light>−</RoundBtn>
                <div style={{ flex: 1, background: "#e0f2fe", borderRadius: 8, height: 8, overflow: "hidden" }}>
                  <div style={{ width: `${Math.min(100, (day.water / (profile.water_goal || 2000)) * 100)}%`, background: "#3b82f6", height: "100%", borderRadius: 8, transition: "width 0.3s" }} />
                </div>
                <RoundBtn onClick={() => water(1)}>＋</RoundBtn>
              </div>
            </Card>

            {/* exercises */}
            {day.exercises?.length > 0 && (
              <Card>
                <Row><b style={{ fontSize: 14, color: "#166534" }}>🏃 Vận động</b></Row>
                {day.exercises.map((ex, i) => (
                  <Row key={ex.id} border={i < day.exercises.length - 1} pad>
                    <div>
                      <div style={{ fontSize: 14, fontWeight: 600 }}>{ex.name}</div>
                      <div style={{ fontSize: 12, color: "#6b7280" }}>{ex.mins} phút · −{Math.round(ex.burned)} kcal</div>
                    </div>
                    <Trash onClick={async () => { await api.deleteExercise(ex.id); loadDay(); }} />
                  </Row>
                ))}
              </Card>
            )}
            <button onClick={() => setModal({ type: "exercise" })}
              style={{ width: "100%", marginBottom: 12, background: "white", border: `1.5px dashed ${GREEN}`, color: GREEN, borderRadius: 12, padding: 11, fontSize: 13, fontWeight: 600, cursor: "pointer" }}>
              ＋ Thêm bài tập
            </button>

            {/* meals */}
            {MEALS.map(([key, label]) => {
              const items = day.entries?.filter(e => e.meal === key) || [];
              const cal = items.reduce((s, e) => s + e.cal * e.qty, 0);
              return (
                <Card key={key}>
                  <Row>
                    <div>
                      <b style={{ fontSize: 14, color: "#166534" }}>{label}</b>
                      {cal > 0 && <span style={{ fontSize: 12, color: GREEN_MID, marginLeft: 8, fontWeight: 600 }}>{Math.round(cal)} kcal</span>}
                    </div>
                    <button onClick={() => setModal({ type: "food", meal: key })}
                      style={{ background: GREEN, color: "white", border: "none", borderRadius: 8, padding: "5px 12px", fontSize: 13, fontWeight: 600, cursor: "pointer" }}>＋ Thêm</button>
                  </Row>
                  {items.map((e, i) => (
                    <Row key={e.id} border={i < items.length - 1} pad>
                      <div>
                        <div style={{ fontSize: 13, fontWeight: 600 }}>{e.food_name}</div>
                        <div style={{ fontSize: 12, color: "#6b7280" }}>{e.qty} {e.unit} · {Math.round(e.cal * e.qty)} kcal</div>
                      </div>
                      <button onClick={async () => { await api.deleteEntry(e.id); loadDay(); }}
                        style={{ background: "none", border: "none", color: "#d1d5db", cursor: "pointer", fontSize: 15 }}>✕</button>
                    </Row>
                  ))}
                </Card>
              );
            })}
          </div>
        </>
      )}

      {/* ── STATS ── */}
      {tab === "stats" && (
        <div style={{ padding: "calc(48px + env(safe-area-inset-top)) 16px 16px" }}>
          <h2 style={{ fontSize: 20, fontWeight: 800, marginBottom: 16, color: "#14532d" }}>📊 Thống kê</h2>

          {/* Week navigator */}
          <Card>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12 }}>
              <button onClick={() => setWeekOffset(w => w - 1)}
                style={{ background: GREEN_LIGHT, border: "none", color: GREEN, borderRadius: 8, width: 34, height: 34, fontSize: 18, cursor: "pointer", fontWeight: 700 }}>‹</button>
              <div style={{ textAlign: "center" }}>
                <div style={{ fontSize: 15, fontWeight: 700, color: "#14532d" }}>{weekLabel}</div>
                <div style={{ fontSize: 12, color: "#6b7280", marginTop: 2 }}>
                  {fmtFull(statsMonday)} – {fmtFull(statsSunday)}
                </div>
              </div>
              <button onClick={() => setWeekOffset(w => Math.min(0, w + 1))}
                disabled={isCurrentWeek}
                style={{ background: isCurrentWeek ? "#f3f4f6" : GREEN_LIGHT, border: "none", color: isCurrentWeek ? "#d1d5db" : GREEN, borderRadius: 8, width: 34, height: 34, fontSize: 18, cursor: isCurrentWeek ? "default" : "pointer", fontWeight: 700 }}>›</button>
            </div>

            {/* Date picker */}
            <div style={{ display: "flex", alignItems: "center", gap: 8, background: "#f0fdf4", border: "1.5px solid #bbf7d0", borderRadius: 10, padding: "8px 12px" }}>
              <span style={{ fontSize: 13, color: "#6b7280", whiteSpace: "nowrap" }}>Chọn ngày:</span>
              <input
                type="date"
                value={pickerDate}
                onChange={handlePickerChange}
                max={toDateKey(new Date())}
                style={{ flex: 1, border: "none", background: "transparent", fontSize: 13, color: "#166534", fontFamily: FONT, outline: "none", cursor: "pointer" }}
              />
              {pickerDate && (
                <button onClick={() => { setPickerDate(""); setWeekOffset(0); }}
                  style={{ background: "none", border: "none", color: "#9ca3af", cursor: "pointer", fontSize: 14, padding: "0 2px" }}>✕</button>
              )}
            </div>
          </Card>

          {week ? (
            <>
              {/* Bar chart */}
              <Card>
                <b style={{ fontSize: 14, color: "#166534" }}>Calo theo ngày</b>
                <div style={{ display: "flex", gap: 6, alignItems: "flex-end", height: 130, marginTop: 16 }}>
                  {week.days.map((d, i) => {
                    const max = Math.max(...week.days.map(x => x.cal), week.target_cal, 1);
                    const over = d.cal > week.target_cal;
                    const isToday = d.date === toDateKey(new Date());
                    return (
                      <div key={i} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 3 }}>
                        <div style={{ fontSize: 9, color: d.cal === 0 ? "transparent" : over ? "#ef4444" : GREEN, fontWeight: 600 }}>
                          {d.cal > 0 ? (d.cal >= 1000 ? (d.cal / 1000).toFixed(1) + "k" : d.cal) : "·"}
                        </div>
                        <div style={{
                          width: "100%",
                          background: d.cal === 0 ? "#e5e7eb" : over ? "#fca5a5" : "#86efac",
                          borderRadius: "4px 4px 0 0",
                          height: `${max ? Math.max(4, (d.cal / max) * 88) : 4}px`,
                          border: isToday ? `2px solid ${GREEN}` : "none",
                          transition: "height 0.4s",
                          position: "relative",
                        }}>
                          {d.cal > 0 && <div style={{ position: "absolute", top: 0, left: 0, right: 0, bottom: 0, background: over ? "#ef4444" : GREEN, opacity: 0.7, borderRadius: "2px 2px 0 0" }} />}
                        </div>
                        <div style={{ fontSize: 10, color: isToday ? GREEN : "#6b7280", fontWeight: isToday ? 700 : 400 }}>{d.label}</div>
                        <div style={{ fontSize: 9, color: "#9ca3af" }}>{d.date?.slice(5).replace("-", "/")}</div>
                      </div>
                    );
                  })}
                </div>
                <div style={{ marginTop: 10, fontSize: 11, color: "#6b7280", display: "flex", gap: 12 }}>
                  <span>🟩 Đạt mục tiêu</span>
                  <span>🟥 Vượt ({week.target_cal} kcal)</span>
                </div>
              </Card>

              {/* Summary cards */}
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginBottom: 12 }}>
                <Card style={{ marginBottom: 0 }}>
                  <div style={{ fontSize: 11, color: "#6b7280", marginBottom: 4 }}>🔥 Calo TB/ngày</div>
                  <div style={{ fontSize: 22, fontWeight: 800, color: GREEN }}>{week.avg_cal}</div>
                  <div style={{ fontSize: 11, color: "#9ca3af" }}>mục tiêu {week.target_cal}</div>
                </Card>
                <Card style={{ marginBottom: 0 }}>
                  <div style={{ fontSize: 11, color: "#6b7280", marginBottom: 4 }}>📅 Ngày có log</div>
                  <div style={{ fontSize: 22, fontWeight: 800, color: "#3b82f6" }}>
                    {week.days.filter(d => d.cal > 0).length}
                    <span style={{ fontSize: 13, fontWeight: 500, color: "#9ca3af" }}>/7</span>
                  </div>
                  <div style={{ fontSize: 11, color: "#9ca3af" }}>ngày trong tuần</div>
                </Card>
              </div>

              {/* Daily detail table */}
              <Card>
                <b style={{ fontSize: 14, color: "#166534" }}>Chi tiết từng ngày</b>
                <div style={{ marginTop: 10 }}>
                  {week.days.map((d, i) => {
                    const isToday = d.date === toDateKey(new Date());
                    const pct = week.target_cal > 0 ? Math.round((d.cal / week.target_cal) * 100) : 0;
                    return (
                      <div key={i} style={{
                        display: "flex", alignItems: "center", gap: 10,
                        padding: "8px 0",
                        borderBottom: i < 6 ? "1px solid #f0fdf4" : "none",
                        background: isToday ? "#f0fdf4" : "transparent",
                        borderRadius: isToday ? 8 : 0,
                        paddingLeft: isToday ? 8 : 0,
                      }}>
                        <div style={{ width: 28, textAlign: "center" }}>
                          <div style={{ fontSize: 11, fontWeight: 700, color: isToday ? GREEN : "#374151" }}>{d.label}</div>
                          <div style={{ fontSize: 9, color: "#9ca3af" }}>{d.date?.slice(5).replace("-", "/")}</div>
                        </div>
                        <div style={{ flex: 1, background: "#f3f4f6", borderRadius: 6, height: 7, overflow: "hidden" }}>
                          <div style={{
                            width: `${Math.min(100, pct)}%`,
                            background: d.cal > week.target_cal ? "#ef4444" : GREEN_MID,
                            height: "100%", borderRadius: 6, transition: "width 0.4s",
                          }} />
                        </div>
                        <div style={{ width: 70, textAlign: "right" }}>
                          {d.cal > 0
                            ? <span style={{ fontSize: 13, fontWeight: 700, color: d.cal > week.target_cal ? "#ef4444" : "#166534" }}>{d.cal} kcal</span>
                            : <span style={{ fontSize: 12, color: "#d1d5db" }}>—</span>}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </Card>

              {/* Export */}
              <button onClick={() => api.exportWithToken().catch(e => alert(e.message))}
                style={{ width: "100%", marginTop: 4, background: "white", border: `2px solid ${GREEN}`, color: GREEN, borderRadius: 12, padding: 13, fontSize: 14, fontWeight: 700, cursor: "pointer", fontFamily: FONT }}>
                📥 Xuất file CSV (Excel)
              </button>
            </>
          ) : (
            <Card><div style={{ textAlign: "center", color: "#9ca3af", padding: 20 }}>Đang tải...</div></Card>
          )}
        </div>
      )}

      {/* ── PROFILE ── */}
      {tab === "profile" && showAdmin && (
        <AdminPage onBack={() => setShowAdmin(false)} />
      )}

      {tab === "profile" && !showAdmin && (
        <div style={{ padding: "48px 16px 16px" }}>
          <h2 style={{ fontSize: 20, fontWeight: 800, marginBottom: 16, color: "#14532d" }}>👤 Hồ sơ</h2>
          <div style={{ background: `linear-gradient(135deg,#15803d,${GREEN_MID})`, borderRadius: 20, padding: 24, color: "white", marginBottom: 12 }}>
            <div style={{ fontSize: 36 }}>🙋</div>
            <div style={{ fontSize: 22, fontWeight: 800, marginTop: 4 }}>{profile.name || "Người dùng"}</div>
            <div style={{ opacity: 0.85, marginTop: 4, fontSize: 13 }}>{profile.height} cm · {profile.weight} kg · {profile.age} tuổi</div>
            <div style={{ marginTop: 14, background: "rgba(255,255,255,0.18)", borderRadius: 12, padding: 12 }}>
              <div style={{ fontSize: 12, opacity: 0.8 }}>Mục tiêu calo mỗi ngày</div>
              <div style={{ fontSize: 28, fontWeight: 800 }}>{profile.target_cal} kcal</div>
            </div>
          </div>
          {[
            ["💪 Mục tiêu", { lose: "Giảm cân", gain: "Tăng cân", maintain: "Duy trì" }[profile.goal]],
            ["📏 BMI", (profile.weight / (profile.height / 100) ** 2).toFixed(1)],
            ["💧 Nước mỗi ngày", `${profile.water_goal} ml`],
            ["🥩 Protein mục tiêu", `${goalProtein} g/ngày`],
            ["🍞 Carbs mục tiêu", `${goalCarbs} g/ngày`],
            ["🧈 Fat mục tiêu", `${goalFat} g/ngày`],
          ].map(([k, v]) => (
            <Card key={k}><Row><span style={{ fontSize: 14 }}>{k}</span><b style={{ color: GREEN, fontSize: 14 }}>{v}</b></Row></Card>
          ))}
          <button onClick={() => setNeedSetup(true)}
            style={{ width: "100%", marginTop: 4, background: GREEN, color: "white", border: "none", borderRadius: 12, padding: 13, fontWeight: 700, cursor: "pointer", fontFamily: FONT, fontSize: 14 }}>
            ✏️ Chỉnh sửa hồ sơ
          </button>
          {/* Đổi mật khẩu */}
          <button onClick={() => { setShowChangePw(v => !v); setCpMsg(null); }}
            style={{ width: "100%", marginTop: 4, background: "white", border: "1.5px solid #d1fae5", color: "#166534", borderRadius: 12, padding: 13, fontWeight: 600, cursor: "pointer", fontFamily: FONT, fontSize: 14 }}>
            🔒 {showChangePw ? "Đóng" : "Đổi mật khẩu"}
          </button>

          {showChangePw && (
            <div style={{ background: "#f0fdf4", border: "1.5px solid #86efac", borderRadius: 14, padding: 16, marginTop: 0 }}>
              {cpMsg && (
                <div style={{ fontSize: 12, color: cpMsg.type === "ok" ? "#166534" : "#dc2626", marginBottom: 10, fontWeight: 600 }}>
                  {cpMsg.type === "ok" ? "✅ " : "❌ "}{cpMsg.text}
                </div>
              )}
              {[["cur","Mật khẩu hiện tại"],["n1","Mật khẩu mới"],["n2","Xác nhận mật khẩu mới"]].map(([k,ph]) => (
                <input key={k} type="password" placeholder={ph} value={cpForm[k]}
                  onChange={e => setCpForm(p => ({...p,[k]:e.target.value}))}
                  style={{ width:"100%", padding:"9px 12px", border:"1.5px solid #d1fae5", borderRadius:10, fontSize:13, fontFamily:FONT, marginBottom:8, boxSizing:"border-box", outline:"none", background:"white" }} />
              ))}
              <button onClick={handleChangePw}
                style={{ width:"100%", background:GREEN, color:"white", border:"none", borderRadius:10, padding:11, fontWeight:700, cursor:"pointer", fontFamily:FONT, fontSize:14 }}>
                Xác nhận đổi mật khẩu
              </button>
            </div>
          )}

          {/* Admin panel */}
          {profile?.is_admin && (
            <button onClick={() => setShowAdmin(true)}
              style={{ width: "100%", marginTop: 4, background: "linear-gradient(90deg,#f59e0b,#fbbf24)", color: "#1c1917", border: "none", borderRadius: 12, padding: 13, fontWeight: 700, cursor: "pointer", fontFamily: FONT, fontSize: 14 }}>
              🛡️ Quản lý tài khoản (Admin)
            </button>
          )}

          <button onClick={() => { clearToken(); setAuthed(false); }}
            style={{ width: "100%", marginTop: 10, background: "white", border: "2px solid #ef4444", color: "#ef4444", borderRadius: 12, padding: 13, fontWeight: 700, cursor: "pointer", fontFamily: FONT, fontSize: 14 }}>
            Đăng xuất
          </button>
        </div>
      )}

      {/* Bottom nav */}
      <div style={{ position: "fixed", bottom: 0, left: "50%", transform: "translateX(-50%)", width: "100%", maxWidth: 430, background: "white", borderTop: "1px solid #e5e7eb", display: "flex", padding: "8px 0", paddingBottom: "calc(16px + env(safe-area-inset-bottom))", zIndex: 100, boxShadow: "0 -2px 12px rgba(0,0,0,0.06)" }}>
        {[["home", "🏠", "Trang chủ"], ["stats", "📊", "Thống kê"], ["profile", "👤", "Cá nhân"]].map(([id, icon, label]) => (
          <button key={id} onClick={() => setTab(id)}
            style={{ flex: 1, background: "none", border: "none", cursor: "pointer", display: "flex", flexDirection: "column", alignItems: "center", gap: 3, paddingTop: 4 }}>
            <span style={{ fontSize: 22 }}>{icon}</span>
            <span style={{ fontSize: 11, color: tab === id ? GREEN : "#9ca3af", fontWeight: tab === id ? 700 : 400, fontFamily: FONT }}>{label}</span>
          </button>
        ))}
      </div>

      {modal?.type === "food" && <FoodSearchModal meal={modal.meal} dateKey={dateKey} onClose={() => setModal(null)} onAdded={() => { setModal(null); loadDay(); }} />}
      {modal?.type === "exercise" && <ExerciseModal dateKey={dateKey} onClose={() => setModal(null)} onAdded={() => { setModal(null); loadDay(); }} />}
    </div>
  );
}

// ── Components ──
const Card = ({ children, style }) => (
  <div style={{ background: "white", borderRadius: 16, padding: 16, marginBottom: 12, boxShadow: "0 1px 8px rgba(0,0,0,0.05)", ...style }}>{children}</div>
);
const Row = ({ children, border, pad }) => (
  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: pad ? "8px 0" : 0, borderBottom: border ? "1px solid #f0fdf4" : "none" }}>{children}</div>
);
const Stat = ({ label, value }) => (
  <div style={{ textAlign: "center" }}>
    <div style={{ color: "rgba(255,255,255,0.75)", fontSize: 11, fontWeight: 500 }}>{label}</div>
    <div style={{ color: "white", fontWeight: 700, fontSize: 18 }}>{value}</div>
  </div>
);
const NavBtn = ({ onClick, children }) => (
  <button onClick={onClick} style={{ background: "rgba(255,255,255,0.22)", border: "none", color: "white", borderRadius: 8, padding: "4px 10px", cursor: "pointer", fontSize: 18, fontWeight: 700 }}>{children}</button>
);
const RoundBtn = ({ onClick, light, children }) => (
  <button onClick={onClick} style={{ width: 28, height: 28, borderRadius: "50%", border: light ? "1.5px solid #e5e7eb" : "none", background: light ? "white" : "#3b82f6", color: light ? "#111" : "white", cursor: "pointer", fontSize: 16 }}>{children}</button>
);
const Trash = ({ onClick }) => (
  <button onClick={onClick} style={{ background: "none", border: "none", color: "#d1d5db", cursor: "pointer", fontSize: 15 }}>🗑</button>
);
const Center = ({ children }) => (
  <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", color: "#6b7280", fontFamily: FONT }}>{children}</div>
);

function ProfileSetup({ profile, onDone }) {
  const [f, setF] = useState({
    name: profile.name || "", gender: profile.gender || "female", age: profile.age || 25,
    height: profile.height || 165, weight: profile.weight || 60, goal: profile.goal || "lose",
  });
  const s = (k, v) => setF(p => ({ ...p, [k]: v }));
  return (
    <div style={{ minHeight: "100vh", background: `linear-gradient(160deg,#15803d,${GREEN_MID},#f0fdf4)`, padding: "0 0 40px", fontFamily: FONT }}>
      <div style={{ padding: "60px 24px 20px" }}>
        <h1 style={{ color: "white", fontSize: 24, fontWeight: 800 }}>Thiết lập hồ sơ</h1>
        <p style={{ color: "rgba(255,255,255,0.8)", fontSize: 13, marginTop: 4 }}>Điền thông tin để tính calo chính xác</p>
      </div>
      <div style={{ background: "white", margin: "0 16px", borderRadius: 20, padding: 24 }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          {[["Họ tên", "name", "text"], ["Tuổi", "age", "number"], ["Chiều cao (cm)", "height", "number"], ["Cân nặng (kg)", "weight", "number"]].map(([l, k, t]) => (
            <div key={k}>
              <label style={{ fontSize: 13, color: "#6b7280", display: "block", marginBottom: 4, fontWeight: 500 }}>{l}</label>
              <input type={t} value={f[k]} onChange={e => s(k, t === "number" ? +e.target.value : e.target.value)}
                style={{ width: "100%", padding: "10px 14px", border: "1.5px solid #e5e7eb", borderRadius: 10, fontSize: 15, boxSizing: "border-box", outline: "none", fontFamily: FONT }} />
            </div>
          ))}
          <Choice label="Giới tính" value={f.gender} onChange={v => s("gender", v)} options={[["female", "👩 Nữ"], ["male", "👨 Nam"]]} />
          <Choice label="Mục tiêu" value={f.goal} onChange={v => s("goal", v)} options={[["lose", "⬇️ Giảm"], ["maintain", "⚖️ Duy trì"], ["gain", "⬆️ Tăng"]]} />
          <button onClick={() => onDone(f)} disabled={!f.name}
            style={{ background: `linear-gradient(90deg,#15803d,${GREEN_MID})`, color: "white", border: "none", borderRadius: 12, padding: 14, fontSize: 15, fontWeight: 700, cursor: "pointer", opacity: f.name ? 1 : 0.5, fontFamily: FONT }}>
            Lưu & tiếp tục →
          </button>
        </div>
      </div>
    </div>
  );
}

function Choice({ label, value, onChange, options }) {
  return (
    <div>
      <label style={{ fontSize: 13, color: "#6b7280", display: "block", marginBottom: 6, fontWeight: 500 }}>{label}</label>
      <div style={{ display: "flex", gap: 8 }}>
        {options.map(([v, l]) => (
          <button key={v} onClick={() => onChange(v)}
            style={{ flex: 1, padding: 10, borderRadius: 10, border: `2px solid ${value === v ? GREEN : "#e5e7eb"}`, background: value === v ? GREEN_LIGHT : "white", cursor: "pointer", fontWeight: 600, fontSize: 13, fontFamily: FONT }}>
            {l}
          </button>
        ))}
      </div>
    </div>
  );
}
