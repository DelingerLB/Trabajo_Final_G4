from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Plan
from ..schemas import PlanResponse

router = APIRouter()


@router.post("/planes/generar/", response_model=PlanResponse)
def generar_plan(db: Session = Depends(get_db)):
    # Lógica para generar planes automáticamente
    nuevo_plan = Plan()  # Ejemplo simplificado
    db.add(nuevo_plan)
    db.commit()
    db.refresh(nuevo_plan)
    return nuevo_plan


@router.get("/planes/", response_model=List[PlanResponse])
def get_planes(db: Session = Depends(get_db)):
    planes = db.query(Plan).all()
    if not planes:
        raise HTTPException(
            status_code=404, detail="No hay planes disponibles")
    return planes
