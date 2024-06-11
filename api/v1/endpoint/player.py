from typing import List

from fastapi import APIRouter,status,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.Data_analyts_model import leagueModel,countryModel,teamModel,playerModel,competitionsModel,continenteModel,player_continenteModel
from schemas.Data_analyts_schemas import  leagueSchemam,countrySchemam,playerSchemam,teamSchemam,continenteSchemam, player_continenteSchemam
from core.deps import get_session



router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED,response_model=playerSchemam)
async def post_player(player: playerSchemam, db: AsyncSession = Depends(get_session)):
    new_player = playerModel(player_name = player.player_name,
                                                    player_number = player.player_number,
                                                    player_type = player.player_type,
                                                    )