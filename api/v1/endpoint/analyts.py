from typing import List

from fastapi import APIRouter,status,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.Data_analyts_model import leagueModel,countryModel,teamModel,playerModel,competitionsModel,continenteModel,player_continenteModel
from schemas.Data_analyts_schemas import  league,country,player,team,continente, player_continente
from core.deps import get_session


router = APIRouter()

@router.get('/')
async def get_test():
    return "123123131"