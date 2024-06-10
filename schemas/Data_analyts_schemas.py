from typing import Optional

from pydantic import BaseModel as SchemasBaseModel


class league(SchemasBaseModel):
    league_id:Optional[int]= None
    league_name:str


    class Config:
        from_atributes = True

class country(SchemasBaseModel):
    country_id:Optional[int]= None
    country_name:str
    league_id:int
    league: league

    class Config:
        from_atributes = True

class player(SchemasBaseModel):
    player_id: Optional[int]= None 
    player_name:str 
    player_number: int
    player_type: str
    class Config:
        from_atributes = True

class team(SchemasBaseModel):
    team_id:Optional[int]=None
    team_name: str
    country_id:int
    league_id: int

    country:country
    league:league
    class Config:
        from_atributes = True

class continente(SchemasBaseModel):
    continente_id:Optional[int] = None
    continente_name:str
    class Config:
        from_atributes = True

class player_continente(SchemasBaseModel):
    player_id:int
    continente_id: int

    player:player
    continente:continente
    class Config:
        from_atributes = True 