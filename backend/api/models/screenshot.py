from datetime import datetime

from core.db import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.schema import ForeignKey


class Screenshot(Base):
    __tablename__ = "screenshot"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(250))
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now())
    app_id = Column(Integer, ForeignKey("app.id"))
