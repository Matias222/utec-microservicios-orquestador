from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    correo: str

class PrecioPeor(BaseModel):
    precio: float
    titulo: str
    puntuacion: int

class UsuariosResenas(BaseModel):
    usuarios: list[Usuario]

class LibrosPeor(BaseModel):
    libros: list[PrecioPeor]