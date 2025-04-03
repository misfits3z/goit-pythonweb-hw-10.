from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date, Text, DateTime, func

class Base(DeclarativeBase):
    pass


class Contact(Base):

    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)  
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)  
    email: Mapped[str] = mapped_column(String(255), unique=True) 
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)  
    birth_date: Mapped[Date] = mapped_column(Date, nullable=False)
    note: Mapped[str] =  mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column("created_at", DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column("updated_at", DateTime, default=func.now(), onupdate=func.now())


