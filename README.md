# 🌿 CaloViet — App theo dõi calo & dinh dưỡng (Full-stack)

Phiên bản full-stack của app tính calo, xây dựng dựa trên feedback người dùng Việt: thêm món ăn Việt, giao diện tiếng Việt, sửa UX, không quảng cáo, xuất file, theo dõi tập luyện.

## Kiến trúc

```
caloviet/
├── backend/          FastAPI + SQLAlchemy + JWT (PostgreSQL / SQLite)
│   └── app/
│       ├── main.py           khởi tạo app, CORS, seed món ăn
│       ├── database.py       kết nối DB (tự nhận DATABASE_URL của Railway)
│       ├── models.py         User, Food, DiaryEntry, WaterLog, ExerciseLog
│       ├── schemas.py        Pydantic request/response
│       ├── security.py       hash mật khẩu (bcrypt) + JWT + tính TDEE
│       ├── seed_foods.py     ~37 món ăn Việt mặc định
│       └── routers/          auth, foods, diary, stats
├── frontend/         React + Vite (giao diện mobile)
│   └── src/
│       ├── App.jsx           3 tab: Trang chủ / Thống kê / Cá nhân
│       ├── lib/api.js        gọi API + lưu JWT
│       ├── pages/AuthPage    đăng nhập / đăng ký
│       └── components/       modal tìm món, thêm tập, biểu đồ
├── docker-compose.yml
└── README.md
```

## Tính năng (đã cải tiến theo feedback)

| Feedback người dùng | Đã xử lý |
|---|---|
| Thiếu món ăn, ít món miền Nam | 37 món Việt + **tự tạo món mới** lưu vào DB |
| App toàn tiếng Anh | Giao diện 100% tiếng Việt |
| Khó tìm chỗ ghi món (nút +) | Nút "＋ Thêm món" rõ ràng từng bữa |
| Protein/số liệu sai | Tính theo công thức chuẩn (1.6g × cân nặng) |
| Xem quảng cáo mới được phân tích | **Không có quảng cáo** |
| Không xuất file tổng hợp | Xuất CSV mở bằng Excel (`/stats/export`) |
| Không lưu dữ liệu giữa các máy | **Tài khoản + DB** đồng bộ mọi thiết bị |
| Thiếu theo dõi tập luyện | 10 bài tập (có pickleball) |

## Chạy local

### Cách 1 — Docker (đơn giản nhất)
```bash
docker compose up --build
# Backend:  http://localhost:8000  (docs: /docs)
# DB Postgres tự chạy
```
Frontend chạy riêng:
```bash
cd frontend
cp .env.example .env        # VITE_API_URL=http://localhost:8000
npm install && npm run dev  # http://localhost:5173
```

### Cách 2 — Không Docker (dùng SQLite)
```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload   # DB mặc định SQLite (caloviet.db)

# Frontend (terminal khác)
cd frontend
cp .env.example .env
npm install && npm run dev
```

## Deploy lên Railway

### Backend
1. Tạo project mới trên Railway → **Add PostgreSQL** (Railway tự cấp `DATABASE_URL`).
2. **New Service → GitHub repo**, chọn thư mục `backend/`.
3. Thêm biến môi trường:
   - `SECRET_KEY` = chuỗi ngẫu nhiên mạnh (bắt buộc đổi!)
   - `CORS_ORIGINS` = domain frontend (vd `https://caloviet.up.railway.app`)
4. Railway tự đọc `Procfile` và chạy. Kiểm tra `/health` và `/docs`.

### Frontend
1. **New Service** → cùng repo, thư mục `frontend/`.
2. Biến môi trường: `VITE_API_URL` = domain backend Railway.
3. Railway đọc `nixpacks.toml` để build và serve static.

## API chính (xem đầy đủ tại `/docs`)

| Method | Endpoint | Mô tả |
|---|---|---|
| POST | `/auth/register` | Đăng ký, trả JWT |
| POST | `/auth/login` | Đăng nhập (form: username=email) |
| GET/PUT | `/auth/me` | Xem/sửa hồ sơ (tự tính lại calo) |
| GET/POST | `/foods` | Tìm món / tạo món mới |
| POST/DELETE | `/diary/entries` | Thêm/xóa món đã ăn |
| PUT | `/diary/water` | Cập nhật nước |
| POST/DELETE | `/diary/exercises` | Thêm/xóa bài tập |
| GET | `/diary/day` | Tổng hợp 1 ngày |
| GET | `/stats/week` | Thống kê 7 ngày |
| GET | `/stats/export` | Xuất CSV |

## Đưa lên App Store / Google Play

Frontend là web app. Để thành app native:
- **Capacitor** (khuyên dùng): `npm i @capacitor/core @capacitor/cli`, `npx cap init`, `npx cap add ios/android`, build `dist` rồi `npx cap sync`. Mở Xcode / Android Studio để submit.
- Hoặc viết lại UI bằng **React Native / Expo** (logic API trong `lib/api.js` tái sử dụng gần như nguyên vẹn).

## Bảo mật cần làm trước production
- Đổi `SECRET_KEY` thành chuỗi ngẫu nhiên dài.
- Đặt `CORS_ORIGINS` đúng domain (không để `*`).
- Dùng Alembic cho migration thay vì `create_all` khi schema thay đổi.
