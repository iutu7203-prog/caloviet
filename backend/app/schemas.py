from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


# ---------- Auth ----------
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str = ""


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- Profile ----------
class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    goal: Optional[str] = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    gender: str
    age: int
    height: float
    weight: float
    goal: str
    target_cal: int
    water_goal: int
    is_admin: bool = False

    class Config:
        from_attributes = True


# ---------- Food ----------
class FoodBase(BaseModel):
    name: str
    cal: float
    carbs: float = 0
    protein: float = 0
    fat: float = 0
    unit: str = "phần"
    category: str = "vietnam"


class FoodCreate(FoodBase):
    pass


class FoodOut(FoodBase):
    id: int
    owner_id: Optional[int] = None

    class Config:
        from_attributes = True


# ---------- Diary ----------
class DiaryCreate(BaseModel):
    log_date: Optional[date] = None
    meal: str
    food_name: str
    qty: float = 1
    unit: str = "phần"
    cal: float = 0
    carbs: float = 0
    protein: float = 0
    fat: float = 0


class DiaryOut(BaseModel):
    id: int
    log_date: date
    meal: str
    food_name: str
    qty: float
    unit: str
    cal: float
    carbs: float
    protein: float
    fat: float

    class Config:
        from_attributes = True


# ---------- Water ----------
class WaterUpdate(BaseModel):
    log_date: Optional[date] = None
    amount: int


class WaterOut(BaseModel):
    log_date: date
    amount: int

    class Config:
        from_attributes = True


# ---------- Exercise ----------
class ExerciseCreate(BaseModel):
    log_date: Optional[date] = None
    name: str
    icon: str = "🏃"
    mins: int = 30
    burned: int = 0


class ExerciseOut(BaseModel):
    id: int
    log_date: date
    name: str
    icon: str
    mins: int
    burned: int

    class Config:
        from_attributes = True


# ---------- Day summary ----------
class DaySummary(BaseModel):
    log_date: date
    target_cal: int
    eaten: float
    burned: int
    remaining: float
    carbs: float
    protein: float
    fat: float
    water: int
    water_goal: int
    entries: list[DiaryOut]
    exercises: list[ExerciseOut]


# ---------- Forgot / Reset password ----------
class ForgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    email: EmailStr
    code: str
    new_password: str

class ChangePassword(BaseModel):
    current_password: str
    new_password: str

# ---------- Admin ----------
class AdminUserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    is_admin: bool
    gender: str
    age: int
    height: float
    weight: float
    goal: str
    target_cal: int
    created_at: str = ""

    class Config:
        from_attributes = True

class AdminResetResult(BaseModel):
    new_password: str
