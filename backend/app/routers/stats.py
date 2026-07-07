import csv
import io
from datetime import date, timedelta

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, security

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/week")
def week_stats(
    week_start: str = None,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    """Calo + nước 7 ngày. Truyền week_start=YYYY-MM-DD để xem tuần bất kỳ."""
    if week_start:
        try:
            ref = date.fromisoformat(week_start)
        except ValueError:
            ref = date.today()
    else:
        ref = date.today()
    monday = ref - timedelta(days=ref.weekday())
    days = [monday + timedelta(days=i) for i in range(7)]

    result = []
    for d in days:
        entries = db.query(models.DiaryEntry).filter(
            models.DiaryEntry.user_id == current.id, models.DiaryEntry.log_date == d
        ).all()
        water = db.query(models.WaterLog).filter(
            models.WaterLog.user_id == current.id, models.WaterLog.log_date == d
        ).first()
        result.append({
            "date": d.isoformat(),
            "label": ["T2", "T3", "T4", "T5", "T6", "T7", "CN"][d.weekday()],
            "cal": round(sum(e.cal * e.qty for e in entries), 1),
            "water": water.amount if water else 0,
        })

    active = [r["cal"] for r in result if r["cal"] > 0]
    avg_cal = round(sum(active) / len(active)) if active else 0
    return {"target_cal": current.target_cal, "days": result, "avg_cal": avg_cal}


@router.get("/export")
def export_csv(
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    """Xuất toàn bộ nhật ký ăn uống ra CSV (mở được bằng Excel)."""
    entries = db.query(models.DiaryEntry).filter(
        models.DiaryEntry.user_id == current.id
    ).order_by(models.DiaryEntry.log_date).all()

    buf = io.StringIO()
    buf.write("\ufeff")  # BOM cho Excel đọc đúng tiếng Việt
    writer = csv.writer(buf)
    writer.writerow(["Ngày", "Bữa", "Món", "Số lượng", "Đơn vị", "Kcal", "Carbs(g)", "Protein(g)", "Fat(g)"])

    meal_vi = {"breakfast": "Bữa sáng", "lunch": "Bữa trưa", "dinner": "Bữa tối", "snack": "Ăn vặt"}
    for e in entries:
        writer.writerow([
            e.log_date.isoformat(), meal_vi.get(e.meal, e.meal), e.food_name,
            e.qty, e.unit, round(e.cal * e.qty, 1),
            round(e.carbs * e.qty, 1), round(e.protein * e.qty, 1), round(e.fat * e.qty, 1),
        ])

    buf.seek(0)
    return StreamingResponse(
        iter([buf.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=caloviet_{date.today()}.csv"},
    )
