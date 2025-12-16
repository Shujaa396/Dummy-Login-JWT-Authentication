from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from datetime import datetime, date
from typing import Optional

from app.config.database import get_db
from app import models

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)


# -----------------------------
# POST /report/seed
# -----------------------------
@router.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter_by(username="testuser").first()
    if existing_user:
        return {"message": "Seed data already exists"}

    # User + Profile
    user = models.User(username="testuser", email="test@example.com", password="hashedpassword")
    profile = models.Profile(full_name="Syed Shujaa Hussain", role="Admin", user=user)

    # Products
    product1 = models.Product(name="Panadol", category="Pharmacy", price=50.0)
    product2 = models.Product(name="Milk Pack", category="Grocery", price=120.0)
    product3 = models.Product(name="Shampoo", category="Grocery", price=250.0)

    # Invoices
    invoice1 = models.Invoice(invoice_number="INV-001", total=220.0, sync_status="success", user=user)
    invoice2 = models.Invoice(invoice_number="INV-002", total=370.0, sync_status="failed", user=user)

    # Invoice Items
    item1 = models.InvoiceItem(invoice=invoice1, product=product1, quantity=2, price=50.0)
    item2 = models.InvoiceItem(invoice=invoice1, product=product2, quantity=1, price=120.0)
    item3 = models.InvoiceItem(invoice=invoice2, product=product2, quantity=2, price=120.0)
    item4 = models.InvoiceItem(invoice=invoice2, product=product3, quantity=1, price=250.0)

    db.add(user)
    db.add(profile)
    db.add_all([product1, product2, product3])
    db.add_all([invoice1, invoice2])
    db.add_all([item1, item2, item3, item4])
    db.commit()

    return {"message": "Seed data inserted successfully"}
