from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    total = Column(Float)
    sync_status = Column(String, default="pending")  # pending/success/failed
    date = Column(DateTime, server_default=func.now())

    sync_logs = relationship("InvoiceSyncLog", back_populates="invoice")


class InvoiceSyncLog(Base):
    __tablename__ = "invoice_sync_logs"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    status = Column(String)  # success/failed
    message = Column(String, nullable=True)
    timestamp = Column(DateTime, server_default=func.now())

    invoice = relationship("Invoice", back_populates="sync_logs")
