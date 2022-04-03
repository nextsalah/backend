from fastapi import APIRouter

from app.api.api_v1.endpoints import prayertimes


api_router = APIRouter()
api_router.include_router(prayertimes.router, prefix="/prayertimes", tags=["Prayertimes"])