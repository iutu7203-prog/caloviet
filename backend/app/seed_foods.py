"""Dữ liệu món ăn Việt mặc định (món hệ thống, owner_id=NULL)."""

# ───── BATCH 1 — 37 món gốc ─────
SYSTEM_FOODS_V1 = [
    # Món Việt
    ("Cơm tấm sườn bì chả",    650, 85,   28,   18,   "phần", "vietnam"),
    ("Bánh mì thịt nguội",     380, 52,   18,   10,   "ổ",    "vietnam"),
    ("Phở bò tái",             420, 58,   25,    8,   "tô",   "vietnam"),
    ("Bún bò Huế",             450, 60,   26,   10,   "tô",   "vietnam"),
    ("Hủ tiếu Nam Vang",       400, 55,   22,    9,   "tô",   "vietnam"),
    ("Cháo lòng",              280, 38,   15,    6,   "tô",   "vietnam"),
    ("Bánh cuốn",              320, 48,   14,    7,   "phần", "vietnam"),
    ("Gỏi cuốn tôm thịt",      120, 18,    8,    2,   "cuốn", "vietnam"),
    ("Chả giò chiên",          180, 14,    7,   11,   "cuốn", "vietnam"),
    ("Bún thịt nướng",         520, 70,   28,   12,   "tô",   "vietnam"),
    ("Cơm chiên dương châu",   580, 78,   22,   16,   "phần", "vietnam"),
    ("Mì xào hải sản",         490, 65,   24,   13,   "phần", "vietnam"),
    ("Bún riêu cua",           380, 52,   18,    8,   "tô",   "vietnam"),
    ("Canh chua cá lóc",       220, 12,   22,    8,   "tô",   "vietnam"),
    ("Thịt kho tàu",           320,  8,   28,   18,   "chén", "vietnam"),
    ("Bún chả Hà Nội",         480, 58,   26,   14,   "phần", "vietnam"),
    ("Xôi xéo",                380, 68,   12,    6,   "gói",  "vietnam"),
    ("Bánh bao thịt",          280, 38,   14,    8,   "cái",  "vietnam"),
    ("Bánh mì chay",           300, 50,   10,    6,   "ổ",    "vietnam"),
    ("Bánh bao chay",          240, 42,    8,    4,   "cái",  "vietnam"),
    # Đồ uống
    ("Cà phê sữa đá",          180, 28,    3,    5,   "ly",   "drink"),
    ("Nước mía",               120, 30,    0,    0,   "ly",   "drink"),
    ("Sinh tố bơ",             320, 22,    4,   22,   "ly",   "drink"),
    ("Trà sữa trân châu",      350, 58,    4,    8,   "ly",   "drink"),
    # Cơ bản
    ("Cơm trắng",              130, 28,  2.7,  0.3,   "chén", "basic"),
    ("Trứng gà luộc",           78,  0.6,  6,    5,   "quả",  "basic"),
    ("Ức gà luộc",             165,  0,   31,  3.6,   "100g", "basic"),
    ("Cá hồi nướng",           208,  0,   28,   10,   "100g", "basic"),
    ("Rau muống xào tỏi",       85,  8,    4,    4,   "đĩa",  "basic"),
    ("Đậu phụ chiên",          145,  4,   11,    9,   "bìa",  "basic"),
    ("Bơ (avocado)",           160,  8.5,  2, 14.7,   "100g", "basic"),
    ("Chuối tiêu",              89, 23,  1.1,  0.3,   "quả",  "basic"),
    # Thực phẩm chức năng
    ("Sữa chua Vinamilk",       90, 14,    4,    2,   "hộp",  "supplement"),
    ("Protein shake (whey)",   150,  8,   25,    2,   "ly",   "supplement"),
    ("Bánh gạo lứt",            35,  7,  0.7,  0.2,   "cái",  "supplement"),
    # Fast food
    ("Jollibee gà giòn",       350, 22,   24,   18,   "miếng","fastfood"),
    ("Jollibee Yum burger",    420, 38,   22,   18,   "cái",  "fastfood"),
]

# ───── BATCH 2 — 50 món mới bổ sung ─────
SYSTEM_FOODS_V2 = [
    # === Món nước / bún / phở ===
    ("Phở gà",                 380, 55,   26,    7,   "tô",   "vietnam"),
    ("Bún cá",                 360, 52,   24,    6,   "tô",   "vietnam"),
    ("Mì Quảng",               480, 66,   24,   12,   "tô",   "vietnam"),
    ("Cao lầu Hội An",         450, 62,   22,   12,   "tô",   "vietnam"),
    ("Bún mắm",                430, 58,   22,   10,   "tô",   "vietnam"),
    ("Cháo gà",                280, 40,   18,    4,   "tô",   "vietnam"),
    ("Súp cua",                220, 22,   14,    8,   "tô",   "vietnam"),
    ("Bún tôm thịt xào",       460, 60,   26,   12,   "tô",   "vietnam"),

    # === Cơm / xôi ===
    ("Cơm gà Hội An",          580, 75,   30,   14,   "phần", "vietnam"),
    ("Cơm sườn nướng",         620, 80,   30,   18,   "phần", "vietnam"),
    ("Cơm chiên trứng",        480, 72,   14,   16,   "phần", "vietnam"),
    ("Xôi gà",                 480, 72,   22,   10,   "phần", "vietnam"),
    ("Xôi đậu phộng",          400, 72,   12,    8,   "gói",  "vietnam"),

    # === Bánh / snack ===
    ("Bánh xèo tôm thịt",      450, 42,   20,   22,   "cái",  "vietnam"),
    ("Bánh khọt",              280, 32,   12,   12,   "phần", "vietnam"),
    ("Bánh căn",               320, 42,   14,   12,   "phần", "vietnam"),
    ("Bánh bèo",               280, 48,   10,    6,   "phần", "vietnam"),
    ("Bánh ướt cuộn nhân",     240, 40,   12,    4,   "phần", "vietnam"),
    ("Bánh giò",               290, 42,   12,    8,   "cái",  "vietnam"),
    ("Bánh mì ốp la",          420, 45,   18,   18,   "ổ",    "vietnam"),
    ("Bánh mì chả cá",         360, 48,   18,   10,   "ổ",    "vietnam"),
    ("Bánh tráng trộn",        280, 42,   10,    8,   "túi",  "vietnam"),
    ("Bánh ít trần",           200, 34,    6,    5,   "cái",  "vietnam"),
    ("Nem chua",               120,  5,   10,    6,   "cái",  "vietnam"),

    # === Đồ nướng / chiên ===
    ("Gà nướng muối ớt",       320,  5,   38,   16,   "phần", "vietnam"),
    ("Nem nướng Nha Trang",    320, 25,   22,   14,   "phần", "vietnam"),
    ("Thịt heo quay",          420,  5,   32,   28,   "100g", "vietnam"),
    ("Vịt quay",               340,  0,   28,   24,   "100g", "vietnam"),
    ("Bò lúc lắc",             380,  8,   35,   22,   "phần", "vietnam"),
    ("Gà kho gừng",            290,  5,   30,   16,   "chén", "vietnam"),

    # === Món kho / canh ===
    ("Cá kho tộ",              280, 10,   30,   12,   "chén", "vietnam"),
    ("Tôm rim mặn ngọt",       220, 15,   20,    8,   "đĩa",  "vietnam"),
    ("Canh khổ qua nhồi thịt", 180,  8,   18,    7,   "tô",   "vietnam"),
    ("Cà ri gà khoai tây",     420, 22,   28,   24,   "tô",   "vietnam"),
    ("Chả cá Lã Vọng",         350, 20,   30,   16,   "phần", "vietnam"),
    ("Đậu hũ sốt sả ớt",       190,  8,   13,   11,   "đĩa",  "vietnam"),
    ("Chả lụa / giò lụa",      185,  3,   16,   12,   "100g", "vietnam"),

    # === Hải sản ===
    ("Tôm sú luộc",            140,  1,   26,    3,   "100g", "vietnam"),
    ("Ốc len xào dừa",         280, 18,   18,   14,   "phần", "vietnam"),
    ("Mực chiên giòn",         310, 18,   22,   16,   "phần", "vietnam"),

    # === Bún đậu / lẩu ===
    ("Bún đậu mắm tôm",        550, 58,   24,   22,   "phần", "vietnam"),
    ("Lẩu thái hải sản",       520, 45,   38,   18,   "phần", "vietnam"),
    ("Lẩu bò",                 580, 42,   42,   22,   "phần", "vietnam"),

    # === Món khác / đặc sản ===
    ("Trứng vịt lộn",          182, 14,   13,    8,   "quả",  "vietnam"),
    ("Mì gói Hảo Hảo",         360, 52,   10,   12,   "gói",  "vietnam"),
    ("Khoai lang nướng",       130, 30,    2,  0.2,   "củ",   "basic"),
    ("Bắp xào bơ",             180, 32,    4,    5,   "bắp",  "vietnam"),

    # === Đồ uống / tráng miệng ===
    ("Sinh tố xoài",           220, 52,    3,    1,   "ly",   "drink"),
    ("Nước dừa tươi",           46, 11,  0.5,    0,   "trái", "drink"),
    ("Đá xay cacao",           280, 50,    5,    7,   "ly",   "drink"),
    ("Chè đậu xanh",           200, 38,    6,    3,   "chén", "vietnam"),
    ("Chè chuối nước cốt dừa", 220, 42,    3,    5,   "chén", "vietnam"),
    ("Bánh flan caramel",      180, 28,    6,    5,   "cái",  "vietnam"),
    ("Sữa chua nếp cẩm",       250, 40,    5,    7,   "hũ",   "vietnam"),
]

# ───── BATCH 3 — 100 món bổ sung ─────
SYSTEM_FOODS_V3 = [

    # ═══════════════════════════════════════════════
    # 1. MÓN NƯỚC — bún / phở / mì / cháo (18 món)
    # ═══════════════════════════════════════════════
    ("Phở bò chín",                430, 58, 28,  9, "tô",   "vietnam"),
    ("Phở bò viên",                400, 56, 24,  8, "tô",   "vietnam"),
    ("Phở cuốn",                   320, 45, 20,  6, "phần", "vietnam"),
    ("Bún suông",                  380, 52, 22,  8, "tô",   "vietnam"),
    ("Bún kèn",                    390, 52, 22, 10, "tô",   "vietnam"),
    ("Bún bò Nam Bộ",              480, 62, 26, 12, "tô",   "vietnam"),
    ("Bánh canh giò heo",          480, 62, 28, 14, "tô",   "vietnam"),
    ("Bánh canh cua",              450, 58, 26, 12, "tô",   "vietnam"),
    ("Bánh canh tôm",              420, 58, 24, 10, "tô",   "vietnam"),
    ("Miến gà",                    360, 58, 22,  6, "tô",   "vietnam"),
    ("Miến cua",                   340, 55, 18,  6, "tô",   "vietnam"),
    ("Cháo cá",                    260, 38, 18,  4, "tô",   "vietnam"),
    ("Cháo hải sản",               280, 40, 18,  5, "tô",   "vietnam"),
    ("Cháo tim cật",               300, 40, 20,  6, "tô",   "vietnam"),
    ("Hủ tiếu xào bò",             460, 62, 26, 12, "phần", "vietnam"),
    ("Mì hoành thánh",             420, 58, 22, 10, "tô",   "vietnam"),
    ("Bánh đa cua Hải Phòng",      420, 55, 22, 12, "tô",   "vietnam"),
    ("Bún bò xào",                 460, 58, 28, 14, "phần", "vietnam"),

    # ═══════════════════════════════════════════════
    # 2. CƠM ĐẶC SẢN (7 món)
    # ═══════════════════════════════════════════════
    ("Cơm hến",                    380, 60, 18,  8, "phần", "vietnam"),
    ("Cơm lam",                    200, 42,  6,  2, "ống",  "vietnam"),
    ("Cơm bì",                     500, 72, 22, 14, "phần", "vietnam"),
    ("Cơm gà xối mỡ",              650, 78, 35, 24, "phần", "vietnam"),
    ("Cơm âm phủ Huế",             580, 72, 28, 18, "phần", "vietnam"),
    ("Cơm cháy",                   220, 46,  5,  4, "miếng","vietnam"),
    ("Cơm nắm muối mè",            280, 56,  6,  4, "nắm",  "vietnam"),

    # ═══════════════════════════════════════════════
    # 3. XÔI ĐẶC SẢN (5 món)
    # ═══════════════════════════════════════════════
    ("Xôi bắp",                    320, 62,  8,  4, "gói",  "vietnam"),
    ("Xôi chiên phồng",            280, 42,  6, 10, "cái",  "vietnam"),
    ("Xôi xoài nước cốt dừa",      380, 68,  5, 10, "phần", "vietnam"),
    ("Xôi lạc vừng",               350, 60, 12,  8, "gói",  "vietnam"),
    ("Xôi mặn thập cẩm",           420, 65, 18, 10, "gói",  "vietnam"),

    # ═══════════════════════════════════════════════
    # 4. BÁNH ĐẶC SẢN (14 món)
    # ═══════════════════════════════════════════════
    ("Bánh tét miền Nam",          280, 52,  8,  5, "khúc", "vietnam"),
    ("Bánh chưng",                 320, 58, 12,  6, "miếng","vietnam"),
    ("Bánh phu thê (su sê)",       200, 38,  3,  4, "cái",  "vietnam"),
    ("Bánh ít nhân dừa",           180, 32,  3,  5, "cái",  "vietnam"),
    ("Bánh đúc mặn",               250, 42, 10,  5, "phần", "vietnam"),
    ("Bánh trôi nước",             150, 28,  3,  3, "cái",  "vietnam"),
    ("Bánh chuối chiên",           200, 32,  2,  8, "cái",  "vietnam"),
    ("Bánh tráng nướng",           260, 42,  8,  7, "cái",  "vietnam"),
    ("Bánh rán nhân đậu xanh",     220, 35,  5,  7, "cái",  "vietnam"),
    ("Bánh khoái Huế",             380, 38, 18, 18, "phần", "vietnam"),
    ("Bánh mì pate",               400, 50, 18, 14, "ổ",    "vietnam"),
    ("Bánh mì xíu mại",            420, 52, 20, 14, "ổ",    "vietnam"),
    ("Bánh khúc",                  300, 52, 10,  6, "cái",  "vietnam"),
    ("Bánh đậu xanh Hải Dương",    120, 22,  3,  3, "cái",  "vietnam"),

    # ═══════════════════════════════════════════════
    # 5. CUỐN / NEM (5 món)
    # ═══════════════════════════════════════════════
    ("Gỏi cuốn chay",               90, 16,  4,  1, "cuốn", "vietnam"),
    ("Bò bía",                     130, 18,  6,  4, "cuốn", "vietnam"),
    ("Bánh tráng cuộn thịt heo",   320, 38, 18, 10, "phần", "vietnam"),
    ("Phô mai que chiên",          160, 12,  6, 10, "cái",  "vietnam"),
    ("Cuốn diếp bò tươi",          140, 10, 12,  5, "cuốn", "vietnam"),

    # ═══════════════════════════════════════════════
    # 6. THỊT / GIA CẦM (10 món)
    # ═══════════════════════════════════════════════
    ("Sườn xào chua ngọt",         380, 22, 28, 18, "phần", "vietnam"),
    ("Thịt bò xào rau muống",      280, 10, 26, 14, "đĩa",  "vietnam"),
    ("Gà rang muối",               320,  4, 36, 18, "phần", "vietnam"),
    ("Gà chiên mắm",               350, 10, 34, 20, "phần", "vietnam"),
    ("Heo kho nước dừa",           380, 12, 28, 22, "chén", "vietnam"),
    ("Vịt nấu chao",               380,  8, 30, 24, "tô",   "vietnam"),
    ("Thịt gà luộc",               185,  0, 28,  8, "100g", "basic"),
    ("Sườn heo nướng",             350,  8, 28, 22, "phần", "vietnam"),
    ("Lòng heo xào dứa",           250, 14, 20, 12, "đĩa",  "vietnam"),
    ("Chân giò hầm",               420, 10, 38, 26, "tô",   "vietnam"),

    # ═══════════════════════════════════════════════
    # 7. HẢI SẢN (10 món)
    # ═══════════════════════════════════════════════
    ("Cá lóc nướng trui",          280,  0, 32, 14, "phần", "vietnam"),
    ("Cá chiên sả ớt",             320,  8, 28, 18, "phần", "vietnam"),
    ("Tôm chiên bột giòn",         280, 18, 18, 14, "phần", "vietnam"),
    ("Cua rang muối",              240,  6, 24, 12, "phần", "vietnam"),
    ("Bạch tuộc nướng sa tế",      220,  6, 28,  8, "phần", "vietnam"),
    ("Sò huyết xào",               180,  8, 18,  8, "phần", "vietnam"),
    ("Nghêu hấp sả",               160,  6, 20,  5, "đĩa",  "vietnam"),
    ("Cá basa chiên",              250,  8, 24, 14, "phần", "vietnam"),
    ("Mực nướng sa tế",            260,  8, 28, 12, "phần", "vietnam"),
    ("Tôm rang muối",              220,  4, 26, 10, "phần", "vietnam"),

    # ═══════════════════════════════════════════════
    # 8. CANH / SÚP (8 món)
    # ═══════════════════════════════════════════════
    ("Canh bầu tôm khô",           120,  8, 10,  4, "tô",   "vietnam"),
    ("Canh mướp xào trứng",        140,  8,  8,  6, "tô",   "vietnam"),
    ("Canh rau ngót",               80,  6,  6,  2, "tô",   "vietnam"),
    ("Canh bí đỏ thịt heo",        160, 15, 10,  5, "tô",   "vietnam"),
    ("Canh ngao",                  140,  5, 16,  4, "tô",   "vietnam"),
    ("Canh chua tôm",              200, 10, 18,  7, "tô",   "vietnam"),
    ("Canh cải thịt băm",          140,  8, 12,  5, "tô",   "vietnam"),
    ("Canh riêu cua đồng",         180, 10, 16,  6, "tô",   "vietnam"),

    # ═══════════════════════════════════════════════
    # 9. GỎI / RAU (6 món)
    # ═══════════════════════════════════════════════
    ("Gỏi gà rau húng",            280, 12, 24, 12, "đĩa",  "vietnam"),
    ("Gỏi bắp chuối tôm",         220, 18, 16,  8, "đĩa",  "vietnam"),
    ("Gỏi ngó sen",                200, 20, 12,  7, "đĩa",  "vietnam"),
    ("Gỏi đu đủ thịt khô",         180, 20, 10,  6, "đĩa",  "vietnam"),
    ("Gỏi bò bóp thấu",            260, 10, 26, 12, "đĩa",  "vietnam"),
    ("Đậu cô ve xào tỏi",           80, 10,  4,  3, "đĩa",  "basic"),

    # ═══════════════════════════════════════════════
    # 10. ĂN VẶT / STREET FOOD (5 món)
    # ═══════════════════════════════════════════════
    ("Khoai mì chiên",             200, 38,  2,  6, "phần", "vietnam"),
    ("Hột vịt nướng",              120,  8,  8,  6, "quả",  "vietnam"),
    ("Ốc nhồi thịt nướng",         180,  8, 14, 10, "phần", "vietnam"),
    ("Đậu phộng rang muối",        580, 18, 26, 50, "100g", "basic"),
    ("Bắp nướng bơ",               170, 30,  4,  5, "bắp",  "vietnam"),

    # ═══════════════════════════════════════════════
    # 11. TRÁNG MIỆNG / CHÈ (8 món)
    # ═══════════════════════════════════════════════
    ("Chè thập cẩm",               250, 48,  5,  5, "chén", "vietnam"),
    ("Chè bưởi",                   210, 42,  2,  4, "chén", "vietnam"),
    ("Chè trôi nước",              240, 44,  4,  5, "chén", "vietnam"),
    ("Chè khoai lang",             200, 40,  3,  4, "chén", "vietnam"),
    ("Kem que chuối",              130, 22,  2,  4, "cái",  "vietnam"),
    ("Thạch rau câu dừa",           80, 18,  0,  1, "hũ",   "vietnam"),
    ("Bánh bột lọc Huế",           160, 28,  6,  3, "phần", "vietnam"),
    ("Dừa dầm",                    220, 38,  2,  7, "ly",   "vietnam"),

    # ═══════════════════════════════════════════════
    # 12. ĐỒ UỐNG (4 món)
    # ═══════════════════════════════════════════════
    ("Cà phê đen đá",               10,  1,  0,  0, "ly",   "drink"),
    ("Cà phê trứng",               220, 20,  6, 12, "ly",   "drink"),
    ("Nước ép cam tươi",           110, 26,  2,  0, "ly",   "drink"),
    ("Trà đào cam sả",             160, 40,  0,  0, "ly",   "drink"),
]

