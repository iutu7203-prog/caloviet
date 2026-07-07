import random
import string
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, security

router = APIRouter(prefix="/admin", tags=["admin"])


def require_admin(
    current: models.User = Depends(security.get_current_user),
):
    if not current.is_admin:
        raise HTTPException(status_code=403, detail="Chỉ admin mới có quyền truy cập")
    return current


@router.get("/users")
def list_users(
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    users = db.query(models.User).order_by(models.User.created_at).all()
    return [
        {
            "id": u.id,
            "email": u.email,
            "name": u.name,
            "is_admin": u.is_admin,
            "gender": u.gender,
            "age": u.age,
            "height": u.height,
            "weight": u.weight,
            "goal": u.goal,
            "target_cal": u.target_cal,
            "created_at": u.created_at.strftime("%d/%m/%Y") if u.created_at else "",
        }
        for u in users
    ]


@router.get("/stats")
def admin_stats(
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    total_users = db.query(models.User).count()
    total_entries = db.query(models.DiaryEntry).count() if hasattr(models, "DiaryEntry") else 0
    return {
        "total_users": total_users,
        "total_diary_entries": db.query(models.DiaryEntry).count(),
        "total_foods": db.query(models.Food).count(),
    }


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current: models.User = Depends(require_admin),
):
    if user_id == current.id:
        raise HTTPException(status_code=400, detail="Không thể tự xóa tài khoản admin")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    db.delete(user)
    db.commit()
    return {"ok": True, "message": f"Đã xóa tài khoản {user.email}"}


@router.post("/users/{user_id}/reset-password")
def admin_reset_password(
    user_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")

    new_pw = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    user.hashed_password = security.hash_password(new_pw)
    user.reset_code = None
    user.reset_code_expires = None
    db.commit()
    return {"new_password": new_pw}


@router.put("/users/{user_id}/toggle-admin")
def toggle_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current: models.User = Depends(require_admin),
):
    if user_id == current.id:
        raise HTTPException(status_code=400, detail="Không thể thay đổi quyền của chính mình")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    user.is_admin = not user.is_admin
    db.commit()
    return {"ok": True, "is_admin": user.is_admin}
