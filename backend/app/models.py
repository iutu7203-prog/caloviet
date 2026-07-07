from datetime import date, datetime

from sqlalchemy import (
    Column, Integer, String, Float, Date, DateTime, ForeignKey, Boolean
)
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, default="")
    gender = Column(String, default="female")     # male / female
    age = Column(Integer, default=25)
    height = Column(Float, default=165)            # cm
    weight = Column(Float, default=60)             # kg
    goal = Column(String, default="lose")          # lose / maintain / gain
    target_cal = Column(Integer, default=1800)
    water_goal = Column(Integer, default=2000)     # ml
    is_admin = Column(Boolean, default=False)
    reset_code = Column(String, nullable=True)
    reset_code_expires = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    entries = relationship("DiaryEntry", back_populates="user", cascade="all, delete-orphan")
    water_logs = relationship("WaterLog", back_populates="user", cascade="all, delete-orphan")
    exercise_logs = relationship("ExerciseLog", back_populates="user", cascade="all, delete-orphan")
    custom_foods = relationship("Food", back_populates="owner", cascade="all, delete-orphan")


class Food(Base):
    """Thư viện món ăn. owner_id = NULL nghĩa là món hệ thống (ai cũng thấy)."""
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    cal = Column(Float, nullable=False)
    carbs = Column(Float, default=0)
    protein = Column(Float, default=0)
    fat = Column(Float, default=0)
    unit = Column(String, default="phần")
    category = Column(String, default="vietnam")   # vietnam / basic / drink / supplement / fastfood
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", back_populates="custom_foods")


class DiaryEntry(Base):
    """Một món đã ăn, gắn với ngày + bữa."""
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    log_date = Column(Date, default=date.today, index=True)
    meal = Column(String, nullable=False)          # breakfast / lunch / dinner / snack
    food_name = Column(String, nullable=False)
    qty = Column(Float, default=1)
    unit = Column(String, default="phần")
    cal = Column(Float, default=0)                 # giá trị / 1 đơn vị
    carbs = Column(Float, default=0)
    protein = Column(Float, default=0)
    fat = Column(Float, default=0)
    is_admin = Column(Boolean, default=False)
    reset_code = Column(String, nullable=True)
    reset_code_expires = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="entries")


class WaterLog(Base):
    __tablename__ = "water_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    log_date = Column(Date, default=date.today, index=True)
    amount = Column(Integer, default=0)            # ml tổng trong ngày

    user = relationship("User", back_populates="water_logs")


class ExerciseLog(Base):
    __tablename__ = "exercise_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    log_date = Column(Date, default=date.today, index=True)
    name = Column(String, nullable=False)
    icon = Column(String, default="🏃")
    mins = Column(Integer, default=30)
    burned = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)
    reset_code = Column(String, nullable=True)
    reset_code_expires = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="exercise_logs")
