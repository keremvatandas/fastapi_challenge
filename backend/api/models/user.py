from datetime import datetime

from core.db import Base
from sqlalchemy import Column, DateTime, Integer, String


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now())
