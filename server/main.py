from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import schemas
import models
from database import Base, engine, SessionLocal, db

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
@app.get("/getCinematographyByGenres/{id}")         #Вывод кинематографа по жанру
async def get_cinematography_by_genres(genre: int):
    cinema = db.query(models.Cinematography).filter(models.Cinematography.genre_id == genre).all()
    return cinema

@app.get("/getCinematography/")         #Вывод всего кинематографа
async def get_cinematography(db: Session = Depends(get_db)):
    return db.query(models.Cinematography).all()

@app.get("/getGenres/")             #Вывод всех жанров
async def get_genres():
    genres = db.query(models.Genres).all()
    return genres