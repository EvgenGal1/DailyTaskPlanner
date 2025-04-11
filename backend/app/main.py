from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# настр.CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLT_URL], # URL front
    allow_credentials=True,
    allow_methods=["*"], # все мтд.
    allow_headers=["*"], # все заголовки 
)

# нач.путь
@app.get("/")
def root():
    return {"message": "Добро пожаловать в DayTaskPlan!"}