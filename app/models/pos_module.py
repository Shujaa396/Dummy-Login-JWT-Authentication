from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.config.database import Base

class POSModule(Base):
    __tablename__ = "pos_modules"

    id = Column(Integer, primary_key=True, index=True)
    module_name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
