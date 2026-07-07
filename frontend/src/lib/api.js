const BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

function getToken() {
  return localStorage.getItem("caloviet_token");
}

async function request(path, { method = "GET", body, form } = {}) {
  const headers = {};
  const token = getToken();
  if (token) headers["Authorization"] = `Bearer ${token}`;

  let payload;
  if (form) {
    payload = new URLSearchParams(form);
    headers["Content-Type"] = "application/x-www-form-urlencoded";
  } else if (body) {
    payload = JSON.stringify(body);
    headers["Content-Type"] = "application/json";
  }

  const res = await fetch(`${BASE}${path}`, { method, headers, body: payload });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Lỗi kết nối" }));
    throw new Error(err.detail || "Có lỗi xảy ra");
  }
  return res.status === 204 ? null : res.json();
}

export const api = {
  // auth
  register: (email, password, name) =>
    request("/auth/register", { method: "POST", body: { email, password, name } }),
  login: (email, password) =>
    request("/auth/login", { method: "POST", form: { username: email, password } }),
  me: () => request("/auth/me"),
  updateProfile: (data) => request("/auth/me", { method: "PUT", body: data }),

  // foods
  searchFoods: (q = "") => request(`/foods?q=${encodeURIComponent(q)}&limit=80`),
  createFood: (data) => request("/foods", { method: "POST", body: data }),

  // diary
  addEntry: (data) => request("/diary/entries", { method: "POST", body: data }),
  deleteEntry: (id) => request(`/diary/entries/${id}`, { method: "DELETE" }),
  setWater: (amount, log_date) => request("/diary/water", { method: "PUT", body: { amount, log_date } }),
  addExercise: (data) => request("/diary/exercises", { method: "POST", body: data }),
  deleteExercise: (id) => request(`/diary/exercises/${id}`, { method: "DELETE" }),
  day: (log_date) => request(`/diary/day${log_date ? `?log_date=${log_date}` : ""}`),

  // stats — truyền weekStart (YYYY-MM-DD) để xem tuần bất kỳ
  week: (weekStart) => request(`/stats/week${weekStart ? `?week_start=${weekStart}` : ""}`),
  exportUrl: () => `${BASE}/stats/export`,
  // auth extras
  forgotPassword: (email) => request("/auth/forgot-password", { method: "POST", body: { email } }),
  resetPassword: (email, code, new_password) =>
    request("/auth/reset-password", { method: "POST", body: { email, code, new_password } }),
  changePassword: (current_password, new_password) =>
    request("/auth/change-password", { method: "PUT", body: { current_password, new_password } }),

  // admin
  adminUsers: () => request("/admin/users"),
  adminStats: () => request("/admin/stats"),
  adminDeleteUser: (id) => request(`/admin/users/${id}`, { method: "DELETE" }),
  adminResetPassword: (id) => request(`/admin/users/${id}/reset-password`, { method: "POST" }),
  adminToggleAdmin: (id) => request(`/admin/users/${id}/toggle-admin`, { method: "PUT" }),

  exportWithToken: async () => {
    const token = getToken();
    const res = await fetch(`${BASE}/stats/export`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Xuất thất bại");
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `caloviet_${new Date().toISOString().split("T")[0]}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  },
};

export function setToken(t) { localStorage.setItem("caloviet_token", t); }
export function clearToken() { localStorage.removeItem("caloviet_token"); }
export function hasToken() { return !!getToken(); }
export { getToken };
