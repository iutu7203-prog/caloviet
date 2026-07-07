from fastapi import APIRouter, Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, security

router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("", response_model=list[schemas.FoodOut])
def list_foods(
    q: str = "",
    limit: int = 50,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    """Trả về món hệ thống + món riêng của user. Có thể tìm theo tên."""
    query = db.query(models.Food).filter(
        or_(models.Food.owner_id.is_(None), models.Food.owner_id == current.id)
    )
    if q:
        query = query.filter(models.Food.name.ilike(f"%{q}%"))
    return query.order_by(models.Food.owner_id.isnot(None).desc()).limit(limit).all()


@router.post("", response_model=schemas.FoodOut)
def create_food(
    data: schemas.FoodCreate,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    """Tạo món tự định nghĩa (giải quyết feedback 'thiếu món ăn')."""
    food = models.Food(**data.model_dump(), owner_id=current.id)
    db.add(food)
    db.commit()
    db.refresh(food)
    return food


@router.delete("/{food_id}")
def delete_food(
    food_id: int,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    food = db.query(models.Food).filter(
        models.Food.id == food_id, models.Food.owner_id == current.id
    ).first()
    if food:
        db.delete(food)
        db.commit()
    return {"ok": True}
