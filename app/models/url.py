from sqlalchemy import DateTime, Integer, String, Column
from sqlalchemy.sql import func
from app.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url: str = Column(String, index=True)
    short_code: str =  Column(String, index=True, unique=True, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())