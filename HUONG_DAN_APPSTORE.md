# 📱 Hướng dẫn đưa CaloViet lên App Store & Google Play

## Tổng quan

```
Code React (web)
    └── Capacitor bọc thành native
            ├── iOS App → Xcode → App Store (Apple)
            └── Android App → Android Studio → Google Play
```

---

## Yêu cầu

| Nền tảng | Cần | Chi phí |
|----------|-----|---------|
| iOS (App Store) | Mac + Xcode + Apple Developer Account | $99/năm |
| Android (Play) | Windows/Mac + Android Studio + Google Play Account | $25 một lần |

---

## BƯỚC 0 — Chuẩn bị backend online

App mobile cần backend chạy trên Internet (không dùng localhost).

Deploy backend lên Railway (xem `README.md`), sau đó:

```
frontend/.env
VITE_API_URL=https://ten-backend-cua-ban.railway.app
```

---

## BƯỚC 1 — Cài đặt môi trường

### Cài Node.js 18+
https://nodejs.org

### Cài Xcode (chỉ Mac, cho iOS)
App Store → tìm "Xcode" → Install (~10GB)
Sau đó: `xcode-select --install`

### Cài Android Studio (cho Android)
https://developer.android.com/studio
Sau khi cài: SDK Manager → cài Android 13+ (API 33+)

### Cài CocoaPods (chỉ Mac, cho iOS)
```bash
sudo gem install cocoapods
```

---

## BƯỚC 2 — Cài dependencies Capacitor

Trong thư mục `frontend/`:
```bash
npm install
```

---

## BƯỚC 3 — Build và khởi tạo Capacitor

```bash
cd frontend/

# Build web app
npm run build

# Khởi tạo Capacitor (chỉ lần đầu)
npx cap init CaloViet com.caloviet.app --web-dir dist

# Thêm nền tảng
npx cap add ios        # cho iOS
npx cap add android    # cho Android

# Sync code vào native projects
npx cap sync
```

---

## BƯỚC 4 — Tạo icon và splash screen

Đặt file icon 1024×1024px vào `assets/icon.png` và chạy:
```bash
npx @capacitor/assets generate --iconBackgroundColor '#15803d' --splashBackgroundColor '#15803d'
```

File SVG mẫu đã có tại `assets/icon.svg` — mở Figma hoặc Inkscape export ra PNG 1024×1024.

---

## BƯỚC 5A — Build iOS

```bash
# Mở Xcode
npx cap open ios
```

Trong Xcode:
1. Chọn target `App`
2. **Signing & Capabilities** → chọn Team (Apple Developer Account)
3. Đổi Bundle ID: `com.caloviet.app` (phải trùng với capacitor.config.json)
4. **Product → Archive** để tạo file upload
5. **Window → Organizer** → **Distribute App** → App Store Connect

### App Store Connect (appstoreconnect.apple.com)
1. Tạo app mới: `+ New App`
2. Điền thông tin: tên, mô tả, screenshots
3. Upload build từ Xcode
4. Submit for Review (~1-3 ngày)

---

## BƯỚC 5B — Build Android

```bash
# Mở Android Studio
npx cap open android
```

Trong Android Studio:
1. **Build → Generate Signed Bundle/APK**
2. Chọn **Android App Bundle (.aab)** (bắt buộc cho Play Store)
3. Tạo keystore mới (giữ file này cẩn thận, mất là mất app!)
4. Build → tải file `.aab`

### Google Play Console (play.google.com/console)
1. **Create app**
2. Điền thông tin: tên, mô tả, category = Health & Fitness
3. **Production → Create new release** → upload file `.aab`
4. Điền release notes → Submit (~3-7 ngày review)

---

## BƯỚC 6 — Cập nhật app sau này

Mỗi lần có code mới:
```bash
cd frontend/
npm run cap:ios      # build + sync + mở Xcode
# hoặc
npm run cap:android  # build + sync + mở Android Studio
```

Tăng version trong `package.json` trước khi submit bản mới.

---

## Thông tin app (điền khi submit)

```
Tên app:     CaloViet - Theo dõi Dinh dưỡng
Category:    Health & Fitness
Age Rating:  4+ / Everyone
Language:    Vietnamese (chính), English
Keywords:    calo, dinh dưỡng, ăn kiêng, giảm cân, theo dõi ăn uống

Mô tả ngắn:
Ứng dụng theo dõi calo và dinh dưỡng hàng ngày với 1167+ món ăn Việt Nam.

Mô tả đầy đủ:
CaloViet giúp bạn theo dõi chế độ ăn uống một cách thông minh với:
• 1167+ món ăn Việt Nam (phở, bún, cơm, bánh, lẩu...)
• Theo dõi calo, carbs, protein, fat mỗi ngày
• Đặt mục tiêu: giảm cân, tăng cân, duy trì
• Theo dõi lượng nước uống hàng ngày
• Ghi nhận hoạt động thể chất
• Thống kê tuần với biểu đồ trực quan
• Xuất dữ liệu ra Excel/CSV
• Giao diện tiếng Việt hoàn toàn
```

---

## Screenshots cần có

| Loại | Kích thước |
|------|-----------|
| iPhone 6.7" | 1290 × 2796 px |
| iPhone 6.5" | 1284 × 2778 px |
| Android phone | 1080 × 1920 px |

Chụp màn hình: Trang chủ, Thêm món, Thống kê, Hồ sơ, Đăng nhập

---

## Lưu ý quan trọng

⚠️ **Keystore Android**: Backup file `.jks` và mật khẩu cẩn thận.
Mất keystore = không thể cập nhật app trên Play Store.

⚠️ **Apple Developer**: Gia hạn $99/năm. Nếu hết hạn app bị gỡ.

✅ **Bundle ID**: Đặt một lần không đổi được.
Format: `com.ten_cong_ty.caloviet`

✅ **Backend**: Đảm bảo Railway backend chạy ổn định trước khi submit.
