

from fastapi import APIRouter
from api.v1.endpoint import analyts,league,player,team,competitions,continente,country

api_router = APIRouter()
api_router.include_router(analyts.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(league.router, prefix="/league", tags=["League"])
api_router.include_router(team.router,prefix='/team', tags=["Team"])
api_router.include_router(competitions.router,prefix='/competitions', tags=["Competitions"])
api_router.include_router(continente.router,prefix='/continente', tags=["Continente"])
api_router.include_router(country.router,prefix='/country', tags=["Country"])

