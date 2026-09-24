from pydantic import BaseModel, Field

class patient(BaseModel):

    patient_id:str
    name:str
    age:int = Field(..., ge=0, le=120)
    gender:str
    blood_group:str
    diagnosis:str
    admitted:bool

class patient_update(BaseModel):
    patient_id: str | None = None
    name: str | None = None
    age: int | None = Field(None, ge=0, le=120)
    gender: str | None = None
    blood_group: str | None = None
    diagnosis: str | None = None
    admitted: bool | None = None