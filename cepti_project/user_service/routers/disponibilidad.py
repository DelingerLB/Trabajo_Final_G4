from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Disponibilidad
from ..schemas import DisponibilidadResponse

router = APIRouter()


@router.get("/disponibilidad/", response_model=List[DisponibilidadResponse])
def get_disponibilidad(db: Session = Depends(get_db)):
    disponibilidad = db.query(Disponibilidad).all()
    if not disponibilidad:
        raise HTTPException(
            status_code=404, detail="No hay disponibilidad registrada")
    return disponibilidad
