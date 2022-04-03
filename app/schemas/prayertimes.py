from typing import Optional
from pydantic import BaseModel, EmailStr


class VaktijaEU(BaseModel):
    date: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr] = None
    is_superuser: bool = False