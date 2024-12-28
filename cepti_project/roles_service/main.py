from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

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

# Simular una base de datos en memoria para roles
mock_roles = [
    {"id": 1, "name": "gerente"},
    {"id": 2, "name": "terapeuta"},
    {"id": 3, "name": "operador"},
    {"id": 4, "name": "padre"}
]


class RoleCreate(BaseModel):
    name: str


class RoleResponse(BaseModel):
    id: int
    name: str


@app.post("/roles/", response_model=RoleResponse)
def create_role(role: RoleCreate):
    new_id = len(mock_roles) + 1
    new_role = {"id": new_id, "name": role.name}
    mock_roles.append(new_role)
    return new_role


@app.put("/roles/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role: RoleCreate):
    role_to_update = next((r for r in mock_roles if r['id'] == role_id), None)
    if not role_to_update:
        raise HTTPException(status_code=404, detail="Role not found")
    role_to_update['name'] = role.name
    return role_to_update


@app.get("/roles/", response_model=List[RoleResponse])
def get_roles():
    return mock_roles
