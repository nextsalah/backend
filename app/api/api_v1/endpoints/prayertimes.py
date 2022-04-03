from fastapi import APIRouter, HTTPException
from typing import Any

from app.schemas.prayertimes import VaktijaEU


router = APIRouter()


@router.get("/vaktijaeu", status_code=200, response_model=VaktijaEU)
def fetch_vaktijaEU(data: VaktijaEU) -> Any:
    """
    Fetch a prayertimes from VaktijaEU.
    """
    result = "crud.prayertimes.get_vaktijaEU()"
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Could not fetch VaktijaEU "
        )

    return result

