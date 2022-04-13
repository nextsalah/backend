from fastapi import APIRouter, HTTPException
from typing import List

from app.utils.utils import VaktijaEU, VaktijaBA
from app.schemas.prayertimes import PrayerTimeFullYear, VaktijaEULocations

router = APIRouter()

@router.get("/vaktijaeu/locations", status_code=200, response_model=VaktijaEULocations)
async def vaktijaEU_get_locations() -> VaktijaEULocations:
    result = VaktijaEU.get_locations()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from VaktijaEU",
        )
    return result

@router.get("/vaktijaeu", status_code=200, response_model=PrayerTimeFullYear)
async def vaktijaEU_fetch_prayertimes(location_slug: str) -> PrayerTimeFullYear:
    
    result = VaktijaEU.get_prayertimes(location_slug)
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from VaktijaEU",
        )
    
    return result



@router.get("/vaktijaba/locations", status_code=200, response_model=List[str])
async def vaktijaBA_get_locations() -> List[str]:
    result = VaktijaBA.get_locations()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from VaktijaBA",
        )
    return result

@router.get("/vaktijaba", status_code=200, response_model=PrayerTimeFullYear)
async def vaktijaBA_fetch_prayertimes(location_id: int) -> PrayerTimeFullYear:
    
    result = VaktijaBA.get_prayertimes(location_id)
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from VaktijaBA",
        )
    
    return result

