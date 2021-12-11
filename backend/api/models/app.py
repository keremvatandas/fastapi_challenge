from datetime import datetime

from core.db import Base
from sqlalchemy import Column, DateTime, Integer, String


class App(Base):
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    icon = Column(String(250))
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now())
