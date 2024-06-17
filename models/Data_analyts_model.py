from core.configs import settings
from sqlalchemy import Column,Integer,String,ForeignKey,Enum
from sqlalchemy.orm import  relationship
import enum


    
class leagueModel(settings.DBBaseModel):
    __tablename__ = "league"
    league_id: int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    league_name: str = Column(String(100))

    countries = relationship("countryModel", back_populates="league")
    teams = relationship("teamModel", back_populates="league")

class countryModel(settings.DBBaseModel):
    __tablename__="country"
    country_id:int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    country_name:str = Column(String(100))
    league_id:int= Column(Integer, ForeignKey('league.league_id', ondelete="CASCADE"))

    league = relationship("leagueModel", back_populates="countries")
    teams = relationship("teamModel", back_populates="country")




class teamModel(settings.DBBaseModel):
    __tablename__="team"
    team_id: int= Column (Integer,primary_key=True,autoincrement=True,nullable=False)
    team_name:str = Column(String(100))
    team_founded: int = Column(String(100))
    country_id: int = Column(Integer, ForeignKey('country.country_id', ondelete="CASCADE"))
    league_id: int = Column(Integer, ForeignKey('league.league_id', ondelete="CASCADE"))
   

    country = relationship("countryModel", back_populates="teams")
    league = relationship("leagueModel", back_populates="teams")
    players = relationship("playerModel", back_populates="team")


class playerModel(settings.DBBaseModel):
    __tablename__="player"
    player_id:int = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    player_name:str = Column(String(100))
    player_number: int = Column(Integer)
    player_type = Column(Enum('Goalkeepers','Defenders','Midfielders','attackers'))
    team_id:int =  Column(Integer, ForeignKey('team.team_id',ondelete="CASCADE"))

    team = relationship("teamModel", back_populates="players")
    player_continente_associations = relationship("player_continenteModel", back_populates="player")


class competitionsModel(settings.DBBaseModel):
    __tablename__="competitions"
    competitions_id: int =Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    competitions_name: str = Column(String(100))
    continente= Column(Enum('America', 'Africa', 'Europe', 'Asia', 'Oceania' , 'Antarctica'))

class continenteModel(settings.DBBaseModel):
    __tablename__ = "continente"
    continente_id: int= Column (Integer,primary_key=True,autoincrement=True,nullable=False) 
    continente_name:str = Column(String(100 ))

    players = relationship("player_continenteModel", back_populates="continente")
    
class player_continenteModel(settings.DBBaseModel):
    __tablename__ = "player_continente"
    player_id: int = Column(Integer, ForeignKey('player.player_id'),primary_key=True  )
    continente_id: int = Column(Integer, ForeignKey('continente.continente_id'),primary_key=True  )

    player = relationship("playerModel", back_populates="player_continente_associations")
    continente = relationship("continenteModel", back_populates="players")