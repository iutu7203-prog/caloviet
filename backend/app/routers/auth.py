import random
import string
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, security
from ..email_service import (
    is_email_configured, send_email_async,
    build_reset_email, build_welcome_email,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=schemas.Token)
def register(data: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email đã được đăng ký")

    is_first = db.query(models.User).count() == 0
    target, water = security.calc_targets("female", 25, 165, 60, "lose")
    user = models.User(
        email=data.email,
        hashed_password=security.hash_password(data.password),
        name=data.name,
        target_cal=target,
        water_goal=water,
        is_admin=is_first,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Gửi email chào mừng (nếu đã cấu hình SMTP)
    if is_email_configured():
        send_email_async(
            to_email=data.email,
            subject=f"Chào mừng đến với CaloViet! 🥗",
            html_body=build_welcome_email(data.name, data.email),
        )

    return schemas.Token(access_token=security.create_access_token(user.id))


@router.post("/login", response_model=schemas.Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form.username).first()
    if not user or not security.verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Email hoặc mật khẩu không đúng")
    return schemas.Token(access_token=security.create_access_token(user.id))


@router.get("/me", response_model=schemas.UserOut)
def me(current: models.User = Depends(security.get_current_user)):
    return current


@router.put("/me", response_model=schemas.UserOut)
def update_me(
    data: schemas.ProfileUpdate,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(current, field, value)
    current.target_cal, current.water_goal = security.calc_targets(
        current.gender, current.age, current.height, current.weight, current.goal
    )
    db.commit()
    db.refresh(current)
    return current


@router.put("/change-password")
def change_password(
    data: schemas.ChangePassword,
    db: Session = Depends(get_db),
    current: models.User = Depends(security.get_current_user),
):
    if not security.verify_password(data.current_password, current.hashed_password):
        raise HTTPException(status_code=400, detail="Mật khẩu hiện tại không đúng")
    current.hashed_password = security.hash_password(data.new_password)
    db.commit()
    return {"ok": True, "message": "Đổi mật khẩu thành công"}


@router.post("/forgot-password")
def forgot_password(data: schemas.ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        return {"message": "Nếu email tồn tại, mã xác nhận đã được gửi."}

    code = "".join(random.choices(string.digits, k=6))
    user.reset_code = security.hash_password(code)
    user.reset_code_expires = datetime.utcnow() + timedelta(minutes=15)
    db.commit()

    if is_email_configured():
        # ✅ Production: gửi email thật
        send_email_async(
            to_email=user.email,
            subject="Mã xác nhận đặt lại mật khẩu CaloViet",
            html_body=build_reset_email(user.name, code),
        )
        return {
            "message": f"Mã xác nhận đã gửi đến {user.email}. Kiểm tra hộp thư (kể cả Spam).",
            "expires_in": "15 phút",
        }
    else:
        # ⚠️ Dev mode: trả code trực tiếp
        return {
            "message": "⚠️ Dev mode: SMTP chưa cấu hình. Mã hiển thị trực tiếp.",
            "code": code,
            "expires_in": "15 phút",
            "dev_note": "Thêm SMTP_EMAIL và SMTP_PASSWORD vào .env để gửi email thật",
        }


@router.post("/reset-password")
def reset_password(data: schemas.ResetPassword, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not user.reset_code or not user.reset_code_expires:
        raise HTTPException(status_code=400, detail="Yêu cầu không hợp lệ. Vui lòng thử lại.")

    if datetime.utcnow() > user.reset_code_expires:
        raise HTTPException(status_code=400, detail="Mã xác nhận đã hết hạn. Vui lòng yêu cầu lại.")

    if not security.verify_password(data.code, user.reset_code):
        raise HTTPException(status_code=400, detail="Mã xác nhận không đúng")

    if len(data.new_password) < 6:
        raise HTTPException(status_code=400, detail="Mật khẩu mới phải có ít nhất 6 ký tự")

    user.hashed_password = security.hash_password(data.new_password)
    user.reset_code = None
    user.reset_code_expires = None
    db.commit()
    return {"ok": True, "message": "Đặt lại mật khẩu thành công! Hãy đăng nhập lại."}
