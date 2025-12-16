from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.config.database import get_db
from app import models
from datetime import datetime, date
from typing import Optional, List

router = APIRouter(prefix="/reports", tags=["Reports"])


# ✅ Seed data (your existing code)
@router.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    db.query(models.InvoiceItem).delete()
    db.query(models.Invoice).delete()
    db.query(models.Product).delete()
    db.query(models.Profile).delete()
    db.query(models.User).delete()
    db.commit()

    user = models.User(
        username="syed",
        email="syed@example.com",
        hashed_password="1234"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    profile = models.Profile(full_name="Syed Shujaa Hussain", role="Admin", user_id=user.id)
    db.add(profile)

    product1 = models.Product(name="Panadol", category="Pharmacy", price=50.0)
    product2 = models.Product(name="Cola", category="Grocery", price=120.0)
    db.add_all([product1, product2])
    db.commit()
    db.refresh(product1)
    db.refresh(product2)

    invoice = models.Invoice(
        invoice_number="INV-001",
        total=170.0,
        sync_status="success",
        date=datetime(2025, 8, 10),
        user_id=user.id
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    item1 = models.InvoiceItem(invoice_id=invoice.id, product_id=product1.id, quantity=1, price=50.0)
    item2 = models.InvoiceItem(invoice_id=invoice.id, product_id=product2.id, quantity=1, price=120.0)
    db.add_all([item1, item2])
    db.commit()

    return {"message": "Seed data inserted successfully"}


# ✅ 1. Invoice History API
@router.get("/invoice/history")
def get_invoice_history(
    db: Session = Depends(get_db),
    status: Optional[str] = Query(None, description="Filter by sync_status"),
    start_date: Optional[date] = Query(None, description="Filter start date"),
    end_date: Optional[date] = Query(None, description="Filter end date"),
    page: int = 1,
    limit: int = 10
):
    query = db.query(models.Invoice)

    if status:
        query = query.filter(models.Invoice.sync_status == status)

    if start_date:
        query = query.filter(models.Invoice.date >= start_date)

    if end_date:
        query = query.filter(models.Invoice.date <= end_date)

    total_records = query.count()
    invoices = query.order_by(models.Invoice.date.desc()) \
                    .offset((page - 1) * limit) \
                    .limit(limit) \
                    .all()

    result = [
        {
            "invoice_id": inv.id,
            "invoice_number": inv.invoice_number,
            "date": inv.date,
            "total": inv.total,
            "sync_status": inv.sync_status,
        }
        for inv in invoices
    ]

    return {
        "page": page,
        "limit": limit,
        "total_records": total_records,
        "data": result
    }


# ✅ 2. Sales Report API
@router.post("/sales")
def get_sales_report(
    db: Session = Depends(get_db),
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    category: Optional[str] = None
):
    query = db.query(models.InvoiceItem, models.Product).join(models.Product)

    if start_date:
        query = query.join(models.Invoice).filter(models.Invoice.date >= start_date)
    if end_date:
        query = query.join(models.Invoice).filter(models.Invoice.date <= end_date)
    if category:
        query = query.filter(models.Product.category == category)

    items = query.all()

    total_sales = sum(item.InvoiceItem.price * item.InvoiceItem.quantity for item in items)

    product_sales = {}
    for item, product in items:
        product_sales[product.name] = product_sales.get(product.name, 0) + (item.price * item.quantity)

    top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_sales": total_sales,
        "top_products": top_products
    }
