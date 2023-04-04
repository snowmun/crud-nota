from pydantic import BaseModel, EmailStr
from typing import  Optional

class DatoPersonal(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    edad: int
    rut: str
    profesion: str
    nombre_usuario:str
    id_comuna: int
    id_dato_personal: Optional[int]
