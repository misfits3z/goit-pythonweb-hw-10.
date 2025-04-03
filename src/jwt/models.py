from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from src.database.models import Base


# Модель Користувачів
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
