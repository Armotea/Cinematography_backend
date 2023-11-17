from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import schemas
import models
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addCinema/")        #Добавление кинематографа в БД
async def add_cinematography(cinematography: schemas.addCinematography, db: Session = Depends(get_db)):
    cinema = models.Cinematography(name=cinematography.name,
                                   variety_id=cinematography.variety_id,
                                   description=cinematography.description)
    db.add(cinema)
    db.commit()
    db.refresh(cinema)

    return cinema

@app.get("/getCinematographyByVarity/")         #Вывод кинематографа по типу кинематографа
async def get_cinematography_by_variety(variety: str, db: Session = Depends(get_db)):
    variety = str.capitalize(variety)
    variety = db.query(models.Variety).filter(models.Variety.variety_name == variety).first().id

    return db.query(models.Cinematography).filter(models.Cinematography.variety_id == variety).all()

@app.get("/getCinematographyByGenres/")
async def get_cinematography_by_genres(genre: str, db: Session = Depends(get_db)):
    genre = str.capitalize(genre)
    genre = db.query(models.Genres).filter(models.Genres.genre_name == genre).first().id

    return db.query(models.Cinematography).filter(models.Cinematography.genre_id == genre).all()


@app.get("/getCinematographyByDirector/")
async def get_cinematography_by_director(director: str, db: Session = Depends(get_db)):
    director = str.capitalize(director)
    director = db.query(models.Directors).filter(models.Directors.name == director).first().id

    return db.query(models.Cinematography).filter(models.Cinematography.director_id == director).all()

@app.get("/getCinematography/")
@app.get("/getCinematography/")
async def get_cinematography(db: Session = Depends(get_db)):
    return db.query(models.Cinematography).all()

@app.get("/getVarieties/")          #Вывод всех типов кинематографа
async def get_Varieties(db: Session = Depends(get_db)):
    return db.query(models.Variety).all()

@app.get("/getGenres/")             #Вывод всех жанров
async def get_genres(db: Session = Depends(get_db)):
    return db.query(models.Genres).all()

@app.get("/getDirectors/")          #Вывод всех режиссёров
async def get_directors(db: Session = Depends(get_db)):
    return db.query(models.Directors).all()