from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
from models import UsuariosResenas, LibrosPeor

import os
import funciones

load_dotenv()

API_GESTION=os.getenv("API_GESTION")
API_COMENTARIOS=os.getenv("API_COMENTARIOS")
app = FastAPI(title="MV1")

@app.get("/nombres_mas_resenas")
def nombres_con_mas_resenas() -> UsuariosResenas:

    return funciones.usuarios_resenas()

@app.get("/libros_peor_resenados")
def libros_peor_resenados() -> LibrosPeor:

    return funciones.peor_criticado()

