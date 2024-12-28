from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time, datetime
import requests

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simular una base de datos en memoria
mock_users = [{"dni": "12345678", "name": "Ana", "email": "ana@gmail.com",
               "phone": "888888888", "password": "abc123", "id": 1,
               "role": "gerente"},
              {"dni": "23456789", "name": "Luis", "email": "luis@gmail.com",
               "phone": "777777777", "password": "def456", "id": 2,
               "role": "terapeuta", "specialty": "Lenguaje"},
              {"dni": "34567890", "name": "Maria", "email": "maria@gmail.com",
               "phone": "666666666", "password": "ghi789", "id": 3,
               "role": "operador"},
              {"dni": "45678901", "name": "Carlos", "email": "carlos@gmail.com",
               "phone": "555555555", "password": "jkl012", "id": 4,
               "role": "padre"},
              {"dni": "56789012", "name": "Laura", "email": "laura@gmail.com",
               "phone": "444444444", "password": "mno345", "id": 5,
               "role": "terapeuta", "specialty": "Psicológica"},
              {"dni": "67890123", "name": "Pedro", "email": "pedro@gmail.com",
               "phone": "333333333", "password": "pqr678", "id": 6,
               "role": "operador"},
              {"dni": "78901234", "name": "Sofia", "email": "sofia@gmail.com",
               "phone": "222222222", "password": "stu901", "id": 7,
               "role": "padre"},
              {"dni": "89012345", "name": "Diego", "email": "diego@gmail.com",
               "phone": "111111111", "password": "vwx234", "id": 8,
               "role": "gerente"},
              {"dni": "90123456", "name": "Lucia", "email": "lucia@gmail.com",
               "phone": "000000000", "password": "yzb567", "id": 9,
               "role": "terapeuta", "specialty": "Ocupacional"},
              {"dni": "01234567", "name": "Jose", "email": "jose@gmail.com",
               "phone": "999999999", "password": "cde890", "id": 10,
               "role": "operador"}]

# Datos simulados de disponibilidad de terapeutas
mock_disponibilidad = [
    {"terapeuta_id": 2, "fecha": date(2024, 8, 5), "hora_inicio": time(
        9, 0), "hora_fin": time(10, 0)},
    {"terapeuta_id": 2, "fecha": date(2024, 8, 7), "hora_inicio": time(
        10, 0), "hora_fin": time(11, 0)},
    {"terapeuta_id": 5, "fecha": date(2024, 8, 6), "hora_inicio": time(
        11, 0), "hora_fin": time(12, 0)},
    {"terapeuta_id": 5, "fecha": date(2024, 8, 8), "hora_inicio": time(
        13, 0), "hora_fin": time(14, 0)},
    {"terapeuta_id": 9, "fecha": date(2024, 8, 5), "hora_inicio": time(
        14, 0), "hora_fin": time(15, 0)},
    {"terapeuta_id": 9, "fecha": date(2024, 8, 6), "hora_inicio": time(
        15, 0), "hora_fin": time(16, 0)}
]


class UserCreate(BaseModel):
    dni: str
    name: str
    email: str
    phone: str
    password: str
    role: str


class DisponibilidadResponse(BaseModel):
    terapeuta_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time


class Terapeuta(BaseModel):
    id: int
    name: str
    specialty: str


# Montar la carpeta user_interface para servir archivos estáticos
app.mount("/user_interface", StaticFiles(directory="user_interface"),
          name="user_interface")


@app.post("/users/")
async def create_user(user: UserCreate):
    # Generar ID automáticamente de forma correlativa
    new_id = len(mock_users) + 1
    new_user = user.dict()
    new_user['id'] = new_id

    # Verificar si el correo ya está registrado
    existing_user_email = next(
        (u for u in mock_users if u['email'] == user.email), None)
    if existing_user_email:
        raise HTTPException(
            status_code=400, detail="El correo electrónico ya está registrado.")

    # Verificar si el DNI ya está registrado
    existing_user_dni = next(
        (u for u in mock_users if u['dni'] == user.dni), None)
    if existing_user_dni:
        raise HTTPException(
            status_code=400, detail="El DNI ya está registrado.")

    # Crear rol en el servicio de roles
    role_response = requests.post(
        "http://localhost:8001/roles/", json={"name": user.role})
    if role_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error al crear el rol.")

    # Guardar el usuario en la lista (simulando la base de datos)
    mock_users.append(new_user)

    return {"message": "Usuario creado exitosamente", "user": new_user}


@app.get("/users/")
async def get_users():
    return {"users": mock_users}


@app.get("/disponibilidad/", response_model=List[DisponibilidadResponse])
def get_disponibilidad(terapeuta_id: Optional[int] = None):
    if terapeuta_id:
        return [d for d in mock_disponibilidad if d["terapeuta_id"] == terapeuta_id]
    return mock_disponibilidad


@app.get("/terapeutas/", response_model=List[Terapeuta])
def get_terapeutas():
    terapeutas = [user for user in mock_users if user["role"] == "terapeuta"]
    return [{"id": terapeuta["id"], "name": terapeuta["name"], "specialty": terapeuta["specialty"]} for terapeuta in terapeutas]


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    global mock_users
    mock_users = [user for user in mock_users if user["id"] != user_id]
    return {"message": "Usuario eliminado exitosamente"}
