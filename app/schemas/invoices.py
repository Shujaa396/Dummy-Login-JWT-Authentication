from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Invoice Schemas
class InvoiceBase(BaseModel):
    invoice_number: str
    total: float
    sync_status: Optional[str] = "pending"

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True

# Invoice Sync Log Schemas
class InvoiceSyncLogBase(BaseModel):
    status: str
    message: Optional[str] = None

class InvoiceSyncLogCreate(InvoiceSyncLogBase):
    invoice_id: int

class InvoiceSyncLogResponse(InvoiceSyncLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Invoice with logs
class InvoiceWithLogs(InvoiceResponse):
    sync_logs: List[InvoiceSyncLogResponse] = []
