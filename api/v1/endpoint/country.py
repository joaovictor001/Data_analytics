from typing import List

from fastapi import APIRouter,status,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.Data_analyts_model import leagueModel,countryModel,teamModel,playerModel,competitionsModel,continenteModel,player_continenteModel
from schemas.Data_analyts_schemas import  leagueSchemam,countrySchemam,playerSchemam,teamSchemam,continenteSchemam, player_continenteSchemam
from core.deps import get_session


router = APIRouter()

@router.post('/')
async def post_country(dados: countrySchemam, db: AsyncSession = Depends(get_session)):

    new_country  = countryModel(country_name = dados.country_name,
                                                            league_id = dados.league_id,
                                                            )
    db.add(new_country)
    await db.commit()
    return new_country


@router.get('/')
async def get_country(db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(countryModel)
        result = await session.execute(query)
        countrys: List[countryModel] = result.scalars().all()

        return countrys