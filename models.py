from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    correo: str

class UsuariosResenas(BaseModel):
    usuarios: list[Usuario]