from pydantic import BaseModel
from datetime import datetime

class LoginLogBase(BaseModel):
    user_id: int
    login_time: datetime

class LoginLogCreate(LoginLogBase):
    pass

class LoginLog(LoginLogBase):
    id: int

    class Config:
        from_attributes = True
