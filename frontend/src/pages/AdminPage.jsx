import { useState, useEffect } from "react";
import { api } from "../lib/api";

const GREEN = "#16a34a";
const FONT = "'Be Vietnam Pro', sans-serif";

export default function AdminPage({ onBack }) {
  const [users, setUsers] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [msg, setMsg] = useState(null);
  const [confirmDelete, setConfirmDelete] = useState(null);
  const [resetResult, setResetResult] = useState(null); // { name, password }

  useEffect(() => { loadData(); }, []);

  async function loadData() {
    setLoading(true);
    try {
      const [u, s] = await Promise.all([api.adminUsers(), api.adminStats()]);
      setUsers(u);
      setStats(s);
    } catch (e) { setMsg({ type: "err", text: e.message }); }
    finally { setLoading(false); }
  }

  async function deleteUser(user) {
    try {
      await api.adminDeleteUser(user.id);
      setMsg({ type: "ok", text: `Đã xóa tài khoản ${user.email}` });
      setConfirmDelete(null);
      loadData();
    } catch (e) { setMsg({ type: "err", text: e.message }); }
  }

  async function resetPw(user) {
    try {
      const r = await api.adminResetPassword(user.id);
      setResetResult({ name: user.name || user.email, password: r.new_password });
    } catch (e) { setMsg({ type: "err", text: e.message }); }
  }

  async function toggleAdmin(user) {
    try {
      await api.adminToggleAdmin(user.id);
      loadData();
    } catch (e) { setMsg({ type: "err", text: e.message }); }
  }

  const goalLabel = { lose: "Giảm cân", maintain: "Duy trì", gain: "Tăng cân" };

  return (
    <div style={{ padding: "48px 16px 16px", fontFamily: FONT }}>
      {/* Header */}
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 16 }}>
        <button onClick={onBack} style={{ background: "#f0fdf4", border: "none", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontSize: 18 }}>←</button>
        <h2 style={{ fontSize: 20, fontWeight: 800, color: "#14532d" }}>🛡️ Quản lý tài khoản</h2>
      </div>

      {/* Thông báo */}
      {msg && (
        <div style={{ background: msg.type === "ok" ? "#f0fdf4" : "#fef2f2", border: `1.5px solid ${msg.type === "ok" ? "#86efac" : "#fca5a5"}`, color: msg.type === "ok" ? "#166534" : "#dc2626", borderRadius: 10, padding: "10px 14px", fontSize: 13, marginBottom: 12, fontWeight: 500 }}>
          {msg.type === "ok" ? "✅ " : "❌ "}{msg.text}
          <button onClick={() => setMsg(null)} style={{ float: "right", background: "none", border: "none", cursor: "pointer", fontSize: 14, color: "inherit" }}>✕</button>
        </div>
      )}

      {/* Popup mật khẩu mới */}
      {resetResult && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", zIndex: 200, display: "flex", alignItems: "center", justifyContent: "center", padding: 16 }}>
          <div style={{ background: "white", borderRadius: 20, padding: 24, width: "100%", maxWidth: 360, fontFamily: FONT }}>
            <h3 style={{ fontSize: 16, fontWeight: 800, color: "#14532d", marginBottom: 12 }}>🔑 Mật khẩu mới</h3>
            <p style={{ fontSize: 13, color: "#6b7280", marginBottom: 12 }}>Mật khẩu tạm thời cho <b>{resetResult.name}</b>:</p>
            <div style={{ background: "#f0fdf4", border: "1.5px solid #86efac", borderRadius: 10, padding: "12px 16px", fontSize: 20, fontWeight: 800, color: GREEN, letterSpacing: 2, textAlign: "center", marginBottom: 16 }}>
              {resetResult.password}
            </div>
            <p style={{ fontSize: 12, color: "#9ca3af", marginBottom: 16 }}>⚠️ Ghi lại ngay. Sau khi đóng cửa sổ này bạn không thể xem lại.</p>
            <button onClick={() => setResetResult(null)} style={{ width: "100%", background: GREEN, color: "white", border: "none", borderRadius: 10, padding: 12, fontWeight: 700, cursor: "pointer", fontFamily: FONT }}>Đã ghi lại</button>
          </div>
        </div>
      )}

      {/* Popup xác nhận xóa */}
      {confirmDelete && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", zIndex: 200, display: "flex", alignItems: "center", justifyContent: "center", padding: 16 }}>
          <div style={{ background: "white", borderRadius: 20, padding: 24, width: "100%", maxWidth: 340, fontFamily: FONT }}>
            <h3 style={{ fontSize: 16, fontWeight: 800, color: "#dc2626", marginBottom: 8 }}>🗑️ Xóa tài khoản</h3>
            <p style={{ fontSize: 14, color: "#374151", marginBottom: 16 }}>Xóa tài khoản <b>{confirmDelete.email}</b>? Thao tác này không thể hoàn tác.</p>
            <div style={{ display: "flex", gap: 10 }}>
              <button onClick={() => setConfirmDelete(null)} style={{ flex: 1, background: "#f3f4f6", border: "none", borderRadius: 10, padding: 11, fontWeight: 600, cursor: "pointer", fontFamily: FONT }}>Hủy</button>
              <button onClick={() => deleteUser(confirmDelete)} style={{ flex: 1, background: "#ef4444", color: "white", border: "none", borderRadius: 10, padding: 11, fontWeight: 700, cursor: "pointer", fontFamily: FONT }}>Xóa</button>
            </div>
          </div>
        </div>
      )}

      {/* Thống kê tổng quan */}
      {stats && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 10, marginBottom: 16 }}>
          {[
            ["👥", stats.total_users, "Người dùng"],
            ["📝", stats.total_diary_entries, "Nhật ký"],
            ["🍜", stats.total_foods, "Món ăn"],
          ].map(([icon, val, label]) => (
            <div key={label} style={{ background: "white", borderRadius: 14, padding: "12px 8px", textAlign: "center", boxShadow: "0 1px 8px rgba(0,0,0,0.05)" }}>
              <div style={{ fontSize: 20 }}>{icon}</div>
              <div style={{ fontSize: 20, fontWeight: 800, color: GREEN }}>{val}</div>
              <div style={{ fontSize: 10, color: "#9ca3af", marginTop: 2 }}>{label}</div>
            </div>
          ))}
        </div>
      )}

      {/* Danh sách users */}
      {loading ? (
        <div style={{ textAlign: "center", padding: 40, color: "#9ca3af" }}>Đang tải...</div>
      ) : (
        users.map(u => (
          <div key={u.id} style={{ background: "white", borderRadius: 16, padding: 16, marginBottom: 10, boxShadow: "0 1px 8px rgba(0,0,0,0.05)" }}>
            {/* Row 1: avatar + name + badges */}
            <div style={{ display: "flex", alignItems: "flex-start", gap: 12, marginBottom: 10 }}>
              <div style={{ width: 40, height: 40, borderRadius: "50%", background: u.is_admin ? `linear-gradient(135deg,#fbbf24,#f59e0b)` : `linear-gradient(135deg,#86efac,${GREEN})`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 18, flexShrink: 0 }}>
                {u.is_admin ? "🛡️" : "👤"}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontSize: 14, fontWeight: 700, color: "#14532d", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  {u.name || "Chưa đặt tên"}
                  {u.is_admin && <span style={{ fontSize: 10, background: "#fef3c7", color: "#92400e", borderRadius: 6, padding: "2px 6px", marginLeft: 6, fontWeight: 700 }}>ADMIN</span>}
                </div>
                <div style={{ fontSize: 12, color: "#6b7280", marginTop: 2, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{u.email}</div>
                <div style={{ fontSize: 11, color: "#9ca3af", marginTop: 1 }}>
                  {u.age} tuổi · {u.weight}kg · {u.height}cm · {goalLabel[u.goal] || u.goal} · {u.target_cal} kcal
                </div>
              </div>
              <div style={{ fontSize: 11, color: "#9ca3af", whiteSpace: "nowrap" }}>{u.created_at}</div>
            </div>

            {/* Row 2: action buttons */}
            <div style={{ display: "flex", gap: 6 }}>
              <button onClick={() => resetPw(u)}
                style={{ flex: 1, background: "#eff6ff", color: "#3b82f6", border: "none", borderRadius: 8, padding: "7px 4px", fontSize: 11, fontWeight: 700, cursor: "pointer", fontFamily: FONT }}>
                🔑 Cấp lại MK
              </button>
              <button onClick={() => toggleAdmin(u)}
                style={{ flex: 1, background: u.is_admin ? "#fef3c7" : "#f0fdf4", color: u.is_admin ? "#92400e" : "#166534", border: "none", borderRadius: 8, padding: "7px 4px", fontSize: 11, fontWeight: 700, cursor: "pointer", fontFamily: FONT }}>
                {u.is_admin ? "⬇️ Bỏ Admin" : "⬆️ Cấp Admin"}
              </button>
              <button onClick={() => setConfirmDelete(u)}
                style={{ background: "#fef2f2", color: "#ef4444", border: "none", borderRadius: 8, padding: "7px 10px", fontSize: 14, cursor: "pointer" }}>
                🗑️
              </button>
            </div>
          </div>
        ))
      )}
    </div>
  );
}
