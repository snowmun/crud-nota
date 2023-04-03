from typing import  Optional
from pydantic import BaseModel

class Nota(BaseModel):
    titulo: str
    contenido: str
    activo: bool
    fecha_termino: str
    id_usuario: Optional[str]
    id_tipo: int
    etiqueta:  Optional[int]