ALL_SYSTEM_FOODS = SYSTEM_FOODS_V1 + SYSTEM_FOODS_V2 + SYSTEM_FOODS_V3


def seed_foods(db, models):
    """
    Upsert tất cả món hệ thống theo tên.
    An toàn khi chạy nhiều lần hoặc khi DB đã có dữ liệu v1.
    """
    import app.seed_foods as _sf
    foods = (_sf.SYSTEM_FOODS_V1 + _sf.SYSTEM_FOODS_V2 +
             _sf.SYSTEM_FOODS_V3 + _sf.SYSTEM_FOODS_V4 +
             _sf.SYSTEM_FOODS_V5)
    existing_names = {
        row[0] for row in
        db.query(models.Food.name).filter(models.Food.owner_id.is_(None)).all()
    }
    added = 0
    for name, cal, c, p, f, unit, cat in foods:
        if name not in existing_names:
            db.add(models.Food(
                name=name, cal=cal, carbs=c, protein=p, fat=f,
                unit=unit, category=cat, owner_id=None,
            ))
            added += 1
    if added:
        db.commit()
        print(f"[seed] Thêm {added} món mới vào thư viện")

# ───── BATCH 4 — 500 món bổ sung ─────
SYSTEM_FOODS_V4 = [

    # ══════════════════════════════════════════
    # 1. PHỞ BIẾN TẤU (12 món)
    # ══════════════════════════════════════════
    ("Phở bò nạm gầu",              450, 58, 30, 10, "tô",   "vietnam"),
    ("Phở vịt",                     400, 56, 26,  8, "tô",   "vietnam"),
    ("Phở chay",                    320, 55, 10,  5, "tô",   "vietnam"),
    ("Phở bò sốt vang",             480, 58, 32, 14, "tô",   "vietnam"),
    ("Phở xào bò",                  480, 62, 30, 12, "phần", "vietnam"),
    ("Phở khô Gia Lai",             420, 60, 28,  8, "phần", "vietnam"),
    ("Phở gà sả",                   390, 55, 28,  6, "tô",   "vietnam"),
    ("Phở hải sản",                 420, 58, 28,  8, "tô",   "vietnam"),
    ("Phở bò kho",                  480, 55, 32, 16, "tô",   "vietnam"),
    ("Bún thang Hà Nội",            380, 52, 22,  8, "tô",   "vietnam"),
    ("Bún ốc Hà Nội",               360, 50, 18,  8, "tô",   "vietnam"),
    ("Phở trộn khô",                410, 60, 26,  8, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 2. BÚN BIẾN TẤU (15 món)
    # ══════════════════════════════════════════
    ("Bún rươi Hà Nội",             400, 55, 22, 10, "tô",   "vietnam"),
    ("Bún bò lá lốt",               460, 60, 26, 12, "tô",   "vietnam"),
    ("Bún cá ngừ",                  370, 52, 24,  7, "tô",   "vietnam"),
    ("Bún sứa",                     320, 48, 20,  5, "tô",   "vietnam"),
    ("Bún mộc",                     380, 52, 22,  8, "tô",   "vietnam"),
    ("Bún nước lèo Sóc Trăng",      420, 55, 22, 10, "tô",   "vietnam"),
    ("Bún cá lóc",                  360, 52, 22,  6, "tô",   "vietnam"),
    ("Bún tôm",                     380, 52, 22,  8, "tô",   "vietnam"),
    ("Bún chả mực",                 440, 58, 24, 12, "phần", "vietnam"),
    ("Bún hải sản",                 400, 55, 24,  8, "tô",   "vietnam"),
    ("Bún bò thơm",                 420, 58, 24, 10, "tô",   "vietnam"),
    ("Bún khô thịt nướng",          480, 65, 28, 12, "phần", "vietnam"),
    ("Bún giò chả",                 440, 60, 26, 10, "tô",   "vietnam"),
    ("Bún Quảng Nam",               400, 55, 22, 10, "tô",   "vietnam"),
    ("Bún chay",                    300, 52, 10,  5, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 3. HỦ TIẾU / MÌ / MIẾN (18 món)
    # ══════════════════════════════════════════
    ("Hủ tiếu chay",                340, 55, 10,  6, "tô",   "vietnam"),
    ("Hủ tiếu bò kho",              460, 58, 28, 14, "tô",   "vietnam"),
    ("Mì vịt tiềm",                 480, 62, 28, 14, "tô",   "vietnam"),
    ("Mì xào bò",                   490, 62, 28, 14, "phần", "vietnam"),
    ("Mì xào gà",                   460, 60, 26, 12, "phần", "vietnam"),
    ("Mì xào chay",                 380, 58, 12, 10, "phần", "vietnam"),
    ("Mì khô trộn",                 400, 58, 20, 10, "phần", "vietnam"),
    ("Mì gõ sốt nước",              380, 55, 18,  8, "tô",   "vietnam"),
    ("Miến xào cua",                380, 58, 18,  8, "phần", "vietnam"),
    ("Miến chay",                   310, 55,  8,  5, "tô",   "vietnam"),
    ("Mì trứng xào thịt",           460, 58, 24, 14, "phần", "vietnam"),
    ("Bánh đa trộn tôm thịt",       380, 52, 20, 10, "phần", "vietnam"),
    ("Bánh phở xào thịt",           460, 62, 26, 12, "phần", "vietnam"),
    ("Miến trộn gà",                380, 56, 22,  8, "phần", "vietnam"),
    ("Mì xào giòn hải sản",         520, 65, 26, 18, "phần", "vietnam"),
    ("Bún xào bò",                  460, 60, 26, 12, "phần", "vietnam"),
    ("Hủ tiếu dai xào",             450, 60, 24, 12, "phần", "vietnam"),
    ("Mì căng bò viên",             440, 58, 24, 14, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 4. CHÁO (12 món)
    # ══════════════════════════════════════════
    ("Cháo vịt",                    290, 40, 20,  6, "tô",   "vietnam"),
    ("Cháo bò",                     300, 40, 20,  7, "tô",   "vietnam"),
    ("Cháo đậu xanh",               220, 40,  8,  3, "tô",   "vietnam"),
    ("Cháo trắng",                  130, 28,  3,  1, "tô",   "vietnam"),
    ("Cháo nấm",                    200, 35,  8,  3, "tô",   "vietnam"),
    ("Cháo cá lóc",                 270, 38, 20,  4, "tô",   "vietnam"),
    ("Cháo sườn",                   280, 40, 18,  6, "tô",   "vietnam"),
    ("Cháo tôm",                    260, 38, 18,  4, "tô",   "vietnam"),
    ("Cháo thịt bằm",               280, 40, 18,  6, "tô",   "vietnam"),
    ("Cháo bào ngư biển",           350, 42, 24,  8, "tô",   "vietnam"),
    ("Cháo ngao",                   240, 38, 16,  4, "tô",   "vietnam"),
    ("Cháo dinh dưỡng",             220, 38, 10,  3, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 5. BÁNH CANH ĐẶC TRƯNG (5 món)
    # ══════════════════════════════════════════
    ("Bánh canh chả cá",            460, 58, 26, 12, "tô",   "vietnam"),
    ("Bánh canh thịt bằm",          440, 60, 24, 12, "tô",   "vietnam"),
    ("Bánh canh cá lóc",            430, 58, 24, 10, "tô",   "vietnam"),
    ("Bánh canh Trảng Bàng",        420, 58, 22, 10, "tô",   "vietnam"),
    ("Bánh canh Nam Phổ",           380, 55, 20,  8, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 6. CƠM ĐA DẠNG (35 món)
    # ══════════════════════════════════════════
    ("Cơm tấm sườn đơn",            520, 75, 25, 14, "phần", "vietnam"),
    ("Cơm tấm bì",                  560, 80, 24, 16, "phần", "vietnam"),
    ("Cơm bò băm",                  520, 72, 28, 14, "phần", "vietnam"),
    ("Cơm gà quay",                 580, 75, 32, 18, "phần", "vietnam"),
    ("Cơm thịt kho tiêu",           500, 72, 24, 14, "phần", "vietnam"),
    ("Cơm tôm chiên",               520, 72, 26, 14, "phần", "vietnam"),
    ("Cơm cá thu kho",              500, 70, 26, 14, "phần", "vietnam"),
    ("Cơm sườn trứng",              560, 76, 28, 16, "phần", "vietnam"),
    ("Cơm chiên kim chi",           540, 75, 22, 18, "phần", "vietnam"),
    ("Cơm chiên cá mặn",            520, 74, 22, 16, "phần", "vietnam"),
    ("Cơm rang bơ tỏi",             480, 72, 12, 16, "phần", "vietnam"),
    ("Cơm bò xào rau",              520, 70, 28, 16, "phần", "vietnam"),
    ("Cơm gà nướng sả",             560, 74, 32, 18, "phần", "vietnam"),
    ("Cơm tôm sốt cà chua",         510, 72, 24, 14, "phần", "vietnam"),
    ("Cơm đậu phụ sốt cà",          420, 68, 16, 10, "phần", "vietnam"),
    ("Cơm cá chiên sả",             500, 70, 26, 14, "phần", "vietnam"),
    ("Cơm vịt quay",                580, 72, 32, 22, "phần", "vietnam"),
    ("Cơm bibimbap Hàn Quốc",       520, 72, 22, 16, "phần", "vietnam"),
    ("Cơm cuộn rong biển",          380, 62, 14,  8, "cuộn", "vietnam"),
    ("Cơm gạo lứt nâu",             120, 25,  3,  1, "chén", "basic"),
    ("Cơm rang thập cẩm",           560, 75, 22, 18, "phần", "vietnam"),
    ("Cơm gà xé phay",              540, 74, 30, 16, "phần", "vietnam"),
    ("Cơm cá kèo kho",              480, 68, 24, 14, "phần", "vietnam"),
    ("Cơm thịt viên sốt",           500, 70, 24, 14, "phần", "vietnam"),
    ("Cơm sốt bò hành tây",         540, 72, 28, 18, "phần", "vietnam"),
    ("Cơm nướng ống tre",           320, 58,  8,  6, "ống",  "vietnam"),
    ("Cơm thịt xào cải",            480, 68, 24, 14, "phần", "vietnam"),
    ("Cơm tôm rang muối",           520, 70, 26, 16, "phần", "vietnam"),
    ("Cơm gà tiềm",                 520, 72, 28, 14, "phần", "vietnam"),
    ("Cơm xào bơ tỏi",              480, 70, 10, 18, "phần", "vietnam"),
    ("Cơm sườn Đài Loan",           540, 74, 28, 16, "phần", "vietnam"),
    ("Cơm chay nấm rơm",            380, 68, 12,  8, "phần", "vietnam"),
    ("Cơm chiên tôm trứng",         540, 72, 26, 18, "phần", "vietnam"),
    ("Cơm cá hộp sốt cà",           400, 62, 22, 10, "phần", "vietnam"),
    ("Cơm cháy chà bông",           320, 50, 12,  8, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 7. XÔI ĐA DẠNG (10 món)
    # ══════════════════════════════════════════
    ("Xôi trứng muối",              420, 68, 14, 10, "phần", "vietnam"),
    ("Xôi thịt",                    450, 68, 20, 12, "phần", "vietnam"),
    ("Xôi dừa",                     380, 65,  6, 14, "gói",  "vietnam"),
    ("Xôi đậu đen",                 360, 65, 12,  6, "gói",  "vietnam"),
    ("Xôi lá cẩm",                  360, 65,  8,  8, "phần", "vietnam"),
    ("Xôi mít",                     350, 65,  6,  8, "phần", "vietnam"),
    ("Xôi gấc",                     380, 68,  8,  8, "phần", "vietnam"),
    ("Xôi lạp xưởng",               450, 66, 18, 14, "phần", "vietnam"),
    ("Xôi sầu riêng",               400, 65,  6, 14, "phần", "vietnam"),
    ("Xôi ngọt nước cốt dừa",       380, 68,  5, 10, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 8. BÁNH ĐA DẠNG (40 món)
    # ══════════════════════════════════════════
    ("Bánh mì kẹp trứng",           380, 45, 16, 16, "ổ",    "vietnam"),
    ("Bánh mì bơ tỏi",              280, 40,  8, 12, "ổ",    "vietnam"),
    ("Bánh cuốn chay",              260, 45,  8,  5, "phần", "vietnam"),
    ("Bánh cuốn trứng",             300, 45, 14,  7, "phần", "vietnam"),
    ("Bánh xèo chay",               350, 40, 10, 16, "cái",  "vietnam"),
    ("Bánh tiêu",                   220, 35,  5,  8, "cái",  "vietnam"),
    ("Bánh cóng",                   250, 28, 12, 12, "cái",  "vietnam"),
    ("Bánh bông lan",               220, 32,  5,  8, "miếng","vietnam"),
    ("Bánh kẹp lá dứa",             180, 28,  4,  6, "cái",  "vietnam"),
    ("Bánh mì que",                 180, 32,  6,  4, "cái",  "vietnam"),
    ("Bánh bía Sóc Trăng",          280, 42,  6, 10, "cái",  "vietnam"),
    ("Bánh tráng phơi sương",       320, 52,  8,  8, "phần", "vietnam"),
    ("Bánh da lợn",                 180, 32,  4,  4, "miếng","vietnam"),
    ("Bánh hỏi thịt nướng",         480, 62, 24, 14, "phần", "vietnam"),
    ("Bánh hỏi chay",               320, 58, 10,  5, "phần", "vietnam"),
    ("Bánh mì nướng muối ớt",       320, 45, 10, 12, "ổ",    "vietnam"),
    ("Bánh gai",                    250, 45,  5,  6, "cái",  "vietnam"),
    ("Bánh ít lá gai",              200, 38,  4,  4, "cái",  "vietnam"),
    ("Bánh ram ít",                 200, 36,  6,  5, "phần", "vietnam"),
    ("Bánh cay miền Trung",         220, 35,  6,  8, "cái",  "vietnam"),
    ("Bánh khoai mì",               250, 45,  4,  6, "phần", "vietnam"),
    ("Bánh nếp nhân đậu",           220, 38,  6,  4, "cái",  "vietnam"),
    ("Bánh tai yến",                150, 28,  4,  3, "cái",  "vietnam"),
    ("Bánh lọc tôm thịt",           160, 28,  6,  3, "phần", "vietnam"),
    ("Bánh mướt",                   240, 42, 10,  4, "phần", "vietnam"),
    ("Bánh đúc ngọt",               220, 40,  4,  5, "phần", "vietnam"),
    ("Bánh tổ",                     280, 50,  5,  6, "miếng","vietnam"),
    ("Bánh thuẫn",                  180, 30,  5,  5, "cái",  "vietnam"),
    ("Bánh in Bình Định",           120, 22,  3,  3, "cái",  "vietnam"),
    ("Bánh căn mực",                340, 42, 18, 12, "phần", "vietnam"),
    ("Bánh cuốn tôm chấy",          280, 42, 14,  6, "phần", "vietnam"),
    ("Bánh ướt tôm chấy",           260, 40, 12,  5, "phần", "vietnam"),
    ("Bánh mì lạnh cốt",            280, 40, 10, 10, "ổ",    "vietnam"),
    ("Bánh chuối hấp",              180, 32,  2,  5, "phần", "vietnam"),
    ("Bánh nếp chiên",              240, 38,  6,  8, "cái",  "vietnam"),
    ("Bánh sắn nhân dừa",           220, 42,  3,  5, "phần", "vietnam"),
    ("Bánh mì sandwich trứng cà",   350, 42, 14, 14, "cái",  "vietnam"),
    ("Bánh croissant bơ",           280, 32,  6, 14, "cái",  "vietnam"),
    ("Bánh tráng nướng mực",        280, 44, 12,  8, "cái",  "vietnam"),
    ("Bánh phồng sữa",              160, 28,  3,  5, "cái",  "vietnam"),

    # ══════════════════════════════════════════
    # 9. CUỐN / NEM MỚI (5 món)
    # ══════════════════════════════════════════
    ("Tôm cuốn bánh tráng",         140, 18, 12,  3, "cuốn", "vietnam"),
    ("Cuốn hải sản tươi",           150, 18, 12,  4, "cuốn", "vietnam"),
    ("Nem rán Hà Nội",              200, 16, 10, 10, "cuốn", "vietnam"),
    ("Chả giò tôm",                 200, 14, 10, 12, "cuốn", "vietnam"),
    ("Bì cuốn rau sống",            180, 14, 12,  8, "cuốn", "vietnam"),

    # ══════════════════════════════════════════
    # 10. THỊT HEO (25 món)
    # ══════════════════════════════════════════
    ("Thịt heo rang tỏi",           320,  6, 28, 20, "đĩa",  "vietnam"),
    ("Thịt heo xào cải chua",       280,  8, 24, 16, "đĩa",  "vietnam"),
    ("Heo xào sả ớt",               300,  6, 26, 18, "đĩa",  "vietnam"),
    ("Thịt ba chỉ luộc",            350,  2, 24, 26, "đĩa",  "vietnam"),
    ("Thịt ba chỉ chiên giòn",      450,  8, 26, 34, "đĩa",  "vietnam"),
    ("Thịt nướng lá lốt",           380, 12, 28, 24, "phần", "vietnam"),
    ("Bì lợn trộn",                 280,  8, 22, 18, "phần", "vietnam"),
    ("Chân giò giả cầy",            450,  8, 34, 30, "tô",   "vietnam"),
    ("Giò thủ đông",                220,  4, 18, 14, "100g", "vietnam"),
    ("Lạp xưởng heo",               350,  8, 18, 28, "100g", "vietnam"),
    ("Dồi heo",                     280, 10, 18, 18, "khúc", "vietnam"),
    ("Thịt heo xào rau củ",         280, 12, 22, 14, "đĩa",  "vietnam"),
    ("Sườn heo rim mặn",            380, 12, 28, 22, "đĩa",  "vietnam"),
    ("Tóp mỡ giòn",                 520,  2, 18, 48, "100g", "vietnam"),
    ("Bao tử heo xào gừng",         220,  6, 20, 12, "đĩa",  "vietnam"),
    ("Gan heo xào hành",            240,  8, 24, 12, "đĩa",  "vietnam"),
    ("Thịt viên heo sốt cà",        300, 14, 22, 16, "đĩa",  "vietnam"),
    ("Thịt kho dưa",                320, 10, 24, 20, "chén", "vietnam"),
    ("Thịt heo xào hành lá",        280,  6, 24, 16, "đĩa",  "vietnam"),
    ("Heo xào gừng",                280,  6, 24, 16, "đĩa",  "vietnam"),
    ("Mọi heo nướng than",          380, 10, 30, 24, "phần", "vietnam"),
    ("Heo kho tiêu",                360,  8, 28, 22, "chén", "vietnam"),
    ("Thịt ba chỉ rang mắm",        400,  6, 26, 30, "đĩa",  "vietnam"),
    ("Sườn xốt BBQ",                420, 18, 28, 24, "phần", "vietnam"),
    ("Chả heo chiên",               280,  8, 20, 18, "đĩa",  "vietnam"),

    # ══════════════════════════════════════════
    # 11. THỊT BÒ (20 món)
    # ══════════════════════════════════════════
    ("Bò nướng lá lốt",             360, 10, 32, 20, "phần", "vietnam"),
    ("Bò xào hành tây",             320, 10, 28, 18, "đĩa",  "vietnam"),
    ("Bò xào ớt chuông",            310, 10, 28, 16, "đĩa",  "vietnam"),
    ("Bò sốt tiêu đen",             360,  8, 30, 22, "phần", "vietnam"),
    ("Bò nướng xiên que",           340,  8, 30, 20, "phần", "vietnam"),
    ("Phá lấu bò",                  320, 14, 24, 18, "phần", "vietnam"),
    ("Bò kho",                      380, 12, 32, 20, "tô",   "vietnam"),
    ("Bò sốt vang",                 420, 14, 32, 24, "phần", "vietnam"),
    ("Bò gỏi trộn",                 260, 10, 26, 12, "đĩa",  "vietnam"),
    ("Bò khô",                      250,  8, 32, 10, "100g", "vietnam"),
    ("Tái bò chanh sả",             280,  6, 30, 14, "đĩa",  "vietnam"),
    ("Bò viên chiên",               300, 10, 24, 18, "đĩa",  "vietnam"),
    ("Gân bò hầm",                  320,  6, 28, 20, "tô",   "vietnam"),
    ("Lòng bò xào",                 220,  6, 22, 12, "đĩa",  "vietnam"),
    ("Dạ dày bò xào gừng",          200,  6, 20, 10, "đĩa",  "vietnam"),
    ("Bò nướng mỡ chài",            380,  8, 30, 24, "phần", "vietnam"),
    ("Bò băm sả ớt",                300,  8, 26, 18, "đĩa",  "vietnam"),
    ("Beefsteak bò sốt hành",       520, 10, 38, 36, "phần", "vietnam"),
    ("Gân bò xào dứa",              280, 12, 24, 14, "đĩa",  "vietnam"),
    ("Bò cuộn rau củ",              310, 10, 28, 18, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 12. GÀ / VỊT / GIA CẦM (20 món)
    # ══════════════════════════════════════════
    ("Gà hấp gừng",                 260,  4, 30, 14, "phần", "vietnam"),
    ("Gà xào sả ớt",                300,  8, 30, 16, "phần", "vietnam"),
    ("Gà tiềm nấm đông cô",         380, 10, 34, 18, "tô",   "vietnam"),
    ("Gà kho mắm",                  280,  8, 28, 14, "chén", "vietnam"),
    ("Gà kho tiêu",                 290,  6, 30, 16, "chén", "vietnam"),
    ("Chim cút chiên giòn",         380, 12, 28, 24, "con",  "vietnam"),
    ("Chim cút nướng",              320,  6, 28, 20, "con",  "vietnam"),
    ("Vịt xiêm nấu chao",           420,  8, 32, 28, "tô",   "vietnam"),
    ("Vịt om sấu",                  390, 12, 30, 24, "tô",   "vietnam"),
    ("Gà rang sả tỏi",              320,  8, 32, 16, "phần", "vietnam"),
    ("Gà kho khô",                  300,  6, 30, 16, "phần", "vietnam"),
    ("Đùi gà nướng",                350,  4, 36, 20, "chiếc","vietnam"),
    ("Cánh gà nướng mật ong",       380, 14, 28, 22, "phần", "vietnam"),
    ("Cánh gà chiên nước mắm",      400, 16, 28, 24, "phần", "vietnam"),
    ("Gà ủ muối",                   320,  2, 32, 20, "phần", "vietnam"),
    ("Gà trống tơ nướng than",      380,  4, 36, 22, "phần", "vietnam"),
    ("Vịt nướng than",              360,  4, 30, 24, "phần", "vietnam"),
    ("Gà băm xúc bánh đa",          350, 22, 26, 16, "phần", "vietnam"),
    ("Chim bồ câu hầm",             380,  8, 32, 22, "tô",   "vietnam"),
    ("Gà chiên giòn da vàng",       420, 12, 34, 26, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 13. HẢI SẢN ĐA DẠNG (35 món)
    # ══════════════════════════════════════════
    ("Cua rang me",                 360, 14, 28, 18, "phần", "vietnam"),
    ("Ghẹ hấp sả",                  260,  6, 28, 12, "phần", "vietnam"),
    ("Tôm nướng muối",              220,  4, 28, 10, "phần", "vietnam"),
    ("Cá điêu hồng hấp",            260,  4, 28, 14, "phần", "vietnam"),
    ("Cá tai tượng chiên xù",       380, 18, 28, 20, "phần", "vietnam"),
    ("Lươn um chuối đậu",           380, 16, 28, 20, "tô",   "vietnam"),
    ("Ếch chiên bơ",                320, 10, 28, 18, "phần", "vietnam"),
    ("Cá lóc hấp bầu",              260,  8, 26, 12, "phần", "vietnam"),
    ("Cá thu kho nghệ",             290,  8, 28, 14, "phần", "vietnam"),
    ("Cá chép chiên",               340, 10, 28, 20, "phần", "vietnam"),
    ("Sò điệp nướng mỡ hành",       280,  8, 22, 16, "phần", "vietnam"),
    ("Hào nướng phô mai",           260, 10, 18, 16, "phần", "vietnam"),
    ("Cá ngừ áp chảo",              300,  4, 32, 18, "phần", "vietnam"),
    ("Tôm sú hấp nước dừa",         220,  6, 26,  8, "phần", "vietnam"),
    ("Mực xào cải xanh",            280, 10, 24, 14, "đĩa",  "vietnam"),
    ("Tôm đất rang cốm",            260, 12, 22, 12, "đĩa",  "vietnam"),
    ("Cá lăng nướng sả",            280,  4, 30, 14, "phần", "vietnam"),
    ("Mực hấp gừng",                240,  6, 26, 10, "phần", "vietnam"),
    ("Tép rang cơm",                180,  6, 18,  8, "đĩa",  "vietnam"),
    ("Cá bống kho tiêu",            240,  6, 26, 12, "chén", "vietnam"),
    ("Cá quả kho cà chua",          280, 10, 28, 12, "chén", "vietnam"),
    ("Ngao hấp bia",                180,  6, 18,  6, "đĩa",  "vietnam"),
    ("Sò huyết luộc",               140,  4, 16,  5, "đĩa",  "vietnam"),
    ("Ghẹ rang muối",               280,  8, 26, 14, "phần", "vietnam"),
    ("Cá tra kho tộ",               280, 10, 26, 14, "chén", "vietnam"),
    ("Mực nhồi thịt hấp",           300,  8, 28, 16, "phần", "vietnam"),
    ("Tôm hùm hấp bơ",             380,  4, 40, 20, "phần", "vietnam"),
    ("Cá kèo kho rau răm",          240,  8, 24, 12, "chén", "vietnam"),
    ("Cua đồng rang",               200,  6, 22, 10, "phần", "vietnam"),
    ("Hải sản xào XO",              380, 12, 28, 20, "phần", "vietnam"),
    ("Cá rô kho tộ",                260,  8, 26, 12, "chén", "vietnam"),
    ("Cá trê chiên",                320, 10, 28, 18, "phần", "vietnam"),
    ("Tôm chiên xù",                280, 14, 20, 16, "phần", "vietnam"),
    ("Bề bề rang muối",             300, 10, 26, 16, "phần", "vietnam"),
    ("Ốc bươu nhồi sả",             220,  8, 18, 10, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 14. CANH / SÚP (20 món)
    # ══════════════════════════════════════════
    ("Canh dưa cải thịt heo",       140,  8, 12,  5, "tô",   "vietnam"),
    ("Canh chua cá basa",           200, 10, 20,  6, "tô",   "vietnam"),
    ("Canh chua tôm đất",           200, 10, 18,  7, "tô",   "vietnam"),
    ("Canh đậu hũ tôm",             160,  8, 14,  6, "tô",   "vietnam"),
    ("Canh bạc hà dọc mùng",        140,  8, 12,  5, "tô",   "vietnam"),
    ("Súp gà rau củ",               220, 18, 18,  6, "tô",   "vietnam"),
    ("Súp măng cua",                240, 18, 16,  8, "tô",   "vietnam"),
    ("Canh măng vịt",               240, 12, 20, 10, "tô",   "vietnam"),
    ("Canh mồng tơi",                80,  6,  4,  2, "tô",   "vietnam"),
    ("Canh rau khoai lang",          90,  8,  4,  2, "tô",   "vietnam"),
    ("Canh bông thiên lý",          100,  6,  6,  3, "tô",   "vietnam"),
    ("Canh cua nấu bầu",            160,  8, 14,  6, "tô",   "vietnam"),
    ("Canh hến bầu",                150,  8, 14,  5, "tô",   "vietnam"),
    ("Canh chua miền Tây",          220, 12, 20,  7, "tô",   "vietnam"),
    ("Súp bò hầm",                  320, 16, 28, 14, "tô",   "vietnam"),
    ("Canh sườn khoai tây",         260, 18, 18, 10, "tô",   "vietnam"),
    ("Canh rau dền",                 90,  6,  5,  2, "tô",   "vietnam"),
    ("Canh nấm kim châm đậu hũ",    120,  8,  8,  4, "tô",   "vietnam"),
    ("Canh củ hủ dừa",              140, 10, 10,  4, "tô",   "vietnam"),
    ("Súp khoai lang",              180, 28,  5,  4, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 15. RAU / ĐẬU / NẤM (15 món)
    # ══════════════════════════════════════════
    ("Rau cải xào tỏi",              80,  8,  4,  3, "đĩa",  "basic"),
    ("Rau bina xào tỏi",             90,  6,  5,  4, "đĩa",  "basic"),
    ("Mướp xào tôm",                120,  8,  8,  5, "đĩa",  "vietnam"),
    ("Đậu bắp luộc",                 80, 10,  4,  2, "đĩa",  "basic"),
    ("Cải thảo xào nấm",            110,  8,  6,  4, "đĩa",  "basic"),
    ("Bông cải xanh xào bò",        200,  8, 16, 10, "đĩa",  "vietnam"),
    ("Su su xào tỏi",                80,  8,  4,  3, "đĩa",  "basic"),
    ("Cà tím nướng mỡ hành",        150,  8,  4, 10, "đĩa",  "vietnam"),
    ("Khổ qua xào trứng",           140,  8,  8,  7, "đĩa",  "vietnam"),
    ("Đậu đũa xào tôm",             120, 10,  8,  4, "đĩa",  "vietnam"),
    ("Rau muống luộc",               60,  6,  4,  1, "đĩa",  "basic"),
    ("Nấm xào thịt",                180,  8, 14, 10, "đĩa",  "vietnam"),
    ("Khoai tây chiên",             300, 38,  4, 15, "phần", "basic"),
    ("Bắp cải xào giấm",             90, 10,  4,  3, "đĩa",  "basic"),
    ("Rau lang luộc",                80, 10,  4,  2, "đĩa",  "basic"),

    # ══════════════════════════════════════════
    # 16. GỎI / SALAD (12 món)
    # ══════════════════════════════════════════
    ("Gỏi cuốn hải sản",            140, 18, 10,  3, "cuốn", "vietnam"),
    ("Gỏi hải sản trộn",            240, 14, 20,  8, "đĩa",  "vietnam"),
    ("Gỏi măng chua thịt",          200, 16, 14,  8, "đĩa",  "vietnam"),
    ("Gỏi tôm thịt trộn",           220, 14, 18,  8, "đĩa",  "vietnam"),
    ("Gỏi xoài xanh tôm",           180, 20, 12,  6, "đĩa",  "vietnam"),
    ("Gỏi mít non",                 180, 18, 10,  6, "đĩa",  "vietnam"),
    ("Gỏi cá trích",                220,  8, 20, 12, "đĩa",  "vietnam"),
    ("Gỏi su hào",                  140, 12,  8,  5, "đĩa",  "vietnam"),
    ("Gỏi bò Thái",                 280, 12, 24, 14, "đĩa",  "vietnam"),
    ("Gỏi rau muống tôm",           160, 10, 12,  6, "đĩa",  "vietnam"),
    ("Gỏi cuốn bò",                 130, 18, 10,  3, "cuốn", "vietnam"),
    ("Salad rau trộn dầu giấm",     120, 10,  4,  6, "đĩa",  "basic"),

    # ══════════════════════════════════════════
    # 17. LẨU ĐẶC SẢN (10 món)
    # ══════════════════════════════════════════
    ("Lẩu cá kèo",                  480, 40, 36, 16, "phần", "vietnam"),
    ("Lẩu cá mú",                   520, 42, 40, 18, "phần", "vietnam"),
    ("Lẩu gà",                      480, 38, 36, 18, "phần", "vietnam"),
    ("Lẩu dê",                      520, 35, 40, 22, "phần", "vietnam"),
    ("Lẩu nấm chay",                320, 38, 14, 10, "phần", "vietnam"),
    ("Lẩu riêu cua",                480, 42, 28, 16, "phần", "vietnam"),
    ("Lẩu vịt",                     500, 38, 36, 22, "phần", "vietnam"),
    ("Lẩu tôm chua",                460, 40, 34, 16, "phần", "vietnam"),
    ("Lẩu chua cay tứ xuyên",       520, 38, 30, 24, "phần", "vietnam"),
    ("Lẩu mắm miền Tây",            480, 40, 32, 18, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 18. ĂN VẶT / STREET FOOD (25 món)
    # ══════════════════════════════════════════
    ("Chuối chiên",                 180, 28,  2,  7, "cái",  "vietnam"),
    ("Khoai lang chiên",            190, 30,  2,  7, "phần", "vietnam"),
    ("Bò viên sốt tương",           220, 14, 16, 10, "phần", "vietnam"),
    ("Bắp bung phô mai",            160, 28,  5,  5, "phần", "vietnam"),
    ("Xoài lắc muối ớt",            140, 32,  2,  1, "phần", "vietnam"),
    ("Ổi lắc muối ớt",              120, 26,  2,  1, "phần", "vietnam"),
    ("Trái cây dầm",                180, 38,  2,  2, "phần", "vietnam"),
    ("Há cảo chiên",                240, 24, 12, 11, "phần", "vietnam"),
    ("Há cảo hấp",                  200, 22, 12,  7, "phần", "vietnam"),
    ("Sủi cảo",                     240, 24, 12, 10, "phần", "vietnam"),
    ("Bánh tằm bì",                 380, 52, 18, 12, "phần", "vietnam"),
    ("Bánh rế",                     180, 28,  4,  6, "cái",  "vietnam"),
    ("Lạp xưởng nướng than",        320,  6, 14, 26, "phần", "vietnam"),
    ("Hột vịt lộn xào me",          240, 18, 14, 12, "phần", "vietnam"),
    ("Xiên thịt nướng hỗn hợp",    340,  8, 28, 20, "phần", "vietnam"),
    ("Bánh mì que phô mai",         200, 30,  8,  7, "cái",  "vietnam"),
    ("Ốc xào sả",                   200,  8, 16, 10, "phần", "vietnam"),
    ("Trứng cút chiên",             120,  4,  8,  8, "phần", "vietnam"),
    ("Khoai tây lắc phô mai",       280, 38,  6, 12, "phần", "vietnam"),
    ("Bắp rang bơ",                 200, 32,  6,  7, "phần", "vietnam"),
    ("Chả cá chiên lăn bột",        280, 14, 22, 16, "phần", "vietnam"),
    ("Nem cuốn tươi",               120, 16,  8,  3, "cuốn", "vietnam"),
    ("Bánh đa lạc miền Bắc",        300, 45, 10,  9, "phần", "vietnam"),
    ("Bò khô ăn kèm",               220,  5, 28, 10, "50g",  "vietnam"),
    ("Phô mai chiên xù",            260, 14, 10, 18, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 19. TRÁNG MIỆNG / CHÈ (20 món)
    # ══════════════════════════════════════════
    ("Chè hạt sen long nhãn",       240, 48,  5,  4, "chén", "vietnam"),
    ("Chè đậu đỏ",                  210, 42,  6,  3, "chén", "vietnam"),
    ("Chè lá dứa trân châu",        220, 44,  3,  4, "ly",   "vietnam"),
    ("Chè khúc bạch",               200, 38,  5,  4, "ly",   "vietnam"),
    ("Chè sương sáo",               160, 34,  2,  2, "ly",   "vietnam"),
    ("Chè sâm bổ lượng",            200, 40,  4,  3, "ly",   "vietnam"),
    ("Chè đậu phộng nước dừa",      280, 42,  8,  8, "chén", "vietnam"),
    ("Chè xôi nước",                280, 52,  6,  6, "chén", "vietnam"),
    ("Bánh su kem",                 260, 30,  6, 12, "cái",  "vietnam"),
    ("Kem tươi sầu riêng",          320, 32,  4, 20, "phần", "vietnam"),
    ("Kem cốt dừa",                 250, 28,  3, 14, "phần", "vietnam"),
    ("Chè ba màu",                  280, 54,  5,  5, "ly",   "vietnam"),
    ("Bánh cam chiên",              240, 36,  5, 10, "cái",  "vietnam"),
    ("Bánh tiêu nhân đậu",          220, 34,  6,  8, "cái",  "vietnam"),
    ("Chè cháo cám",                160, 32,  4,  2, "chén", "vietnam"),
    ("Kem gelato xoài",             220, 28,  3, 10, "phần", "vietnam"),
    ("Panna cotta dừa",             240, 22,  3, 16, "phần", "vietnam"),
    ("Chè sữa chua xoài",           280, 42,  6,  8, "hũ",   "vietnam"),
    ("Cơm rượu",                    200, 38,  5,  3, "đĩa",  "vietnam"),
    ("Xôi vò chè đường",            320, 60,  8,  6, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 20. ĐỒ UỐNG ĐA DẠNG (20 món)
    # ══════════════════════════════════════════
    ("Sinh tố thanh long",          180, 40,  2,  1, "ly",   "drink"),
    ("Sinh tố mãng cầu",            200, 44,  2,  2, "ly",   "drink"),
    ("Sinh tố dưa hấu",             160, 36,  2,  1, "ly",   "drink"),
    ("Sinh tố ổi",                  180, 38,  3,  2, "ly",   "drink"),
    ("Sinh tố dứa",                 190, 42,  2,  1, "ly",   "drink"),
    ("Nước ép cà rốt",              100, 22,  2,  1, "ly",   "drink"),
    ("Nước ép táo",                 120, 28,  0,  0, "ly",   "drink"),
    ("Nước ép cần tây",              80, 16,  2,  0, "ly",   "drink"),
    ("Trà xanh Matcha",              80, 10,  2,  3, "ly",   "drink"),
    ("Bạc xỉu",                     160, 22,  3,  6, "ly",   "drink"),
    ("Nước sâm bổ lượng",           180, 42,  2,  1, "ly",   "drink"),
    ("Sữa ngô",                     200, 36,  5,  5, "ly",   "drink"),
    ("Trà hoa cúc",                  30,  6,  0,  0, "ly",   "drink"),
    ("Trà atiso",                    20,  4,  0,  0, "ly",   "drink"),
    ("Nước chanh mật ong",          100, 24,  0,  0, "ly",   "drink"),
    ("Soda chanh muối",              80, 20,  0,  0, "ly",   "drink"),
    ("Nước gạo rang",                40,  8,  1,  0, "ly",   "drink"),
    ("Sữa tươi không đường",        130, 12,  7,  7, "hộp",  "basic"),
    ("Cà phê Americano đá",          10,  1,  0,  0, "ly",   "drink"),
    ("Trà sữa Thái",                320, 52,  4, 10, "ly",   "drink"),

    # ══════════════════════════════════════════
    # 21. FAST FOOD (10 món)
    # ══════════════════════════════════════════
    ("Hamburger bò",                480, 42, 28, 22, "cái",  "fastfood"),
    ("Hamburger gà",                420, 40, 24, 20, "cái",  "fastfood"),
    ("KFC gà rán 1 miếng",          350, 22, 24, 18, "miếng","fastfood"),
    ("KFC mì gà",                   560, 68, 28, 18, "phần", "fastfood"),
    ("Lotteria gà giòn",            380, 28, 26, 18, "phần", "fastfood"),
    ("Lotteria beef burger",        480, 42, 26, 22, "cái",  "fastfood"),
    ("Mì Ý sốt thịt bằm",          520, 65, 28, 18, "phần", "fastfood"),
    ("Pizza phô mai",               580, 65, 28, 22, "phần", "fastfood"),
    ("Hot dog bánh mì",             360, 34, 16, 18, "cái",  "fastfood"),
    ("Cơm gà KFC box",              620, 78, 32, 22, "phần", "fastfood"),

    # ══════════════════════════════════════════
    # 22. ĐẶC SẢN VÙNG MIỀN (15 món)
    # ══════════════════════════════════════════
    ("Hủ tiếu Mỹ Tho",              400, 56, 22, 10, "tô",   "vietnam"),
    ("Cơm tấm An Giang",            600, 80, 28, 20, "phần", "vietnam"),
    ("Bún bò giò heo Huế",          460, 60, 28, 12, "tô",   "vietnam"),
    ("Mì Quảng gà",                 490, 64, 24, 12, "tô",   "vietnam"),
    ("Bánh đập Quảng Nam",          280, 46, 10,  7, "phần", "vietnam"),
    ("Cơm hến Huế",                 380, 60, 18,  8, "phần", "vietnam"),
    ("Nem lụi Huế",                 290, 14, 22, 16, "phần", "vietnam"),
    ("Bún bò bắp mềm",              450, 58, 28, 12, "tô",   "vietnam"),
    ("Gỏi cá cơm",                  200,  8, 20, 10, "đĩa",  "vietnam"),
    ("Chả cua biển",                240,  8, 22, 12, "phần", "vietnam"),
    ("Bánh canh Phan Rang",         420, 58, 24, 10, "tô",   "vietnam"),
    ("Bánh tằm Cà Mau",             380, 52, 18, 14, "phần", "vietnam"),
    ("Mắm kho quẹt",                280,  8, 22, 18, "chén", "vietnam"),
    ("Bánh xèo miền Tây",           480, 44, 22, 24, "cái",  "vietnam"),
    ("Mắm kho miền Tây",            300, 10, 22, 18, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 23. MÓN CHAY (25 món)
    # ══════════════════════════════════════════
    ("Bún chay nấm hương",          300, 52, 10,  5, "tô",   "vietnam"),
    ("Mì chay xào nấm",             340, 55, 12,  8, "phần", "vietnam"),
    ("Đậu hũ kho nấm",              200, 10, 14, 10, "chén", "vietnam"),
    ("Nấm hương kho tiêu",          180,  8, 12, 10, "đĩa",  "vietnam"),
    ("Đậu hũ sốt me",               220, 14, 14, 10, "đĩa",  "vietnam"),
    ("Rau củ thập cẩm xào",         160, 14,  8,  7, "đĩa",  "basic"),
    ("Chả chay",                    180, 10, 12, 10, "miếng","vietnam"),
    ("Nem rán chay",                160, 14,  8,  8, "cuốn", "vietnam"),
    ("Canh nấm chay",               100,  8,  6,  3, "tô",   "vietnam"),
    ("Bánh mì chả chay",            320, 50, 10,  8, "ổ",    "vietnam"),
    ("Xôi chay",                    340, 62,  8,  6, "gói",  "vietnam"),
    ("Cháo nấm chay",               190, 36,  6,  3, "tô",   "vietnam"),
    ("Cơm chiên chay",              420, 68, 12, 12, "phần", "vietnam"),
    ("Miến chay nấm đông cô",       330, 56, 10,  6, "phần", "vietnam"),
    ("Đậu phụ hấp gừng",            140,  4, 12,  7, "bìa",  "basic"),
    ("Nấm cuốn rau sống",           150, 12,  8,  6, "phần", "vietnam"),
    ("Đậu xanh ninh dừa",           280, 44, 12,  7, "chén", "vietnam"),
    ("Tàu hũ nước đường",           160, 30,  8,  2, "tô",   "vietnam"),
    ("Chả giò chay",                160, 14,  6,  9, "cuốn", "vietnam"),
    ("Bún nước dừa chay",           320, 55,  8,  8, "tô",   "vietnam"),
    ("Lẩu tofu chay",               300, 36, 14, 10, "phần", "vietnam"),
    ("Salad đậu hũ",                180, 10, 12,  8, "đĩa",  "vietnam"),
    ("Bánh tráng cuộn rau củ",      200, 36,  6,  4, "phần", "vietnam"),
    ("Canh đậu hũ nấm",             130,  8, 10,  5, "tô",   "vietnam"),
    ("Đậu hũ chiên sốt chua ngọt",  250, 16, 14, 14, "đĩa",  "vietnam"),

    # ══════════════════════════════════════════
    # 24. ĐỒ UỐNG / SINH TỐ BỔ SUNG (20 món)
    # ══════════════════════════════════════════
    ("Sinh tố sầu riêng",           380, 45,  4, 22, "ly",   "drink"),
    ("Sinh tố vải thiều",           200, 46,  2,  1, "ly",   "drink"),
    ("Sinh tố nhãn",                190, 44,  2,  1, "ly",   "drink"),
    ("Nước ép bưởi",                100, 22,  2,  0, "ly",   "drink"),
    ("Nước ép dứa tươi",            120, 28,  1,  0, "ly",   "drink"),
    ("Nước ép khế",                  90, 20,  1,  0, "ly",   "drink"),
    ("Trà chanh tươi",               80, 20,  0,  0, "ly",   "drink"),
    ("Trà vải đào",                 180, 42,  0,  0, "ly",   "drink"),
    ("Cà phê Mocha",                280, 32,  5, 12, "ly",   "drink"),
    ("Cà phê Cappuccino",           180, 18,  6,  8, "ly",   "drink"),
    ("Cà phê Latte",                200, 22,  8,  8, "ly",   "drink"),
    ("Nước ép rau xanh",             80, 14,  3,  1, "ly",   "drink"),
    ("Trà gừng mật ong",             90, 22,  0,  0, "ly",   "drink"),
    ("Nước ép cà chua",              80, 16,  2,  0, "ly",   "drink"),
    ("Nước ép lựu",                 140, 32,  1,  0, "ly",   "drink"),
    ("Boba matcha",                 320, 55,  5,  8, "ly",   "drink"),
    ("Boba taro",                   350, 58,  5,  9, "ly",   "drink"),
    ("Sinh tố dừa sữa",             280, 30,  3, 18, "ly",   "drink"),
    ("Kombucha",                     60, 14,  0,  0, "ly",   "drink"),
    ("Sữa Yakult",                   50, 10,  1,  1, "chai", "supplement"),

    # ══════════════════════════════════════════
    # 25. MÓN ĂN GIA ĐÌNH HÀNG NGÀY (25 món)
    # ══════════════════════════════════════════
    ("Trứng chiên hành",            150,  1, 10, 12, "quả",  "basic"),
    ("Trứng ốp la",                 140,  0,  8, 12, "quả",  "basic"),
    ("Trứng bác",                   160,  1, 10, 13, "phần", "basic"),
    ("Dưa leo xào trứng",           140,  6,  8,  9, "đĩa",  "basic"),
    ("Cà chua xào trứng",           160,  8,  8,  9, "đĩa",  "vietnam"),
    ("Thịt bằm xào hành",           280,  5, 24, 18, "đĩa",  "basic"),
    ("Lạp xưởng xào dứa",           320, 14, 14, 22, "đĩa",  "vietnam"),
    ("Trứng vịt muối",              180,  1, 12, 14, "quả",  "basic"),
    ("Cá khô chiên",                240,  2, 26, 14, "phần", "basic"),
    ("Cá hộp sốt cà chua",          180,  6, 18,  8, "hộp",  "basic"),
    ("Thịt cuộn lá lốt",            280,  8, 24, 16, "đĩa",  "vietnam"),
    ("Bí xanh nấu canh",            100,  8,  5,  3, "tô",   "basic"),
    ("Dưa cải kho thịt",            200,  8, 16, 10, "chén", "vietnam"),
    ("Đậu cô ve luộc",               70, 10,  3,  1, "đĩa",  "basic"),
    ("Cải xanh luộc",                60,  6,  4,  1, "đĩa",  "basic"),
    ("Rau cần xào tỏi",              80,  8,  4,  3, "đĩa",  "basic"),
    ("Bạc hà xào tôm",              140,  8, 10,  5, "đĩa",  "vietnam"),
    ("Măng xào thịt",               180, 10, 14,  8, "đĩa",  "vietnam"),
    ("Nấm rơm xào tỏi",             140,  8,  8,  6, "đĩa",  "basic"),
    ("Chuối ngự",                   110, 28,  1,  0, "quả",  "basic"),
    ("Bưởi da xanh",                 90, 22,  2,  0, "200g", "basic"),
    ("Ổi xá lị",                    100, 24,  3,  1, "quả",  "basic"),
    ("Cam sành",                     95, 22,  2,  0, "quả",  "basic"),
    ("Dứa cắt",                      80, 18,  1,  0, "200g", "basic"),
    ("Mít thái",                    160, 40,  2,  0, "200g", "basic"),

    # ══════════════════════════════════════════
    # 26. THỰC PHẨM CƠ BẢN / DINH DƯỠNG (20 món)
    # ══════════════════════════════════════════
    ("Yến mạch nấu nước",           150, 27,  5,  3, "tô",   "basic"),
    ("Yến mạch sữa",                220, 36,  8,  6, "tô",   "basic"),
    ("Bánh mì sandwich lúa mì",     130, 24,  5,  2, "lát",  "basic"),
    ("Bơ đậu phộng",                190,  7,  7, 16, "2tbsp","basic"),
    ("Sữa hạt hạnh nhân",            40,  2,  1,  3, "ly",   "basic"),
    ("Phô mai con bò cười",           70,  2,  4,  5, "tam giác","supplement"),
    ("Hạt điều rang",               580, 30, 18, 46, "100g", "basic"),
    ("Hạt hướng dương",             580, 20, 21, 51, "100g", "basic"),
    ("Hạt chia",                    490, 42, 17, 31, "100g", "supplement"),
    ("Khoai mì luộc",               160, 38,  1,  0, "100g", "basic"),
    ("Khoai từ hấp",                100, 24,  2,  0, "100g", "basic"),
    ("Bí đỏ hấp",                    50, 12,  2,  0, "100g", "basic"),
    ("Cà rốt luộc",                  55, 12,  1,  0, "100g", "basic"),
    ("Đậu xanh nảy mầm",             30,  6,  3,  0, "100g", "basic"),
    ("Sữa đậu nành tươi",           140, 14,  8,  6, "ly",   "basic"),
    ("Đậu hũ non trắng",             80,  2,  8,  4, "bìa",  "basic"),
    ("Natto đậu nành",              190, 12, 16, 10, "gói",  "supplement"),
    ("Dưa hấu cắt",                  80, 18,  1,  0, "200g", "basic"),
    ("Xoài cát Hòa Lộc",            130, 32,  1,  1, "200g", "basic"),
    ("Thanh long ruột đỏ",           80, 18,  2,  0, "200g", "basic"),

    # ══════════════════════════════════════════
    # 27. ĐẶC SẢN THÊM / MÓN LẠ (13 món)
    # ══════════════════════════════════════════
    ("Lươn nướng muối ớt",          280,  4, 28, 16, "phần", "vietnam"),
    ("Dê nướng",                    380,  6, 36, 22, "phần", "vietnam"),
    ("Heo sữa quay",                580,  6, 38, 44, "100g", "vietnam"),
    ("Gà chạy đất nướng",           360,  4, 36, 22, "phần", "vietnam"),
    ("Cá lóc nướng mắm gừng",       290,  6, 30, 14, "phần", "vietnam"),
    ("Vịt lá sen",                  380, 10, 30, 24, "phần", "vietnam"),
    ("Gà xào nấm shiitake",         320, 10, 30, 16, "phần", "vietnam"),
    ("Thịt dê hầm thuốc bắc",       420,  8, 38, 26, "tô",   "vietnam"),
    ("Cua biển rang tiêu xanh",     280,  8, 24, 14, "phần", "vietnam"),
    ("Bò nhúng dấm",                420, 35, 36, 14, "phần", "vietnam"),
    ("Lẩu hải sản chua cay",        520, 42, 36, 18, "phần", "vietnam"),
    ("Cá điêu hồng nướng muối",     280,  2, 30, 14, "phần", "vietnam"),
    ("Ếch nướng muối ớt",           300,  6, 30, 16, "phần", "vietnam"),
]

# ───── BATCH 5 — 500 món bổ sung ─────
SYSTEM_FOODS_V5 = [

    # ══════════════════════════════════════════
    # 1. ẨM THỰC HÀN QUỐC (25 món)
    # ══════════════════════════════════════════
    ("Tteokbokki bánh gạo cay",          380, 68, 10,  8, "phần", "fastfood"),
    ("Kimchi cải thảo",                   40,  6,  2,  1, "100g", "basic"),
    ("Bulgogi bò nướng Hàn",             380, 12, 32, 22, "phần", "fastfood"),
    ("Galbi sườn bò Hàn",                520, 10, 40, 36, "phần", "fastfood"),
    ("Samgyeopsal ba chỉ nướng Hàn",     600,  2, 26, 54, "phần", "fastfood"),
    ("Dakgalbi gà cay Hàn",              420, 22, 34, 20, "phần", "fastfood"),
    ("Japchae miến xào Hàn",             380, 55, 14, 12, "phần", "fastfood"),
    ("Sundubu jjigae đậu hũ cay",        320, 14, 22, 16, "tô",   "fastfood"),
    ("Doenjang jjigae tương đậu Hàn",    280, 12, 18, 14, "tô",   "fastfood"),
    ("Ramyeon mì cay Hàn",               500, 78, 16, 18, "tô",   "fastfood"),
    ("Gà chiên Hàn Quốc",                480, 28, 36, 26, "phần", "fastfood"),
    ("Pajeon bánh hành Hàn",             360, 42, 12, 16, "cái",  "fastfood"),
    ("Juk cháo Hàn Quốc",               280, 50, 10,  4, "tô",   "fastfood"),
    ("Budae jjigae lẩu quân đội",        520, 42, 28, 24, "phần", "fastfood"),
    ("Kimbap cuộn Hàn Quốc",            380, 62, 14,  8, "cuộn", "fastfood"),
    ("Mandu há cảo Hàn",                300, 30, 16, 12, "phần", "fastfood"),
    ("Patbingsu đá bào đậu đỏ",         380, 72,  6,  8, "phần", "fastfood"),
    ("Hotteok bánh chiên đường nâu",     280, 45,  6, 10, "cái",  "fastfood"),
    ("Bánh gạo tteok hấp",              180, 40,  4,  1, "cái",  "fastfood"),
    ("Dakbokkeumtang gà om cay",         480, 20, 38, 24, "phần", "fastfood"),
    ("Kimchi jjigae canh kimchi",        320, 16, 22, 16, "tô",   "fastfood"),
    ("Gyeran mari trứng cuộn Hàn",       180,  2, 14, 12, "phần", "fastfood"),
    ("Haemul pajeon bánh hải sản Hàn",   420, 42, 18, 20, "cái",  "fastfood"),
    ("Seolleongtang súp xương bò Hàn",   280,  8, 28, 14, "tô",   "fastfood"),
    ("Bingsu kem trái cây",              350, 65,  5,  8, "phần", "fastfood"),

    # ══════════════════════════════════════════
    # 2. ẨM THỰC NHẬT BẢN (25 món)
    # ══════════════════════════════════════════
    ("Ramen tonkotsu",                   680, 88, 32, 24, "tô",   "fastfood"),
    ("Ramen shoyu",                      580, 82, 28, 18, "tô",   "fastfood"),
    ("Udon nước dashi",                  420, 72, 16,  6, "tô",   "fastfood"),
    ("Soba kiều mạch lạnh",              360, 65, 18,  4, "phần", "fastfood"),
    ("Sushi cuộn California roll",       300, 48, 14,  6, "phần", "fastfood"),
    ("Sashimi cá hồi",                   200,  0, 28, 10, "phần", "fastfood"),
    ("Tempura tôm rau củ",               340, 28, 18, 18, "phần", "fastfood"),
    ("Tonkatsu heo chiên xù Nhật",       560, 42, 30, 32, "phần", "fastfood"),
    ("Gyoza há cảo Nhật",                280, 28, 14, 12, "phần", "fastfood"),
    ("Takoyaki bạch tuộc nướng",         320, 38, 12, 14, "phần", "fastfood"),
    ("Yakitori xiên gà nướng Nhật",      280,  6, 28, 16, "phần", "fastfood"),
    ("Teriyaki gà",                      380, 18, 36, 18, "phần", "fastfood"),
    ("Miso súp đậu hũ rong biển",         80,  8,  6,  3, "tô",   "fastfood"),
    ("Edamame đậu nành luộc",            120, 10, 12,  5, "phần", "basic"),
    ("Onigiri cơm nắm Nhật",             200, 38,  8,  2, "cái",  "fastfood"),
    ("Okonomiyaki bánh mì Osaka",        420, 42, 16, 22, "cái",  "fastfood"),
    ("Dorayaki nhân đậu đỏ",             280, 48,  6,  8, "cái",  "fastfood"),
    ("Mochi kem nhân kem",               220, 32,  4,  8, "cái",  "fastfood"),
    ("Karaage gà chiên Nhật",            380, 20, 28, 22, "phần", "fastfood"),
    ("Katsudon cơm heo chiên Nhật",      680, 82, 30, 28, "phần", "fastfood"),
    ("Oyakodon cơm gà trứng Nhật",       580, 72, 28, 22, "phần", "fastfood"),
    ("Chawanmushi trứng hấp Nhật",       120,  6, 10,  6, "cái",  "fastfood"),
    ("Sunomono dưa leo chua Nhật",        80, 14,  3,  1, "đĩa",  "basic"),
    ("Tamagoyaki trứng cuộn Nhật",       200,  4, 16, 14, "phần", "fastfood"),
    ("Ochazuke cơm trà Nhật",            280, 48, 12,  4, "tô",   "fastfood"),

    # ══════════════════════════════════════════
    # 3. ẨM THỰC THÁI/TRUNG/QUỐC TẾ (25 món)
    # ══════════════════════════════════════════
    ("Tom yum hải sản Thái",             280, 12, 24, 12, "tô",   "fastfood"),
    ("Pad thai tôm",                     480, 62, 24, 18, "phần", "fastfood"),
    ("Som tum gỏi đu đủ Thái",           200, 22, 10,  8, "đĩa",  "fastfood"),
    ("Cà ri xanh Thái",                  480, 22, 28, 28, "phần", "fastfood"),
    ("Massaman curry Thái",              520, 28, 28, 30, "phần", "fastfood"),
    ("Gà xào lá húng quế Thái",          380, 10, 32, 22, "phần", "fastfood"),
    ("Xôi xoài Thái kiểu truyền thống", 420, 75,  6, 12, "phần", "fastfood"),
    ("Vịt quay Bắc Kinh",                580, 12, 38, 42, "phần", "fastfood"),
    ("Char siu xá xíu",                  380, 14, 30, 24, "100g", "fastfood"),
    ("Bánh bao nhân xá xíu",             280, 38, 14,  8, "cái",  "vietnam"),
    ("Xiaolongbao xúp bao",              280, 28, 14, 12, "phần", "fastfood"),
    ("Cơm gà Hải Nam",                   580, 75, 30, 18, "phần", "fastfood"),
    ("Laksa mì cà ri Sing",              580, 60, 28, 28, "tô",   "fastfood"),
    ("Dim sum thập cẩm",                 350, 32, 18, 16, "phần", "fastfood"),
    ("Nasi goreng cơm chiên Indo",       520, 72, 20, 18, "phần", "fastfood"),
    ("Súp hoành thánh Tàu",              280, 28, 14, 10, "tô",   "fastfood"),
    ("Mì xào Phúc Kiến",                 520, 65, 26, 18, "phần", "fastfood"),
    ("Ngưu nhục phở Đài Loan",           480, 58, 30, 14, "tô",   "fastfood"),
    ("Bánh phồng tôm",                   120, 18,  5,  5, "phần", "vietnam"),
    ("Cháo cá Quảng Đông",               280, 42, 20,  5, "tô",   "fastfood"),
    ("Mì vịt quay Tàu",                  480, 60, 28, 16, "tô",   "fastfood"),
    ("Mì udon xào bò",                   480, 62, 26, 16, "phần", "fastfood"),
    ("Hủ tiếu sa tế",                    420, 55, 22, 12, "tô",   "vietnam"),
    ("Tom kha gai súp dừa Thái",         320, 12, 24, 20, "tô",   "fastfood"),
    ("Pad see ew mì xào nước tương",     460, 60, 24, 16, "phần", "fastfood"),

    # ══════════════════════════════════════════
    # 4. PHỞ/BÚN/MÌ MỚI (20 món)
    # ══════════════════════════════════════════
    ("Phở xương bò đặc biệt",            460, 58, 30, 12, "tô",   "vietnam"),
    ("Phở gà ta truyền thống",           390, 54, 28,  8, "tô",   "vietnam"),
    ("Phở bò viên gân sách",             440, 58, 28, 10, "tô",   "vietnam"),
    ("Phở bò thập cẩm",                  490, 60, 34, 12, "tô",   "vietnam"),
    ("Bún bò sốt đặc biệt",              470, 62, 28, 12, "tô",   "vietnam"),
    ("Bún mắm Trà Vinh",                 440, 58, 22, 12, "tô",   "vietnam"),
    ("Bún nêm hải sản",                  390, 52, 24,  8, "tô",   "vietnam"),
    ("Bún ốc suông đặc biệt",            370, 50, 20,  8, "tô",   "vietnam"),
    ("Bún cá chua cay",                  380, 52, 22,  8, "tô",   "vietnam"),
    ("Bún sả bò",                        460, 58, 28, 14, "tô",   "vietnam"),
    ("Miến lươn",                        380, 56, 22,  8, "tô",   "vietnam"),
    ("Miến xương gà",                    360, 55, 20,  6, "tô",   "vietnam"),
    ("Mì vằn thắn",                      420, 58, 22, 10, "tô",   "vietnam"),
    ("Hủ tiếu mực",                      400, 56, 24, 10, "tô",   "vietnam"),
    ("Hủ tiếu xào hải sản",              460, 60, 26, 12, "phần", "vietnam"),
    ("Hủ tiếu thập cẩm",                 440, 58, 24, 12, "tô",   "vietnam"),
    ("Mì khô chả cá",                    440, 58, 24, 12, "phần", "vietnam"),
    ("Mì vàng xào tôm mực",             510, 64, 28, 16, "phần", "vietnam"),
    ("Bánh canh chả cá Quy Nhơn",        450, 58, 24, 12, "tô",   "vietnam"),
    ("Bánh canh chả tôm",                440, 58, 24, 12, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 5. CƠM MỚI (25 món)
    # ══════════════════════════════════════════
    ("Cơm gà áp chảo",                   560, 72, 32, 20, "phần", "vietnam"),
    ("Cơm bò xào tiêu xanh",             540, 70, 30, 18, "phần", "vietnam"),
    ("Cơm gà xào gừng",                  520, 72, 28, 16, "phần", "vietnam"),
    ("Cơm tôm sốt bơ",                   520, 70, 26, 16, "phần", "vietnam"),
    ("Cơm cá thu áp chảo",               520, 70, 28, 18, "phần", "vietnam"),
    ("Cơm rang hải sản",                 540, 72, 26, 18, "phần", "vietnam"),
    ("Cơm tấm thịt viên",                540, 76, 26, 16, "phần", "vietnam"),
    ("Cơm sườn khoai tây",               540, 78, 26, 16, "phần", "vietnam"),
    ("Cơm gà ủ muối Hải Nam kiểu VN",   560, 74, 30, 20, "phần", "vietnam"),
    ("Cơm hải sản sốt đặc biệt",         520, 68, 30, 18, "phần", "vietnam"),
    ("Cơm thịt viên cà chua",            500, 70, 24, 14, "phần", "vietnam"),
    ("Cơm chiên cà ri",                  520, 72, 20, 18, "phần", "vietnam"),
    ("Cơm đùi gà nướng",                 580, 74, 32, 20, "phần", "vietnam"),
    ("Cơm sốt cà chua bò",               520, 72, 28, 16, "phần", "vietnam"),
    ("Cơm hộp văn phòng thập cẩm",       480, 68, 22, 14, "phần", "vietnam"),
    ("Cơm trứng đúc thịt",               480, 68, 24, 16, "phần", "vietnam"),
    ("Cơm lam gà nướng",                 380, 60, 18,  8, "phần", "vietnam"),
    ("Cơm cá thu kho gừng",              500, 70, 26, 14, "phần", "vietnam"),
    ("Cơm sườn xào chua ngọt",           580, 78, 28, 18, "phần", "vietnam"),
    ("Cơm gà xé nước cốt dừa",           560, 74, 30, 20, "phần", "vietnam"),
    ("Cơm tấm trứng ốp la",              520, 75, 22, 16, "phần", "vietnam"),
    ("Cơm trộn cá hồi kiểu Nhật",        580, 72, 30, 22, "phần", "fastfood"),
    ("Cơm bò khô rang sả",               520, 70, 28, 18, "phần", "vietnam"),
    ("Cơm gà tiêu đen",                  540, 72, 30, 18, "phần", "vietnam"),
    ("Cơm trứng muối chả lụa",           520, 72, 24, 16, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 6. BÁNH CÁC LOẠI MỚI (25 món)
    # ══════════════════════════════════════════
    ("Bánh mì trứng gà nướng",           380, 45, 18, 16, "ổ",    "vietnam"),
    ("Bánh cuốn nhân nấm",               280, 44, 10,  6, "phần", "vietnam"),
    ("Bánh căn nhân trứng",              320, 42, 16, 12, "phần", "vietnam"),
    ("Bánh bèo dĩa Huế",                 280, 48, 10,  6, "phần", "vietnam"),
    ("Bánh mì xốt vang",                 420, 50, 20, 14, "ổ",    "vietnam"),
    ("Bánh mì bò kho",                   440, 52, 22, 16, "ổ",    "vietnam"),
    ("Bánh hỏi lòng gà",                 480, 60, 26, 16, "phần", "vietnam"),
    ("Bánh tráng cuộn bắp thịt",         300, 40, 16, 10, "phần", "vietnam"),
    ("Bánh mướt thịt thưng",             260, 42, 12,  6, "phần", "vietnam"),
    ("Bánh đa cua đồng",                 380, 52, 20, 10, "tô",   "vietnam"),
    ("Bánh uôi",                         160, 30,  4,  3, "cái",  "vietnam"),
    ("Bánh quế giòn",                    140, 22,  3,  5, "cái",  "vietnam"),
    ("Bánh mật ong phô mai",             260, 30,  8, 12, "cái",  "vietnam"),
    ("Bánh bơ nhân kem",                 280, 32,  5, 14, "cái",  "vietnam"),
    ("Bánh nướng đậu xanh",              280, 42,  8,  8, "cái",  "vietnam"),
    ("Bánh chuối nếp nướng",             280, 48,  5,  8, "cái",  "vietnam"),
    ("Bánh đậu đỏ",                      260, 44,  7,  6, "cái",  "vietnam"),
    ("Bánh tẻ nhân thịt",                260, 42, 10,  6, "cái",  "vietnam"),
    ("Bánh xốp mít",                     200, 32,  4,  7, "cái",  "vietnam"),
    ("Bánh dứa xốp",                     220, 32,  4,  8, "cái",  "vietnam"),
    ("Bánh gừng miền Trung",             220, 38,  4,  6, "cái",  "vietnam"),
    ("Bánh lemon tart chanh",            320, 38,  5, 16, "cái",  "fastfood"),
    ("Bánh mousse socola",               380, 36,  6, 24, "miếng","fastfood"),
    ("Bánh bía nhân lá dứa",             280, 42,  6, 10, "cái",  "vietnam"),
    ("Bánh dừa nướng",                   320, 46,  6, 14, "cái",  "vietnam"),

    # ══════════════════════════════════════════
    # 7. THỊT/GIA CẦM MỚI (25 món)
    # ══════════════════════════════════════════
    ("Thịt bò sốt tiêu xanh",            380,  8, 32, 24, "phần", "vietnam"),
    ("Bò sốt kem nấm",                   420, 10, 34, 26, "phần", "vietnam"),
    ("Gà sốt cam",                       360, 20, 32, 16, "phần", "vietnam"),
    ("Gà sốt mật ong",                   380, 22, 32, 18, "phần", "vietnam"),
    ("Thịt bò áp chảo",                  460,  8, 38, 30, "phần", "vietnam"),
    ("Gà roti lò nướng",                 380,  4, 36, 24, "phần", "vietnam"),
    ("Thịt heo om nấm đông cô",          380, 12, 26, 24, "tô",   "vietnam"),
    ("Thịt kho măng khô",                340, 14, 26, 18, "chén", "vietnam"),
    ("Sườn xào gừng hành",               360, 12, 26, 22, "đĩa",  "vietnam"),
    ("Thịt bò nướng vỉ",                 460,  8, 38, 30, "phần", "vietnam"),
    ("Gà kho lá chanh",                  300,  8, 28, 16, "chén", "vietnam"),
    ("Chả lụa thui",                     200,  4, 16, 12, "100g", "vietnam"),
    ("Heo quay da giòn",                 440,  6, 34, 30, "100g", "vietnam"),
    ("Gà quay mật ong",                  420, 16, 36, 24, "phần", "vietnam"),
    ("Vịt kho gừng",                     360, 10, 28, 22, "chén", "vietnam"),
    ("Cánh gà sốt tiêu đen",             380, 10, 28, 24, "phần", "vietnam"),
    ("Chân gà ngâm sả ớt",              280,  6, 22, 18, "phần", "vietnam"),
    ("Thịt bò cuộn nấm",                 340,  8, 30, 20, "phần", "vietnam"),
    ("Gà om tiêu xanh",                  360,  8, 32, 22, "tô",   "vietnam"),
    ("Thịt heo rim mắm",                 380, 10, 26, 26, "chén", "vietnam"),
    ("Cánh gà chiên giòn sốt Thái",      420, 16, 30, 26, "phần", "vietnam"),
    ("Bò bít tết phô mai",               580, 10, 42, 40, "phần", "vietnam"),
    ("Thịt bò sốt hành tây kiểu Pháp",  440,  8, 36, 28, "phần", "vietnam"),
    ("Gà kho riềng mắm tôm",             320,  8, 28, 18, "chén", "vietnam"),
    ("Thịt heo kho tương hoisin",         360, 14, 26, 20, "chén", "vietnam"),

    # ══════════════════════════════════════════
    # 8. HẢI SẢN MỚI (25 món)
    # ══════════════════════════════════════════
    ("Cá hồi áp chảo sốt cam",           320,  8, 32, 18, "phần", "vietnam"),
    ("Tôm hấp sả gừng",                  200,  4, 26,  8, "phần", "vietnam"),
    ("Cá ngừ nướng muối ớt",             280,  4, 32, 14, "phần", "vietnam"),
    ("Mực nướng kiểu Nhật",              260,  8, 26, 12, "phần", "vietnam"),
    ("Tôm sú nướng phô mai",             280,  6, 26, 14, "phần", "vietnam"),
    ("Cua cà mau hấp bia",               320,  6, 28, 18, "phần", "vietnam"),
    ("Ốc gạo xào sả",                    200,  8, 16, 10, "phần", "vietnam"),
    ("Ốc mỡ hấp nước dừa",               180,  6, 16,  8, "phần", "vietnam"),
    ("Cá đuối xào sả ớt",                300,  8, 26, 16, "phần", "vietnam"),
    ("Cá chim chiên",                    320,  8, 28, 18, "phần", "vietnam"),
    ("Nghêu xào chuối đậu",              200, 14, 18,  6, "đĩa",  "vietnam"),
    ("Sò lông hấp nước dừa",             200,  8, 20,  8, "đĩa",  "vietnam"),
    ("Cá thu nướng lá chuối",             300,  4, 30, 16, "phần", "vietnam"),
    ("Ếch xào sả ớt",                    300,  8, 28, 16, "phần", "vietnam"),
    ("Hải sản nướng vỉ hỗn hợp",         420,  8, 36, 24, "phần", "vietnam"),
    ("Tôm xào bơ tỏi",                   260,  6, 26, 14, "phần", "vietnam"),
    ("Mực rim mật ong",                  260, 14, 24, 10, "phần", "vietnam"),
    ("Tôm mực hấp đặc biệt",             280,  6, 28, 12, "phần", "vietnam"),
    ("Cá hố chiên giòn",                 280, 10, 26, 14, "phần", "vietnam"),
    ("Sứa trộn tôm thịt",                140,  8, 14,  5, "đĩa",  "vietnam"),
    ("Tôm lăn bột thảo mộc",             300, 18, 18, 16, "phần", "vietnam"),
    ("Cua rang sốt đặc biệt",            360, 12, 28, 20, "phần", "vietnam"),
    ("Lươn nướng mắm gừng",              300,  4, 28, 16, "phần", "vietnam"),
    ("Bề bề hấp sả gừng",                280,  8, 24, 14, "phần", "vietnam"),
    ("Cá điêu hồng nướng muối ớt",       280,  4, 28, 14, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 9. CANH / LẨU MỚI (20 món)
    # ══════════════════════════════════════════
    ("Canh cá ngừ chua",                 200, 10, 22,  7, "tô",   "vietnam"),
    ("Canh mướp hương thịt",             100,  8,  5,  3, "tô",   "vietnam"),
    ("Canh bí xanh tôm",                 140, 10, 10,  4, "tô",   "vietnam"),
    ("Canh cua bắp non",                 180, 12, 14,  6, "tô",   "vietnam"),
    ("Canh cà chua trứng",               160, 10,  8,  8, "tô",   "vietnam"),
    ("Canh sườn hạt sen",                280, 22, 18, 10, "tô",   "vietnam"),
    ("Canh đuôi bò hầm rau củ",          380, 18, 30, 18, "tô",   "vietnam"),
    ("Canh bí đỏ nước cốt dừa",          180, 18,  4, 10, "tô",   "vietnam"),
    ("Canh chua đầu cá hồi",             220, 12, 22,  8, "tô",   "vietnam"),
    ("Canh nấm rơm đậu hũ",             120,  8,  8,  4, "tô",   "vietnam"),
    ("Canh xương hầm rau củ",            280, 16, 22, 12, "tô",   "vietnam"),
    ("Canh nghêu bầu",                   140,  8, 14,  4, "tô",   "vietnam"),
    ("Canh rau muống chua",              120,  8, 10,  4, "tô",   "vietnam"),
    ("Lẩu sukiyaki Nhật",                580, 38, 38, 24, "phần", "fastfood"),
    ("Lẩu kim chi Hàn",                  520, 38, 30, 22, "phần", "fastfood"),
    ("Lẩu Tứ Xuyên cay",                560, 36, 32, 28, "phần", "fastfood"),
    ("Lẩu bò tái nhúng dấm",             520, 40, 40, 20, "phần", "vietnam"),
    ("Lẩu heo quay đặc biệt",            560, 38, 36, 28, "phần", "vietnam"),
    ("Lẩu cá đặc biệt",                  480, 38, 36, 18, "phần", "vietnam"),
    ("Lẩu gà đặc biệt",                  500, 38, 38, 20, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 10. GỎI / SALAD MỚI (15 món)
    # ══════════════════════════════════════════
    ("Gỏi tôm hành tây",                 200, 14, 16,  8, "đĩa",  "vietnam"),
    ("Gỏi sứa tôm thịt",                 160, 10, 14,  5, "đĩa",  "vietnam"),
    ("Gỏi dưa leo thịt bò",              220, 12, 20, 10, "đĩa",  "vietnam"),
    ("Gỏi cóc xanh ớt chua",             140, 22,  4,  4, "đĩa",  "vietnam"),
    ("Gỏi cải bắp tôm",                  180, 14, 14,  6, "đĩa",  "vietnam"),
    ("Gỏi xoài hải sản",                 200, 20, 14,  7, "đĩa",  "vietnam"),
    ("Gỏi măng tươi",                    160, 16, 10,  6, "đĩa",  "vietnam"),
    ("Salad Caesar gà",                  320, 14, 26, 18, "đĩa",  "fastfood"),
    ("Salad trộn dầu mè",                160, 12,  6, 10, "đĩa",  "basic"),
    ("Salad hải sản trộn dầu tỏi",       240, 12, 22, 10, "đĩa",  "fastfood"),
    ("Nộm su hào cà rốt",                120, 14,  6,  4, "đĩa",  "vietnam"),
    ("Nộm hoa chuối",                    200, 16, 12,  8, "đĩa",  "vietnam"),
    ("Salad cá ngừ mù tạt",              280,  8, 28, 14, "đĩa",  "fastfood"),
    ("Gỏi gà trộn ớt xanh",              300, 10, 26, 16, "đĩa",  "vietnam"),
    ("Gỏi rau sống thập cẩm",            140, 12,  6,  6, "đĩa",  "basic"),

    # ══════════════════════════════════════════
    # 11. ĂN VẶT MỚI (20 món)
    # ══════════════════════════════════════════
    ("Bánh tráng cuộn bò khô",           280, 36, 18,  8, "phần", "vietnam"),
    ("Khô gà lá chanh",                  280,  6, 34, 12, "100g", "vietnam"),
    ("Khô mực ăn vặt",                   200,  4, 30,  6, "100g", "vietnam"),
    ("Khô bò sốt sa tế",                 240,  6, 32, 10, "100g", "vietnam"),
    ("Nem chua rán",                     200, 16, 10, 10, "cuốn", "vietnam"),
    ("Chả mực chiên",                    260, 12, 20, 14, "phần", "vietnam"),
    ("Đùi ếch chiên bơ",                 320, 10, 28, 20, "phần", "vietnam"),
    ("Bánh tráng nướng thịt xông khói",  300, 42, 14, 10, "cái",  "vietnam"),
    ("Cơm cuộn phô mai",                 360, 58, 14, 10, "cuộn", "vietnam"),
    ("Chân gà chua cay",                 240,  6, 20, 16, "phần", "vietnam"),
    ("Bắp sữa nướng",                    180, 30,  5,  5, "bắp",  "vietnam"),
    ("Khoai tây thô chiên",              280, 36,  4, 14, "phần", "fastfood"),
    ("Mực khô nướng than",               200,  4, 28,  8, "phần", "vietnam"),
    ("Bò viên sốt sa tế",                260, 12, 20, 14, "phần", "vietnam"),
    ("Hột vịt lộn nướng",                200, 12, 14, 10, "quả",  "vietnam"),
    ("Bánh ngói miền Trung",             260, 40,  8,  8, "cái",  "vietnam"),
    ("Bạch tuộc rim sốt",                220, 10, 24, 10, "phần", "vietnam"),
    ("Tôm nướng muối chanh",             200,  4, 26,  8, "phần", "vietnam"),
    ("Bánh mì gà sốt đặc biệt",          420, 50, 22, 14, "ổ",    "vietnam"),
    ("Cà chua bi nhồi thịt",             200, 10, 16, 10, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 12. ĐỒ UỐNG MỚI (20 món)
    # ══════════════════════════════════════════
    ("Cà phê muối",                      200, 24,  4,  8, "ly",   "drink"),
    ("Cà phê dừa",                       280, 30,  4, 14, "ly",   "drink"),
    ("Cà phê phô mai Đà Lạt",            320, 28,  6, 18, "ly",   "drink"),
    ("Cà phê chồn",                       80,  6,  1,  4, "ly",   "drink"),
    ("Hồng trà sữa",                     280, 46,  3,  8, "ly",   "drink"),
    ("Trà sen",                           20,  4,  0,  0, "ly",   "drink"),
    ("Nước ép thanh long",               100, 22,  2,  0, "ly",   "drink"),
    ("Nước ép nho",                      130, 30,  1,  0, "ly",   "drink"),
    ("Sinh tố nếp cẩm sữa dừa",         260, 52,  5,  4, "ly",   "drink"),
    ("Smoothie rau xanh táo",            160, 28,  5,  3, "ly",   "drink"),
    ("Trà ô long sữa",                   280, 44,  3,  8, "ly",   "drink"),
    ("Cà phê sữa nóng",                  180, 26,  4,  6, "ly",   "drink"),
    ("Sinh tố khoai môn",                280, 52,  4,  6, "ly",   "drink"),
    ("Trà sữa gừng đường nâu",           320, 55,  3,  8, "ly",   "drink"),
    ("Chanh leo soda",                   120, 28,  1,  0, "ly",   "drink"),
    ("Cacao sữa nóng",                   220, 28,  6,  8, "ly",   "drink"),
    ("Nước ép mận sấy",                  110, 26,  1,  0, "ly",   "drink"),
    ("Sinh tố chôm chôm",                200, 44,  2,  1, "ly",   "drink"),
    ("Nước detox dưa hấu chanh",          80, 18,  1,  0, "ly",   "drink"),
    ("Matcha latte đá",                  180, 22,  4,  8, "ly",   "drink"),

    # ══════════════════════════════════════════
    # 13. TRÁNG MIỆNG / CHÈ MỚI (20 món)
    # ══════════════════════════════════════════
    ("Chè hạt sen nhãn nhục",            260, 52,  5,  4, "chén", "vietnam"),
    ("Chè long nhãn đậu đỏ",             240, 48,  5,  4, "chén", "vietnam"),
    ("Chè bắp dừa",                      240, 46,  4,  6, "chén", "vietnam"),
    ("Chè khoai môn bột báng",           260, 48,  4,  7, "chén", "vietnam"),
    ("Chè nếp lá dứa",                   280, 54,  5,  6, "chén", "vietnam"),
    ("Kem dừa dứa",                      260, 30,  3, 14, "phần", "vietnam"),
    ("Kem matcha Nhật",                  240, 26,  4, 12, "phần", "fastfood"),
    ("Thạch xoài",                       100, 22,  1,  1, "hũ",   "vietnam"),
    ("Thạch cà phê",                      80, 18,  1,  1, "hũ",   "vietnam"),
    ("Bánh bông lan trứng muối",         320, 38,  8, 14, "miếng","vietnam"),
    ("Bánh crepe Pháp",                  280, 32,  8, 12, "cái",  "fastfood"),
    ("Bánh waffles",                     350, 42,  8, 16, "cái",  "fastfood"),
    ("Bánh macaron",                     220, 28,  4, 10, "cái",  "fastfood"),
    ("Tiramisu",                         380, 36,  8, 22, "miếng","fastfood"),
    ("Cheesecake vani",                  420, 38,  8, 26, "miếng","fastfood"),
    ("Pudding hạt chia xoài",            280, 36,  8, 12, "hũ",   "basic"),
    ("Granola sữa chua trái cây",        360, 48, 12, 14, "bát",  "basic"),
    ("Açaí bowl",                        380, 52,  8, 16, "bát",  "fastfood"),
    ("Fruit tart bánh hoa quả",          320, 38,  6, 14, "cái",  "fastfood"),
    ("Chè khoai sọ dừa",                 250, 46,  4,  6, "chén", "vietnam"),

    # ══════════════════════════════════════════
    # 14. THỰC PHẨM DINH DƯỠNG MỚI (20 món)
    # ══════════════════════════════════════════
    ("Whey protein bột vị vanilla",      120,  4, 25,  2, "muỗng","supplement"),
    ("Collagen peptide",                  60,  0, 15,  0, "muỗng","supplement"),
    ("Nước hầm xương bò",                 60,  2, 10,  2, "ly",   "supplement"),
    ("Kefir sữa men",                    100, 12,  8,  4, "ly",   "supplement"),
    ("Hạnh nhân sống",                   580, 22, 21, 50, "100g", "basic"),
    ("Hạt óc chó",                       650, 14, 15, 65, "100g", "basic"),
    ("Hạt dẻ rang",                      360, 76,  5,  3, "100g", "basic"),
    ("Tempeh đậu nành lên men",          190, 10, 20, 10, "100g", "basic"),
    ("Quinoa nấu chín",                  120, 22,  4,  2, "chén", "basic"),
    ("Lúa mạch (barley) nấu",            130, 28,  4,  1, "chén", "basic"),
    ("Đậu lăng nấu chín",                116, 20,  9,  0, "100g", "basic"),
    ("Phô mai Cottage",                  100,  4, 12,  4, "100g", "basic"),
    ("Quả việt quất",                     57, 14,  1,  0, "100g", "basic"),
    ("Táo xanh Fuji",                     80, 20,  0,  0, "quả",  "basic"),
    ("Lê Hàn Quốc",                       85, 22,  1,  0, "quả",  "basic"),
    ("Đào vàng",                          80, 20,  2,  0, "quả",  "basic"),
    ("Dâu tây",                           60, 14,  1,  0, "100g", "basic"),
    ("Nho xanh",                          90, 22,  1,  0, "100g", "basic"),
    ("Măng cụt",                         100, 24,  1,  1, "100g", "basic"),
    ("Vải thiều",                        130, 32,  1,  0, "100g", "basic"),

    # ══════════════════════════════════════════
    # 15. ĐẶC SẢN VÙNG MIỀN MỚI (15 món)
    # ══════════════════════════════════════════
    ("Bún bò sườn đặc Huế",              480, 60, 30, 14, "tô",   "vietnam"),
    ("Mì Quảng cá lóc",                  480, 64, 26, 12, "tô",   "vietnam"),
    ("Cao lầu mực Hội An",               460, 62, 24, 14, "tô",   "vietnam"),
    ("Bún mắm Vĩnh Long",                440, 58, 22, 12, "tô",   "vietnam"),
    ("Bánh ít Trà Vinh",                 200, 36,  5,  5, "cái",  "vietnam"),
    ("Hủ tiếu Đồng Nai",                 410, 56, 22, 10, "tô",   "vietnam"),
    ("Cơm tấm Sài Gòn đặc biệt",         680, 88, 32, 24, "phần", "vietnam"),
    ("Bún riêu cua đặc Hà Nội",          390, 52, 20, 10, "tô",   "vietnam"),
    ("Bánh mỳ Huế đặc sản",             380, 48, 18, 12, "ổ",    "vietnam"),
    ("Bánh căn Phan Rang đặc biệt",      340, 42, 16, 14, "phần", "vietnam"),
    ("Cơm gà Tam Kỳ",                    580, 74, 30, 18, "phần", "vietnam"),
    ("Bún thịt nướng Huế",               520, 70, 28, 14, "phần", "vietnam"),
    ("Cơm bắp An Giang",                 380, 68,  8,  6, "phần", "vietnam"),
    ("Bánh hỏi lá dừa Bến Tre",          400, 60, 14, 12, "phần", "vietnam"),
    ("Phở Hà Nội chuẩn vị",             430, 57, 28,  9, "tô",   "vietnam"),

    # ══════════════════════════════════════════
    # 16. MÓN KHO / OM / RIM (15 món)
    # ══════════════════════════════════════════
    ("Cá thu om dưa cải",                280, 10, 26, 14, "tô",   "vietnam"),
    ("Thịt heo kho măng khô",            360, 14, 26, 20, "chén", "vietnam"),
    ("Trứng kho thịt ba chỉ",            280,  6, 20, 18, "chén", "vietnam"),
    ("Cá lóc om chuối xanh",             300, 16, 28, 12, "tô",   "vietnam"),
    ("Đậu hũ kho tương",                 200, 10, 14, 10, "chén", "vietnam"),
    ("Sườn kho dứa",                     380, 18, 26, 22, "chén", "vietnam"),
    ("Thịt bò kho tiêu",                 340,  8, 28, 20, "chén", "vietnam"),
    ("Cá rô phi kho nghệ",               240,  8, 24, 12, "chén", "vietnam"),
    ("Tôm rim cà chua",                  260, 14, 22, 12, "đĩa",  "vietnam"),
    ("Cá trắm kho riềng",                280,  8, 26, 14, "chén", "vietnam"),
    ("Vịt om dưa cải",                   380, 12, 28, 24, "tô",   "vietnam"),
    ("Cá trê kho tiêu",                  260,  8, 24, 14, "chén", "vietnam"),
    ("Thịt bò sốt vang kiểu Pháp",       440, 16, 34, 26, "phần", "vietnam"),
    ("Gà om nấm thập cẩm",               360, 10, 32, 20, "tô",   "vietnam"),
    ("Cua xào me tỏi",                   340, 16, 26, 18, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 17. BÁNH MÌ / BÁNH NGỌT TÂY (10 món)
    # ══════════════════════════════════════════
    ("Bánh mì sandwich BLT",             400, 38, 20, 18, "cái",  "fastfood"),
    ("Sandwich gà nướng",                420, 40, 30, 14, "cái",  "fastfood"),
    ("Bánh mì baguette truyền thống",    260, 52,  8,  2, "ổ",    "vietnam"),
    ("Croissant thịt phô mai",           420, 36, 18, 22, "cái",  "fastfood"),
    ("Bánh muffin việt quất",            340, 44,  6, 16, "cái",  "fastfood"),
    ("Bánh cupcake vani kem",            360, 46,  4, 18, "cái",  "fastfood"),
    ("Bánh brownie chocolate",           400, 48,  6, 22, "miếng","fastfood"),
    ("Cookies bơ hạt",                   180, 22,  3, 10, "cái",  "fastfood"),
    ("Bánh scone bơ",                    320, 40,  6, 16, "cái",  "fastfood"),
    ("Bánh eclair kem sốt caramel",      300, 34,  6, 14, "cái",  "fastfood"),

    # ══════════════════════════════════════════
    # 18. BỮA SÁNG ĐẶC BIỆT (10 món)
    # ══════════════════════════════════════════
    ("Xôi sáng thập cẩm đặc biệt",      450, 68, 20, 12, "phần", "vietnam"),
    ("Bánh mì trứng chiên sáng sớm",     360, 38, 14, 18, "ổ",    "vietnam"),
    ("Phở bò thập cẩm đặc biệt",        490, 60, 34, 12, "tô",   "vietnam"),
    ("Bún mọc",                          380, 52, 22,  8, "tô",   "vietnam"),
    ("Cháo đậu trắng",                   220, 38,  8,  3, "tô",   "vietnam"),
    ("Hủ tiếu bò nước",                  400, 55, 24, 10, "tô",   "vietnam"),
    ("Bánh ướt nhân nấm mộc nhĩ",       260, 42,  8,  6, "phần", "vietnam"),
    ("Mì vằn thắn tôm thịt",            440, 58, 24, 12, "tô",   "vietnam"),
    ("Bánh cuốn sáng nóng",              320, 48, 14,  7, "phần", "vietnam"),
    ("Xôi đặc biệt sáng",               460, 70, 20, 12, "phần", "vietnam"),

    # ══════════════════════════════════════════
    # 19. THỰC PHẨM/NGUYÊN LIỆU CỤ THỂ (15 món)
    # ══════════════════════════════════════════
    ("Sữa đậu nành có đường",            160, 22,  6,  5, "ly",   "basic"),
    ("Trứng gà công nghiệp",              70,  0,  6,  5, "quả",  "basic"),
    ("Trứng gà thả vườn",                 85,  0,  7,  6, "quả",  "basic"),
    ("Cá viên chiên",                    200, 14, 14, 10, "phần", "vietnam"),
    ("Bò viên thật sự",                  220, 10, 18, 12, "phần", "vietnam"),
    ("Lạp sườn tươi nướng",              350,  8, 16, 28, "100g", "vietnam"),
    ("Chả bò thái lát",                  240,  4, 20, 16, "100g", "vietnam"),
    ("Giò xào (giò thủ) thái",           220,  4, 18, 14, "100g", "vietnam"),
    ("Pate gan lợn",                     280,  4, 16, 22, "100g", "vietnam"),
    ("Phô mai mozzarella",               300,  2, 22, 22, "100g", "basic"),
    ("Phô mai cheddar",                  400,  1, 24, 32, "100g", "basic"),
    ("Lòng đỏ trứng vịt muối",           271,  2, 14, 24, "quả",  "basic"),
    ("Thịt xông khói",                   420,  1, 22, 36, "100g", "basic"),
    ("Đùi gà tây nướng",                 250,  0, 32, 14, "100g", "basic"),
    ("Tôm khô",                          280,  2, 56,  4, "100g", "basic"),

    # ══════════════════════════════════════════
    # 20. SÚP QUỐC TẾ / MÓN ĐẶC BIỆT (15 món)
    # ══════════════════════════════════════════
    ("Súp hành tây Pháp",                320, 28, 12, 18, "tô",   "fastfood"),
    ("Chowder hải sản Mỹ",               420, 28, 22, 26, "tô",   "fastfood"),
    ("Minestrone súp rau Ý",             220, 28, 10,  6, "tô",   "fastfood"),
    ("Borscht súp củ dền Nga",           200, 22,  8,  8, "tô",   "fastfood"),
    ("Pho Bo truyen thong Bac",          420, 56, 26,  8, "tô",   "vietnam"),
    ("Bún thịt xào đặc biệt",            480, 62, 26, 14, "phần", "vietnam"),
    ("Gà hầm khoai tây cà rốt",          380, 22, 30, 16, "tô",   "vietnam"),
    ("Cà ri dê khoai mì",                480, 30, 36, 24, "tô",   "vietnam"),
    ("Cà ri bò thơm",                    460, 28, 34, 22, "tô",   "vietnam"),
    ("Thịt heo tiềm thuốc bắc",          400, 12, 30, 26, "tô",   "vietnam"),
    ("Gà hấp muối (white chicken)",      300,  2, 30, 20, "phần", "vietnam"),
    ("Cá ngừ sốt đặc biệt",             320,  8, 32, 18, "phần", "vietnam"),
    ("Mực sốt tiêu xanh",                300, 10, 26, 16, "phần", "vietnam"),
    ("Cua hoàng đế sốt bơ",              480,  8, 44, 28, "phần", "fastfood"),
    ("Tôm hùm Alaska nướng",             380,  4, 42, 20, "phần", "fastfood"),

    # ══════════════════════════════════════════
    # 21. MÓN XÀO THÊM (20 món)
    # ══════════════════════════════════════════
    ("Thịt bò xào nấm",                  300,  8, 28, 16, "đĩa",  "vietnam"),
    ("Tôm xào đậu hà lan",               240, 10, 22, 12, "đĩa",  "vietnam"),
    ("Gà xào dứa",                       320, 16, 30, 14, "đĩa",  "vietnam"),
    ("Bạch tuộc xào sả ớt",              240,  8, 26, 10, "đĩa",  "vietnam"),
    ("Thịt heo xào đậu que",             260, 10, 22, 14, "đĩa",  "vietnam"),
    ("Nghêu xào sả ớt",                  180,  8, 18,  6, "đĩa",  "vietnam"),
    ("Bông cải trắng xào tỏi",           100, 10,  5,  4, "đĩa",  "basic"),
    ("Đậu phụ xào nấm hương",            200,  8, 14, 12, "đĩa",  "vietnam"),
    ("Gà xào bắp non",                   300, 14, 28, 14, "đĩa",  "vietnam"),
    ("Cải ngọt xào bò",                  220,  8, 20, 10, "đĩa",  "vietnam"),
    ("Tôm xào măng tươi",                260, 12, 22, 12, "đĩa",  "vietnam"),
    ("Mực xào ớt chuông",                260, 10, 24, 12, "đĩa",  "vietnam"),
    ("Cà tím xào thịt",                  220, 10, 14, 12, "đĩa",  "vietnam"),
    ("Nấm đông cô xào thịt",             200,  8, 16, 10, "đĩa",  "vietnam"),
    ("Giá xào hẹ",                       120,  8,  8,  5, "đĩa",  "vietnam"),
    ("Thịt bò xào rau bina",             280,  8, 26, 14, "đĩa",  "vietnam"),
    ("Tôm xào trứng",                    280,  6, 22, 16, "đĩa",  "vietnam"),
    ("Thịt heo xào ớt chuông",           280, 10, 22, 16, "đĩa",  "vietnam"),
    ("Gà xào măng le",                   320, 12, 28, 16, "đĩa",  "vietnam"),
    ("Mực xào cần tỏi",                  240,  8, 22, 12, "đĩa",  "vietnam"),

    # ══════════════════════════════════════════
    # 22. ĐỒ UỐNG THÊM (15 món)
    # ══════════════════════════════════════════
    ("Sinh tố chanh dây",                180, 38,  3,  2, "ly",   "drink"),
    ("Sinh tố mãng cầu xiêm",            200, 44,  2,  2, "ly",   "drink"),
    ("Sinh tố bơ socola",                380, 30,  5, 28, "ly",   "drink"),
    ("Nước ép dưa lưới",                 100, 22,  1,  0, "ly",   "drink"),
    ("Nước ép gừng nghệ",                 80, 18,  1,  1, "ly",   "drink"),
    ("Sinh tố chuối ngũ cốc",            280, 52,  6,  6, "ly",   "drink"),
    ("Sinh tố thơm cà rốt",              180, 40,  2,  1, "ly",   "drink"),
    ("Trà thảo mộc hoa hồng",             20,  4,  0,  0, "ly",   "drink"),
    ("Cà phê kem sữa tươi",              280, 24,  5, 16, "ly",   "drink"),
    ("Trà xanh Thái không đường",         40,  8,  0,  0, "ly",   "drink"),
    ("Soda việt quất",                   120, 28,  1,  0, "ly",   "drink"),
    ("Chanh dây mật ong đá",             140, 32,  1,  1, "ly",   "drink"),
    ("Trà hoa đào",                       60, 14,  0,  0, "ly",   "drink"),
    ("Nước chanh gừng mật ong nóng",     110, 26,  0,  0, "ly",   "drink"),
    ("Sinh tố cóc xanh",                 140, 28,  2,  2, "ly",   "drink"),

    # ══════════════════════════════════════════
    # 23. TRÁNG MIỆNG THÊM (15 món)
    # ══════════════════════════════════════════
    ("Chè sương nổi lá dứa",             180, 36,  3,  3, "ly",   "vietnam"),
    ("Chuối ngâm nước cốt dừa",          280, 52,  2,  8, "phần", "vietnam"),
    ("Kem xôi",                          350, 58,  6, 12, "phần", "vietnam"),
    ("Bánh su kem socola",               280, 30,  6, 14, "cái",  "fastfood"),
    ("Bánh opera",                       380, 36,  8, 22, "miếng","fastfood"),
    ("Crème brûlée",                     340, 28,  6, 22, "cái",  "fastfood"),
    ("Mousse xoài",                      240, 28,  4, 12, "hũ",   "fastfood"),
    ("Bánh cốm Hà Nội",                  260, 48,  6,  5, "cái",  "vietnam"),
    ("Chè thưng đặc biệt",               280, 50,  6,  7, "chén", "vietnam"),
    ("Chè bơ đậu xanh",                  260, 44,  6,  6, "chén", "vietnam"),
    ("Bánh đúc heo quay",                320, 42, 16, 10, "phần", "vietnam"),
    ("Panna cotta trái cây",             260, 24,  3, 17, "phần", "fastfood"),
    ("Thạch sương sáo",                   80, 18,  1,  0, "hũ",   "vietnam"),
    ("Chè đậu ván",                      200, 38,  7,  3, "chén", "vietnam"),
    ("Chè khoai sọ bột báng",            250, 46,  4,  6, "chén", "vietnam"),

    # ══════════════════════════════════════════
    # 24. NGUYÊN LIỆU / THỰC PHẨM THÊM (14 món)
    # ══════════════════════════════════════════
    ("Sữa chua Hy Lạp",                  100,  6, 10,  3, "hộp",  "supplement"),
    ("Bông cải xanh hấp",                 55, 10,  4,  1, "100g", "basic"),
    ("Cải bó xôi sống",                   23,  4,  3,  0, "100g", "basic"),
    ("Khoai lang tím hấp",                90, 21,  2,  0, "100g", "basic"),
    ("Ngô hấp chín",                     100, 22,  3,  1, "bắp",  "basic"),
    ("Hành tây chiên giòn",              380, 38,  6, 22, "100g", "basic"),
    ("Quả dứa tươi cắt",                  80, 18,  1,  0, "200g", "basic"),
    ("Ớt chuông đỏ sống",                 31,  6,  1,  0, "100g", "basic"),
    ("Cần tây xanh sống",                 16,  3,  1,  0, "100g", "basic"),
    ("Cải thảo tươi",                     16,  3,  1,  0, "100g", "basic"),
    ("Hạt lanh (flaxseed)",              534, 29, 18, 42, "100g", "basic"),
    ("Đậu phộng nguyên vỏ nướng",        580, 16, 26, 50, "100g", "basic"),
    ("Sữa hạt yến mạch",                  45,  7,  2,  1, "ly",   "basic"),
    ("Nước ép dưa chuột",                 16,  3,  1,  0, "ly",   "drink"),

    # ══════════════════════════════════════════
    # 25. MÓN THÊM ĐẶC BIỆT (20 món)
    # ══════════════════════════════════════════
    ("Bò né beefsteak VN",               480,  8, 36, 34, "phần", "vietnam"),
    ("Vịt lá lốt",                       360, 10, 28, 22, "phần", "vietnam"),
    ("Gà kho nước mắm đường",            300, 10, 28, 16, "chén", "vietnam"),
    ("Cá chiên nước mắm",                280,  4, 28, 16, "phần", "vietnam"),
    ("Bò hầm rau củ",                    380, 20, 32, 18, "tô",   "vietnam"),
    ("Cà ri vịt",                        460, 24, 30, 26, "tô",   "vietnam"),
    ("Cá rô chiên giòn",                 300,  8, 26, 18, "phần", "vietnam"),
    ("Lẩu cua đồng đặc biệt",            460, 38, 30, 16, "phần", "vietnam"),
    ("Phở Nam Định truyền thống",         430, 57, 27,  9, "tô",   "vietnam"),
    ("Bún cua đồng",                     360, 50, 18,  8, "tô",   "vietnam"),
    ("Bún cà ri gà",                     480, 60, 28, 16, "tô",   "vietnam"),
    ("Hủ tiếu sườn nướng",               420, 56, 24, 12, "tô",   "vietnam"),
    ("Mì thập cẩm đặc biệt",             480, 60, 24, 16, "tô",   "vietnam"),
    ("Bánh canh cá ngừ",                 420, 57, 24, 10, "tô",   "vietnam"),
    ("Gà nướng ngũ vị",                  340,  5, 34, 20, "phần", "vietnam"),
    ("Vịt nấu đậu hũ",                   360, 10, 28, 22, "tô",   "vietnam"),
    ("Bánh mì Sài Gòn đặc biệt",         400, 48, 20, 14, "ổ",    "vietnam"),
    ("Cá ngừ kho dứa",                   280, 14, 26, 12, "chén", "vietnam"),
    ("Thịt heo xào bắp cải",             260, 10, 20, 14, "đĩa",  "vietnam"),
    ("Tôm sú xào mướp",                  240, 10, 22, 10, "đĩa",  "vietnam"),
]
