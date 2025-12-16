from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app import models, schemas

router = APIRouter(prefix="/pos_modules", tags=["POS Modules"])

@router.post("/", response_model=schemas.PosModule)
def create_pos_module(pos_module: schemas.PosModuleCreate, db: Session = Depends(get_db)):
    db_module = models.PosModule(**pos_module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module

@router.get("/", response_model=list[schemas.PosModule])
def get_pos_modules(db: Session = Depends(get_db)):
    return db.query(models.PosModule).all()
