from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# настр.CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# нач.путь
@app.get("/")
def root():
    return {"message": "Добро пожаловать в DayTaskPlan!"}