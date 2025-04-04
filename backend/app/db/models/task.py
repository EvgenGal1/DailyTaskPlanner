from .base import Base
from sqlalchemy import Column, UUID, String, Boolean, DateTime, ForeignKey
import uuid

class Task(Base):
    __tablename__ = "tasks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    due_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    user_id = Column(UUID, ForeignKey("users.id"))