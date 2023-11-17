from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base
class Cinematography(Base):
    __tablename__ = "cinematography"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    variety_id = Column(Integer, ForeignKey('variety.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    description = Column(String)
    #image

class Variety(Base):
    __tablename__ = "variety"

    id = Column(Integer, primary_key=True, index=True)
    variety_name = Column(String)
    description = Column(String)

class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    genre_name = Column(String)
    description = Column(String)

class Directors(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)