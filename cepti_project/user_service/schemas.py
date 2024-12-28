from pydantic import BaseModel
from datetime import date, time


class UserCreate(BaseModel):
    dni: str
    name: str
    email: str
    phone: str
    password: str
    role: str


class UserResponse(BaseModel):
    id: int
    dni: str
    name: str
    email: str
    phone: str
    role: str

    class Config:
        orm_mode = True


class DisponibilidadResponse(BaseModel):
    terapeuta_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time

    class Config:
        orm_mode = True
