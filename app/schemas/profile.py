from pydantic import BaseModel

class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    phone: str

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileResponse(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
