from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReminderBase(BaseModel):
    task_id: str
    remind_at: datetime

class ReminderCreate(ReminderBase):
    pass

class Reminder(ReminderBase):
    id: str
    is_sent: bool

    class Config:
        orm_mode = True