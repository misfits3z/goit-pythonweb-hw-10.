from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.future import select

from src.jwt.auth import create_access_token, get_current_user, Hash
from src.database import get_db
from jwt.models import User

router = APIRouter()
hash_handler = Hash()


class UserModel(BaseModel):
    username: str
    password: str


@router.post("/signup")
async def signup(body: UserModel, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.username == body.username)
    result = await db.execute(stmt)
    exist_user = result.scalar_one_or_none()

    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Account already exists"
        )

    new_user = User(
        username=body.username, password=hash_handler.get_password_hash(body.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"new_user": new_user.username}


@router.post("/login")
async def login(
    body: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    stmt = select(User).where(User.username == body.username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username"
        )

    if not hash_handler.verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )

    # Генеруємо JWT
    access_token = await create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/secret")
async def read_secret(current_user: User = Depends(get_current_user)):
    return {"message": "Secret route", "owner": current_user.username}
