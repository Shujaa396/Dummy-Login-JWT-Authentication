from pydantic import BaseModel
from datetime import date

class SubscriptionBase(BaseModel):
    user_id: int
    plan: str
    start_date: date
    end_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int

    class Config:
        from_attributes = True
