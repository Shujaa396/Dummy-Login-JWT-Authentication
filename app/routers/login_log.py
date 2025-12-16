from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.login_log import LoginLog
from app.schemas.login_log import LoginLogCreate, LoginLogResponse

router = APIRouter(prefix="/login_logs", tags=["Login Logs"])

@router.post("/", response_model=LoginLogResponse)
def create_login_log(login_log: LoginLogCreate, db: Session = Depends(get_db)):
    db_log = LoginLog(**login_log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

@router.get("/", response_model=list[LoginLogResponse])
def get_login_logs(db: Session = Depends(get_db)):
    return db.query(LoginLog).all()
