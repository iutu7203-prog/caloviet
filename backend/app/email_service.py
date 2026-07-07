"""
Email service dùng Gmail SMTP.
Nếu biến môi trường SMTP_EMAIL không được cấu hình,
hàm sẽ skip gửi mail và trả về code để hiển thị trực tiếp (dev mode).
"""
import os
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
APP_NAME = os.getenv("APP_NAME", "CaloViet")
APP_URL = os.getenv("APP_URL", "http://localhost:5173")


def is_email_configured() -> bool:
    return bool(SMTP_EMAIL and SMTP_PASSWORD)


def _send_sync(to_email: str, subject: str, html_body: str):
    """Gửi mail đồng bộ — chạy trong thread riêng."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{APP_NAME} <{SMTP_EMAIL}>"
    msg["To"] = to_email
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, to_email, msg.as_string())


def send_email_async(to_email: str, subject: str, html_body: str):
    """Gửi mail trong background thread để không block API response."""
    t = threading.Thread(target=_send_sync, args=(to_email, subject, html_body), daemon=True)
    t.start()


def build_reset_email(name: str, code: str) -> str:
    """HTML template email đặt lại mật khẩu."""
    display_name = name or "bạn"
    return f"""
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
</head>
<body style="margin:0;padding:0;background:#f0fdf4;font-family:'Segoe UI',Arial,sans-serif;">
  <div style="max-width:480px;margin:32px auto;background:white;border-radius:20px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">

    <!-- Header -->
    <div style="background:linear-gradient(135deg,#15803d,#22c55e);padding:32px 24px;text-align:center;">
      <div style="font-size:40px;margin-bottom:8px;">🥗</div>
      <div style="color:white;font-size:24px;font-weight:800;letter-spacing:-0.5px;">{APP_NAME}</div>
      <div style="color:rgba(255,255,255,0.8);font-size:13px;margin-top:4px;">Theo dõi dinh dưỡng thông minh</div>
    </div>

    <!-- Body -->
    <div style="padding:32px 28px;">
      <h2 style="font-size:20px;font-weight:700;color:#14532d;margin:0 0 12px;">Đặt lại mật khẩu</h2>
      <p style="color:#4b5563;font-size:14px;line-height:1.6;margin:0 0 24px;">
        Xin chào <strong>{display_name}</strong>,<br/>
        Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản của bạn.
        Sử dụng mã xác nhận bên dưới để tiếp tục:
      </p>

      <!-- OTP Box -->
      <div style="background:#f0fdf4;border:2px dashed #86efac;border-radius:16px;padding:24px;text-align:center;margin:0 0 24px;">
        <div style="color:#6b7280;font-size:12px;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;">MÃ XÁC NHẬN</div>
        <div style="font-size:42px;font-weight:800;color:#16a34a;letter-spacing:10px;font-family:'Courier New',monospace;">{code}</div>
        <div style="color:#9ca3af;font-size:12px;margin-top:8px;">⏱️ Hết hạn sau <strong>15 phút</strong></div>
      </div>

      <p style="color:#4b5563;font-size:14px;line-height:1.6;margin:0 0 24px;">
        Nhập mã này vào ứng dụng để đặt lại mật khẩu của bạn.
      </p>

      <!-- Security note -->
      <div style="background:#fef9c3;border-left:4px solid #fde047;border-radius:8px;padding:12px 16px;font-size:12px;color:#713f12;">
        ⚠️ <strong>Lưu ý bảo mật:</strong> Không chia sẻ mã này với bất kỳ ai.
        Nếu bạn không yêu cầu đặt lại mật khẩu, hãy bỏ qua email này.
      </div>
    </div>

    <!-- Footer -->
    <div style="background:#f9fafb;border-top:1px solid #e5e7eb;padding:16px 24px;text-align:center;">
      <div style="color:#9ca3af;font-size:11px;">
        © {APP_NAME} · Email tự động, vui lòng không reply<br/>
        <a href="{APP_URL}" style="color:#16a34a;text-decoration:none;">{APP_URL}</a>
      </div>
    </div>
  </div>
</body>
</html>
"""


def build_welcome_email(name: str, email: str) -> str:
    """HTML template email chào mừng đăng ký."""
    display_name = name or "bạn"
    return f"""
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="UTF-8"/></head>
<body style="margin:0;padding:0;background:#f0fdf4;font-family:'Segoe UI',Arial,sans-serif;">
  <div style="max-width:480px;margin:32px auto;background:white;border-radius:20px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
    <div style="background:linear-gradient(135deg,#15803d,#22c55e);padding:32px 24px;text-align:center;">
      <div style="font-size:40px;margin-bottom:8px;">🎉</div>
      <div style="color:white;font-size:24px;font-weight:800;">{APP_NAME}</div>
    </div>
    <div style="padding:32px 28px;">
      <h2 style="font-size:20px;font-weight:700;color:#14532d;margin:0 0 12px;">Chào mừng {display_name}!</h2>
      <p style="color:#4b5563;font-size:14px;line-height:1.6;">
        Tài khoản <strong>{email}</strong> đã được tạo thành công.
        Bắt đầu hành trình dinh dưỡng thông minh của bạn ngay hôm nay!
      </p>
      <div style="margin:24px 0;display:flex;gap:12px;flex-wrap:wrap;">
        {''.join(f'<div style="background:#f0fdf4;border-radius:10px;padding:12px 16px;font-size:13px;color:#166534;flex:1;min-width:120px;text-align:center;">{item}</div>' for item in ['🍜 1167+ món VN', '📊 Theo dõi calo', '💧 Nhắc uống nước', '🏃 Ghi vận động'])}
      </div>
      <a href="{APP_URL}" style="display:block;background:linear-gradient(90deg,#15803d,#22c55e);color:white;text-decoration:none;text-align:center;padding:14px;border-radius:12px;font-weight:700;font-size:15px;">
        Vào ứng dụng ngay →
      </a>
    </div>
    <div style="background:#f9fafb;border-top:1px solid #e5e7eb;padding:16px 24px;text-align:center;">
      <div style="color:#9ca3af;font-size:11px;">© {APP_NAME} · <a href="{APP_URL}" style="color:#16a34a;">{APP_URL}</a></div>
    </div>
  </div>
</body>
</html>
"""
