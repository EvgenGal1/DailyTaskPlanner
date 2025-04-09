from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_access_token, get_password_hash, verify_password
from app.db.models import User
from app.schemas.user import UserCreate, User as UserSchema
from app.core.dependencies import get_async_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserSchema)
async def register(user: UserCreate, db: AsyncSession = Depends(get_async_db)):
    existing_user = await db.execute(select(User).filter(User.email == user.email))
    if existing_user.scalars().first():
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user