from pydantic import BaseModel

class Cinematography(BaseModel):
    name: str
    variety_id: int
    description: str

class addCinematography(Cinematography):
    pass