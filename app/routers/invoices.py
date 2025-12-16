from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.invoice import Invoice, InvoiceSyncLog
from app.schemas.invoices import (
    InvoiceCreate,
    InvoiceResponse,
    InvoiceWithLogs,
    InvoiceSyncLogCreate,
    InvoiceSyncLogResponse,
)

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

# Create invoice
@router.post("/", response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# Get all invoices
@router.get("/", response_model=List[InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()

# Get invoice by ID with logs
@router.get("/{invoice_id}", response_model=InvoiceWithLogs)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

# Create sync log
@router.post("/logs/", response_model=InvoiceSyncLogResponse)
def create_sync_log(log: InvoiceSyncLogCreate, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == log.invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    new_log = InvoiceSyncLog(**log.dict())
    db.add(new_log)
    invoice.sync_status = log.status  # update invoice status
    db.commit()
    db.refresh(new_log)
    return new_log

# Get logs for invoice
@router.get("/{invoice_id}/logs", response_model=List[InvoiceSyncLogResponse])
def get_invoice_logs(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db.query(InvoiceSyncLog).filter(InvoiceSyncLog.invoice_id == invoice_id).all()
