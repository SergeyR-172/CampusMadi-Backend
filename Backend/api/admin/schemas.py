from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    role: str = "default"


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    name: str | None = None
    role: str | None = None


class UserOut(BaseModel):
    id: int
    username: str
    name: str
    role: str

    model_config = ConfigDict(from_attributes=True)