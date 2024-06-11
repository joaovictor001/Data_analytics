from core.configs import settings
from sqlalchemy import Column,Integer,String,ForeignKey,Enum
from sqlalchemy.orm import  relationship
import enum

class leagueModel(settings.DBBaseModel):
    __tablename__ = "league"
    league_id: int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    league_name: str = Column(String(100))


class countryModel(settings.DBBaseModel):
    __tablename__="country"
    country_id:int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    country_name:str = Column(String(100))
    league_id:int= Column(Integer, ForeignKey('league.league_id', ondelete="CASCADE"))
    league = relationship("LeagueModel")
    



class teamModel(settings.DBBaseModel):
    __tablename__="team"
    team_id: int= Column (Integer,primary_key=True,autoincrement=True,nullable=False)
    team_name:str = Column(String(100))
    team_founded: int = Column(String(100))
    country_id: int = Column(Integer, ForeignKey('country.country_id', ondelete="CASCADE"))
    league_id: int = Column(Integer, ForeignKey('league.league_id', ondelete="CASCADE"))
   

    country = relationship("countryModel")
    league = relationship("leagueModel")


class playerModel(settings.DBBaseModel):
    __tablename__="player"
    player_id:int = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    player_name:str = Column(String(100))
    player_number: int = Column(Integer)
    player_type = Column(Enum('Goalkeepers','Defenders','Midfielders','attackers'))
    team_id:int =  Column(Integer, ForeignKey('team.team_id',ondelete="CASCADE"))


class competitionsModel(settings.DBBaseModel):
    __tablename__="competitions"
    competitions_id: int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    competitions_name: str = Column(String(100))
    continente= Column(Enum('America', 'Africa', 'Europe', 'Asia', 'Oceania' , 'Antarctica'))

class continenteModel(settings.DBBaseModel):
    __tablename__ = "continente"
    continente_id: int= Column (Integer,primary_key=True,autoincrement=True,nullable=False) 
    continente_name:str = Column(String(100 ))
    
class player_continenteModel(settings.DBBaseModel):
    __tablename__ = "player_continente"
    player_id: int = Column(Integer, ForeignKey('player.player_id'),primary_key=True  )
    continente_id: int = Column(Integer, ForeignKey('continente.continente_id'),primary_key=True  )

    player = relationship("player")
    continente = relationship("continente")
