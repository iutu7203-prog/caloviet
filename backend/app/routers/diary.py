from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, security

router = APIRouter(prefix="/diary", tags=["diary"])


def _parse_date(d):
    return d or date.today()


# ---------- Bữa ăn ----------
@router.post("/entries", response_model=schemas.DiaryOut)
def add_entry(
    data: schemas.DiaryCreate,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    entry = models.DiaryEntry(
        user_id=current.id,
        log_date=_parse_date(data.log_date),
        meal=data.meal,
        food_name=data.food_name,
        qty=data.qty,
        unit=data.unit,
        cal=data.cal,
        carbs=data.carbs,
        protein=data.protein,
        fat=data.fat,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/entries/{entry_id}")
def delete_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    entry = db.query(models.DiaryEntry).filter(
        models.DiaryEntry.id == entry_id,
        models.DiaryEntry.user_id == current.id,
    ).first()
    if entry:
        db.delete(entry)
        db.commit()
    return {"ok": True}


# ---------- Nước ----------
@router.put("/water", response_model=schemas.WaterOut)
def set_water(
    data: schemas.WaterUpdate,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    d = _parse_date(data.log_date)
    log = db.query(models.WaterLog).filter(
        models.WaterLog.user_id == current.id, models.WaterLog.log_date == d
    ).first()
    if not log:
        log = models.WaterLog(user_id=current.id, log_date=d, amount=0)
        db.add(log)
    log.amount = max(0, data.amount)
    db.commit()
    db.refresh(log)
    return log


# ---------- Tập luyện ----------
@router.post("/exercises", response_model=schemas.ExerciseOut)
def add_exercise(
    data: schemas.ExerciseCreate,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    ex = models.ExerciseLog(
        user_id=current.id,
        log_date=_parse_date(data.log_date),
        name=data.name,
        icon=data.icon,
        mins=data.mins,
        burned=data.burned,
    )
    db.add(ex)
    db.commit()
    db.refresh(ex)
    return ex


@router.delete("/exercises/{ex_id}")
def delete_exercise(
    ex_id: int,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    ex = db.query(models.ExerciseLog).filter(
        models.ExerciseLog.id == ex_id, models.ExerciseLog.user_id == current.id
    ).first()
    if ex:
        db.delete(ex)
        db.commit()
    return {"ok": True}


# ---------- Tổng hợp 1 ngày ----------
@router.get("/day", response_model=schemas.DaySummary)
def day_summary(
    log_date: date | None = None,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    d = _parse_date(log_date)
    entries = db.query(models.DiaryEntry).filter(
        models.DiaryEntry.user_id == current.id, models.DiaryEntry.log_date == d
    ).all()
    exercises = db.query(models.ExerciseLog).filter(
        models.ExerciseLog.user_id == current.id, models.ExerciseLog.log_date == d
    ).all()
    water = db.query(models.WaterLog).filter(
        models.WaterLog.user_id == current.id, models.WaterLog.log_date == d
    ).first()

    eaten = sum(e.cal * e.qty for e in entries)
    carbs = sum(e.carbs * e.qty for e in entries)
    protein = sum(e.protein * e.qty for e in entries)
    fat = sum(e.fat * e.qty for e in entries)
    burned = sum(e.burned for e in exercises)

    return schemas.DaySummary(
        log_date=d,
        target_cal=current.target_cal,
        eaten=round(eaten, 1),
        burned=burned,
        remaining=round(max(0, current.target_cal - eaten + burned), 1),
        carbs=round(carbs, 1),
        protein=round(protein, 1),
        fat=round(fat, 1),
        water=water.amount if water else 0,
        water_goal=current.water_goal,
        entries=entries,
        exercises=exercises,
    )
