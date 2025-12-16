from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models import Profile
from app.schemas.profile import ProfileCreate, ProfileResponse
from app.routers.auth import get_current_user

router = APIRouter(
    prefix="/profiles",
    tags=["profiles"]
)

@router.post("/", response_model=ProfileResponse)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    new_profile = Profile(
        first_name=profile.first_name,
        last_name=profile.last_name,
        phone=profile.phone,
        user_id=current_user["id"]
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.get("/me", response_model=ProfileResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    profile = db.query(Profile).filter(Profile.user_id == current_user["id"]).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
