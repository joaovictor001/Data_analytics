from typing import Optional

from pydantic import BaseModel as SchemasBaseModel


class leagueSchemam(SchemasBaseModel):
    league_id:Optional[int]= None
    league_name:str


    class Config:
        from_atributes = True

class countrySchemam(SchemasBaseModel):
    country_id:Optional[int]= None
    country_name:str
    league_id:int
    league: Optional [leagueSchemam] = None

    class Config:
        from_atributes = True

class playerSchemam(SchemasBaseModel):
    player_id: Optional[int]= None 
    player_name:str 
    player_number: int
    player_type: str
    class Config:
        from_atributes = True

class teamSchemam(SchemasBaseModel):
    team_id:Optional[int]=None
    team_name: str
    country_id:int
    league_id: int

    country:Optional[countrySchemam]= None
    league:Optional[leagueSchemam]= None
    class Config:
        from_atributes = True

class continenteSchemam(SchemasBaseModel):
    continente_id:Optional[int] = None
    continente_name:str
    class Config:
        from_atributes = True

class player_continenteSchemam(SchemasBaseModel):
    player_id:int
    continente_id: int

    player:Optional[playerSchemam] = None
    continente:Optional[continenteSchemam] = None
    class Config:
        from_atributes = True 

        