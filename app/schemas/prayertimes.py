from typing import Optional
from pydantic import BaseModel


class VaktijaEU(BaseModel):
    date: Optional[str]
    surname: Optional[str]
    is_superuser: bool = False