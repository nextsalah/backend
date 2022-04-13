from fastapi import APIRouter, HTTPException
from typing import List

from app.utils.utils import VaktijaEU, VaktijaBA, IslamiskaForbundet
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
    
    if not result or not result["success"]:
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
            detail="Could not get locations from VaktijaBA",
        )
    return result

@router.get("/vaktijaba", status_code=200, response_model=PrayerTimeFullYear)
async def vaktijaBA_fetch_prayertimes(location_id: int) -> PrayerTimeFullYear:
    
    result = VaktijaBA.get_prayertimes(location_id)
    
    if not result or not result["success"]:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from VaktijaBA",
        )
    
    return result



@router.get("/islamiska-forbundet/locations", status_code=200, response_model=List[str])
async def islamiska_forbundet_get_locations() -> List[str]:
    result = IslamiskaForbundet.get_locations()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Could not get locations from IslamiskaForbundet",
        )
    return result

@router.get("/islamiska-forbundet", status_code=200, response_model=PrayerTimeFullYear)
async def islamiska_forbundet_fetch_prayertimes(city: str) -> PrayerTimeFullYear:
    
    if city not in IslamiskaForbundet.get_locations():
        raise HTTPException(
            status_code=404,
            detail="City not found",
        )
        
    result = IslamiskaForbundet.get_prayertimes(city)
    
    if not result or not result["success"]:
        raise HTTPException(
            status_code=404,
            detail="Could not fetch data from IslamiskaForbundet",
        )
    
    return result