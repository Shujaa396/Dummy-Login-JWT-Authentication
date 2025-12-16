from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app import models, schemas

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = models.Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.get("/", response_model=list[schemas.Subscription])
def get_subscriptions(db: Session = Depends(get_db)):
    return db.query(models.Subscription).all()
