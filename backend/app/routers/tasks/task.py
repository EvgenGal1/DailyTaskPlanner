from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.core.dependencies import get_async_db
from sqlalchemy import select

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_async_db)):
    new_task = Task(**task.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

@router.get("/", response_model=list[TaskResponse])
async def read_tasks(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    tasks = result.scalars().all()
    return tasks