from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Reminder
from app.schemas.reminder import ReminderCreate, Reminder
from app.core.dependencies import get_async_db

router = APIRouter(prefix="/reminders", tags=["reminders"])

@router.post("/", response_model=Reminder)
async def create_reminder(reminder: ReminderCreate, db: AsyncSession = Depends(get_async_db)):
    new_reminder = Reminder(**reminder.dict())
    db.add(new_reminder)
    await db.commit()
    await db.refresh(new_reminder)
    return new_reminder