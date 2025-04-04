from sqlalchemy.ext.asyncio import AsyncSession
from libgravatar import Gravatar

from src.repository.users import UserRepository
from src.schemas import UserCreate

import smtplib
from email.mime.text import MIMEText
from src.conf.config import config


class UserService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def create_user(self, body: UserCreate):
        avatar = None
        try:
            g = Gravatar(body.email)
            avatar = g.get_image()
        except Exception as e:
            print(e)

        return await self.repository.create_user(body, avatar)

    async def get_user_by_id(self, user_id: int):
        return await self.repository.get_user_by_id(user_id)

    async def get_user_by_username(self, username: str):
        return await self.repository.get_user_by_username(username)

    async def get_user_by_email(self, email: str):
        return await self.repository.get_user_by_email(email)
    
    async def send_verification_email(email: str, token: str):
        verify_link = f"http://localhost:8000/api/auth/verify-email?token={token}"
        msg = MIMEText(f"Click to verify your email: {verify_link}")
        msg["Subject"] = "Email Verification"
        msg["From"] = config.SMTP_USERNAME
        msg["To"] = email

        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            server.sendmail(config.SMTP_USERNAME, email, msg.as_string())
