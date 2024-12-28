from sqlalchemy import Column, Integer, String, Boolean, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Disponibilidad(Base):
    __tablename__ = 'disponibilidad'

    id = Column(Integer, primary_key=True, index=True)
    terapeuta_id = Column(Integer, ForeignKey('terapeutas.id'))
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)

    terapeuta = relationship("Terapeuta", back_populates="disponibilidad")
