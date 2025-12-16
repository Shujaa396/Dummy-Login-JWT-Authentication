from pydantic import BaseModel

class POSModuleBase(BaseModel):
    name: str
    description: str | None = None

class POSModuleCreate(POSModuleBase):
    pass

class POSModule(POSModuleBase):
    id: int

    class Config:
        from_attributes = True
