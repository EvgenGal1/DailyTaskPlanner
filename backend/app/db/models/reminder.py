from .base import Base
from sqlalchemy import Column, UUID, String, DateTime, ForeignKey, Boolean
from datetime import datetime

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID, ForeignKey("tasks.id"))
    user_id = Column(UUID, ForeignKey("users.id"))
    remind_at = Column(DateTime, nullable=False)
    is_sent = Column(Boolean, default=False)