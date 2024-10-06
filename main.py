from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
from models import UsuariosResenas

import os
import funciones

load_dotenv()

API_GESTION=os.getenv("API_GESTION")
API_COMENTARIOS=os.getenv("API_COMENTARIOS")
app = FastAPI()

@app.get("/nombres_mas_resenas")
def nombres__con_mas_resenas() -> UsuariosResenas:

    return funciones.usuarios_resenas()

