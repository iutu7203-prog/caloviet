import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

// Khởi tạo Capacitor plugins khi chạy native
async function initCapacitor() {
  try {
    const { StatusBar, Style } = await import("@capacitor/status-bar");
    await StatusBar.setStyle({ style: Style.Dark });
    await StatusBar.setBackgroundColor({ color: "#15803d" });
  } catch (_) {
    // Bỏ qua khi chạy web (không có Capacitor)
  }

  try {
    const { Keyboard } = await import("@capacitor/keyboard");
    Keyboard.setAccessoryBarVisible({ isVisible: false });
  } catch (_) {}
}

initCapacitor();

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
