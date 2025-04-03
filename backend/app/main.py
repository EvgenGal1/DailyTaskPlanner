from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# настр.CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# нач.путь
@app.get("/")
def root():
    return {"message": "Добро пожаловать в DayTaskPlan!"}