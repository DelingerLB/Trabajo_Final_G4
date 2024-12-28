from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Simulamos la base de datos en memoria
mock_pacientes = []


class PacienteApoderado(BaseModel):
    nombrePaciente: str
    apellidoPaciente: str
    dniPaciente: str
    fechaNacimiento: str
    nombreApoderado: str
    apellidoApoderado: str
    dniApoderado: str
    telefonoApoderado: str
    direccion: str


@router.post("/paciente/register")
def register_paciente(paciente: PacienteApoderado):
    # Verificar si el DNI del paciente ya está registrado
    for p in mock_pacientes:
        if p["dniPaciente"] == paciente.dniPaciente:
            raise HTTPException(
                status_code=400, detail="El DNI del paciente ya está registrado")

    # Verificar si el DNI del apoderado ya está registrado
    for p in mock_pacientes:
        if p["dniApoderado"] == paciente.dniApoderado:
            raise HTTPException(
                status_code=400, detail="El DNI del apoderado ya está registrado")

    mock_pacientes.append(paciente.dict())
    return {"message": "Registro exitoso"}
