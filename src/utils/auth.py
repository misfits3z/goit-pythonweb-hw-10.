# from datetime import datetime, timedelta, UTC
# from typing import Optional
# from fastapi import Depends, HTTPException, status
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from jose import JWTError, jwt

# from jwt.models import User  # Імпортуємо модель User
# from src.database import get_db  # Асинхронна сесія

# SECRET_KEY = "secret_key"
# ALGORITHM = "HS256"


# class Hash:
#     pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#     def verify_password(self, plain_password, hashed_password):
#         return self.pwd_context.verify(plain_password, hashed_password)

#     def get_password_hash(self, password: str):
#         return self.pwd_context.hash(password)


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# # новий токен
# async def create_access_token(data: dict, expires_delta: Optional[float] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(UTC) + timedelta(seconds=expires_delta)
#     else:
#         expire = datetime.now(UTC) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(
#     token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     stmt = select(User).where(User.username == username)  # Асинхронний SELECT
#     result = await db.execute(stmt)
#     user = result.scalar_one_or_none()  # Асинхронне отримання результату

#     if user is None:
#         raise credentials_exception
#     return user
