from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from app.config.database import Base

class LoginLog(Base):
    __tablename__ = "login_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ip_address = Column(String, nullable=True)
    status = Column(String, nullable=False)   # ✅ success or failure
    timestamp = Column(DateTime(timezone=True), server_default=func.now())  # ✅ matches auth.py
