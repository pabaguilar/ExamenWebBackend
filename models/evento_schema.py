from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime, timezone, timedelta
from typing import List
from typing import Literal

class eventoSchema(BaseModel):
    timestamp: datetime = Field(default_factory=lambda:datetime.now(timezone(timedelta(hours=2))), description="Fecha de evento")
    lugar: str = Field(..., max_length=200,description="Lugar.")
    lat: float = Field(...,description="Latitud.")
    lon: float = Field(...,description="Longitud.")
    email: str = Field(...,description="Email del organizador.")
    imagen: str = Field(...,description="URL de imagen")

