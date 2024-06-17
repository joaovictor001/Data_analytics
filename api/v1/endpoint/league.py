from typing import List

from fastapi import APIRouter,status,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.Data_analyts_model import leagueModel,countryModel,teamModel,playerModel,competitionsModel,continenteModel,player_continenteModel
from schemas.Data_analyts_schemas import  leagueSchemam,countrySchemam,playerSchemam,teamSchemam,continenteSchemam, player_continenteSchemam
from core.deps import get_session



router = APIRouter()

@router.post('/')
async def post_league(dados: leagueSchemam, db: AsyncSession = Depends(get_session)):

    new_league = leagueModel (league_name = dados.league_name)
    db.add(new_league)
    await db.commit()

    return new_league