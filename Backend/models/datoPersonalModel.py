from pydantic import BaseModel, EmailStr
from typing import  Optional

class DatoPersonal(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    edad: int
    rut: str
    profesion: str
    id_comuna: int
    nombre_usuario:str
    id_dato_personal: Optional[int]
