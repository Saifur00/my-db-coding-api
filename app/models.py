from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class StatusEnum(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class SeverityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(Enum(StatusEnum), default="open")
    severity = Column(Enum(SeverityEnum), default="medium")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
