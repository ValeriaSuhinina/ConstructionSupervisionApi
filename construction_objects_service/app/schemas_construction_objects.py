from pydantic import BaseModel, ConfigDict


class SConstructionObjectAdd(BaseModel):
    address: str
    type: str | None = None


class SConstructionObject(SConstructionObjectAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SConstructionObjectId(BaseModel):
    id: int
