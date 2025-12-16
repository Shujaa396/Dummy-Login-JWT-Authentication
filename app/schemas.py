from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ---------------- AUTH ----------------
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    login_time: str

class UserCreate(BaseModel):
    username: str
    password: str
    is_fbr_enabled: bool = False

class UserLogin(BaseModel):
    username: str
    password: str

# ---------------- INVOICE HISTORY ----------------
class InvoiceOut(BaseModel):
    invoice_id: int = Field(..., alias="id")
    invoice_number: str
    date: str = Field(..., alias="invoice_date")
    total: float
    sync_status: str

class PaginatedInvoices(BaseModel):
    page: int
    limit: int
    total_records: int
    total_pages: int
    invoices: List[InvoiceOut]

# ---------------- REPORTS ----------------
class SalesReportRequest(BaseModel):
    date_from: Optional[str] = None  # "YYYY-MM-DD"
    date_to: Optional[str] = None
    category: Optional[str] = None
    top_n: int = 5

class TopProduct(BaseModel):
    name: str
    qty: int
    sales: float

class SalesReportResponse(BaseModel):
    total_sales: float
    total_invoices: int
    top_products: List[TopProduct]

# ---------------- INVOICE + SYNC LOG ----------------
class InvoiceBase(BaseModel):
    invoice_number: str
    total: float

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceSyncLogBase(BaseModel):
    status: str   # success/failed
    message: Optional[str] = None

class InvoiceSyncLogResponse(InvoiceSyncLogBase):
    id: int
    invoice_id: int
    timestamp: datetime

    class Config:
        from_attributes = True   # ✅ updated for Pydantic v2

class InvoiceResponse(InvoiceBase):
    id: int
    date: datetime
    sync_status: str
    sync_logs: List[InvoiceSyncLogResponse] = []

    class Config:
        from_attributes = True   # ✅ updated for Pydantic v2
