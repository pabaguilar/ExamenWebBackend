from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime, timezone, timedelta
from typing import List
from typing import Literal


# class Invitados(BaseModel):
#     useremail: str = Field(...)
#     estado: Literal["aceptada", "pendiente"] = Field("pendiente", title="Estado de la invitación")

# class primerSchema(BaseModel):
#     anfitrion: str = Field(...)
#     descripción: str = Field(..., max_length=50,description="Descripcion.")
#     inicio: datetime = Field(default_factory=lambda:datetime.now(timezone(timedelta(hours=2))), description="Fecha de la edición")
#     duracion: int = Field(...,description="Duracion del evento en tramos de 15 minutos")
#     invitados : List[Invitados] = Field(default_factory=list,description="Lista de invitados")

class eventoSchema(BaseModel):
    nombre: str = Field(...)
    timestamp: datetime = Field(default_factory=lambda:datetime.now(timezone(timedelta(hours=2))), description="Fecha de evento")
    lugar: str = Field(..., max_length=200,description="Lugar.")
    lat: float = Field(...,description="Latitud.")
    lon: float = Field(...,description="Longitud.")
    organizador: str = Field(...,description="Email del organizador.")
    imagen: str = Field(...,description="URL de imagen")

