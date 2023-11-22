from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base
class Cinematography(Base):
    __tablename__ = "cinematography"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    variety = Column(String)
    director = Column(String)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    description = Column(String)
    image = Column(String)

class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    genre_name = Column(String)
    description = Column(String)