import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine, SessionLocal
from . import models
from .seed_foods import seed_foods
from .routers import auth, foods, diary, stats, admin

# Tạo bảng (production lớn nên dùng Alembic, demo dùng create_all)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CaloViet API", version="1.0.0")

origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(foods.router)
app.include_router(diary.router)
app.include_router(stats.router)
app.include_router(admin.router)


@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    try:
        seed_foods(db, models)
    finally:
        db.close()


@app.get("/")
def root():
    return {"app": "CaloViet API", "status": "ok", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "healthy"}
