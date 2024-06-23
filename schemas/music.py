from pydantic import BaseModel
from typing import Optional

class Music(BaseModel):
    GeneroMusical: str
    NombreBanda: str
    Exito: str