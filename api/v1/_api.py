

from fastapi import APIRouter
from api.v1.endpoint import analyts,league

api_router = APIRouter()
api_router.include_router(analyts.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(league.router, prefix="/league", tags=["League"])