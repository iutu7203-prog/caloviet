import { useState } from "react";
import { api, setToken } from "../lib/api";

const GREEN = "#16a34a";
const FONT = "'Be Vietnam Pro', sans-serif";

export default function AuthPage({ onAuthed }) {
  const [mode, setMode] = useState("login"); // login | register | forgot | reset
  const [form, setForm] = useState({ email: "", password: "", name: "", code: "", newPw: "", newPw2: "" });
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState(null);   // { type: "ok"|"err", text }
  const [resetCode, setResetCode] = useState(""); // code returned by server (dev mode)

  const s = (k, v) => setForm(p => ({ ...p, [k]: v }));
  const inp = (k, placeholder, type = "text") => (
    <input
      type={type} placeholder={placeholder} value={form[k]}
      onChange={e => s(k, e.target.value)}
      style={{ width: "100%", padding: "11px 14px", border: "1.5px solid #d1fae5", borderRadius: 10, fontSize: 14, fontFamily: FONT, outline: "none", boxSizing: "border-box", background: "#f0fdf4" }}
    />
  );

  async function handleLogin() {
    if (!form.email || !form.password) return setMsg({ type: "err", text: "Vui lòng điền đủ thông tin" });
    setLoading(true); setMsg(null);
    try {
      const r = await api.login(form.email, form.password);
      setToken(r.access_token);
      onAuthed();
    } catch (e) { setMsg({ type: "err", text: e.message }); }
    finally { setLoading(false); }
  }

  async function handleRegister() {
    if (!form.email || !form.password || !form.name)
      return setMsg({ type: "err", text: "Vui lòng điền đủ họ tên, email và mật khẩu" });
    if (form.password.length < 6)
      return setMsg({ type: "err", text: "Mật khẩu phải có ít nhất 6 ký tự" });
    setLoading(true); setMsg(null);
    try {
      const r = await api.register(form.email, form.password, form.name);
      setToken(r.access_token);
      onAuthed();
    } catch (e) { setMsg({ type: "err", text: e.message }); }
    finally { setLoading(false); }
  }

  async function handleForgot() {
    if (!form.email) return setMsg({ type: "err", text: "Nhập email của bạn" });
    setLoading(true); setMsg(null);
    try {
      const r = await api.forgotPassword(form.email);
      setResetCode(r.code || "");
      setMsg({ type: "ok", text: r.message });
      if (r.code) setMode("reset");
    } catch (e) { setMsg({ type: "err", text: e.message }); }
    finally { setLoading(false); }
  }

  async function handleReset() {
    if (!form.code || !form.newPw)
      return setMsg({ type: "err", text: "Nhập mã xác nhận và mật khẩu mới" });
    if (form.newPw !== form.newPw2)
      return setMsg({ type: "err", text: "Mật khẩu mới không khớp" });
    if (form.newPw.length < 6)
      return setMsg({ type: "err", text: "Mật khẩu phải có ít nhất 6 ký tự" });
    setLoading(true); setMsg(null);
    try {
      const r = await api.resetPassword(form.email, form.code, form.newPw);
      setMsg({ type: "ok", text: r.message });
      setTimeout(() => { setMode("login"); setMsg(null); }, 2000);
    } catch (e) { setMsg({ type: "err", text: e.message }); }
    finally { setLoading(false); }
  }

  const titles = { login: "Đăng nhập", register: "Tạo tài khoản", forgot: "Quên mật khẩu", reset: "Đặt lại mật khẩu" };

  return (
    <div style={{ minHeight: "100vh", background: `linear-gradient(160deg,#14532d,${GREEN},#bbf7d0)`, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "0 16px", fontFamily: FONT }}>
      {/* Logo */}
      <div style={{ textAlign: "center", marginBottom: 28 }}>
        <div style={{ fontSize: 48, marginBottom: 8 }}>🥗</div>
        <div style={{ color: "white", fontSize: 28, fontWeight: 800, letterSpacing: -0.5 }}>CaloViet</div>
        <div style={{ color: "rgba(255,255,255,0.75)", fontSize: 13, marginTop: 4 }}>Theo dõi dinh dưỡng thông minh</div>
      </div>

      {/* Card */}
      <div style={{ background: "white", borderRadius: 24, padding: 28, width: "100%", maxWidth: 400, boxShadow: "0 20px 60px rgba(0,0,0,0.15)" }}>
        <h2 style={{ fontSize: 20, fontWeight: 800, marginBottom: 20, color: "#14532d" }}>{titles[mode]}</h2>

        {/* Thông báo */}
        {msg && (
          <div style={{ background: msg.type === "ok" ? "#f0fdf4" : "#fef2f2", border: `1.5px solid ${msg.type === "ok" ? "#86efac" : "#fca5a5"}`, color: msg.type === "ok" ? "#166534" : "#dc2626", borderRadius: 10, padding: "10px 14px", fontSize: 13, marginBottom: 16, fontWeight: 500 }}>
            {msg.type === "ok" ? "✅ " : "❌ "}{msg.text}
          </div>
        )}

        {/* Hiển thị mã OTP cho dev (production: gửi qua email) */}
        {resetCode && mode === "reset" && (
          <div style={{ background: "#fef9c3", border: "1.5px solid #fde047", borderRadius: 10, padding: "10px 14px", fontSize: 13, marginBottom: 16 }}>
            <div style={{ fontWeight: 700, color: "#713f12" }}>⚠️ Chế độ phát triển</div>
            <div style={{ color: "#854d0e", marginTop: 4 }}>Mã xác nhận: <b style={{ fontSize: 18, letterSpacing: 3 }}>{resetCode}</b></div>
            <div style={{ color: "#a16207", fontSize: 11, marginTop: 4 }}>Production: mã gửi qua email, không hiển thị ở đây</div>
          </div>
        )}

        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {/* Register */}
          {mode === "register" && inp("name", "Họ và tên")}

          {/* Login + Register + Forgot */}
          {(mode === "login" || mode === "register" || mode === "forgot") && inp("email", "Email", "email")}

          {/* Login + Register */}
          {(mode === "login" || mode === "register") && inp("password", "Mật khẩu", "password")}

          {/* Reset */}
          {mode === "reset" && (
            <>
              {inp("code", "Mã xác nhận 6 số")}
              {inp("newPw", "Mật khẩu mới", "password")}
              {inp("newPw2", "Xác nhận mật khẩu mới", "password")}
            </>
          )}

          {/* Submit button */}
          <button
            onClick={mode === "login" ? handleLogin : mode === "register" ? handleRegister : mode === "forgot" ? handleForgot : handleReset}
            disabled={loading}
            style={{ background: `linear-gradient(90deg,#15803d,${GREEN})`, color: "white", border: "none", borderRadius: 12, padding: 13, fontSize: 15, fontWeight: 700, cursor: loading ? "default" : "pointer", opacity: loading ? 0.7 : 1, fontFamily: FONT }}>
            {loading ? "Đang xử lý..." :
              mode === "login" ? "Đăng nhập →" :
              mode === "register" ? "Tạo tài khoản →" :
              mode === "forgot" ? "Gửi mã xác nhận" :
              "Đặt lại mật khẩu"}
          </button>
        </div>

        {/* Nav links */}
        <div style={{ marginTop: 20, textAlign: "center", display: "flex", flexDirection: "column", gap: 8 }}>
          {mode === "login" && (
            <>
              <button onClick={() => { setMode("forgot"); setMsg(null); }}
                style={linkStyle}>Quên mật khẩu?</button>
              <button onClick={() => { setMode("register"); setMsg(null); }}
                style={linkStyle}>Chưa có tài khoản? <b>Đăng ký</b></button>
            </>
          )}
          {mode === "register" && (
            <button onClick={() => { setMode("login"); setMsg(null); }} style={linkStyle}>
              Đã có tài khoản? <b>Đăng nhập</b>
            </button>
          )}
          {(mode === "forgot" || mode === "reset") && (
            <button onClick={() => { setMode("login"); setMsg(null); setResetCode(""); }} style={linkStyle}>
              ← Quay lại đăng nhập
            </button>
          )}
          {mode === "forgot" && (
            <button onClick={() => { setMode("reset"); setMsg(null); }} style={{ ...linkStyle, color: GREEN }}>
              Đã có mã xác nhận? Nhập mã →
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

const linkStyle = {
  background: "none", border: "none", color: "#6b7280", fontSize: 13,
  cursor: "pointer", fontFamily: "'Be Vietnam Pro', sans-serif",
};
