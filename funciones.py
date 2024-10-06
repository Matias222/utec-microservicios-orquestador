from dotenv import load_dotenv
from models import Usuario, UsuariosResenas, PrecioPeor, LibrosPeor

import requests
import os
import json

load_dotenv()

API_GESTION=os.getenv("API_GESTION")
API_COMENTARIOS=os.getenv("API_COMENTARIOS")
API_LIBROS=os.getenv("API_LIBROS")

def usuarios_resenas():

    comentarios=requests.get(f"{API_COMENTARIOS}/reviews")

    mapa={}

    for i in comentarios.json():
        id_cliente=i["id_cliente"]
        if(id_cliente not in mapa): mapa[id_cliente]=1
        else: mapa[id_cliente]+=1

    maxx=-1

    for i in mapa:
        if(maxx<=mapa[i]): maxx=mapa[i]

    respuesta=UsuariosResenas(usuarios=[])

    for i in mapa:
        if(mapa[i]==maxx): 
            
            usuario_req=requests.get(f"{API_GESTION}/clientes/{i}")

            usuario_req=usuario_req.json()

            respuesta.usuarios.append(Usuario(nombre=usuario_req["nombre"],correo=usuario_req["correo"]))
            
    return respuesta

def peor_criticado():

    comentarios=requests.get(f"{API_COMENTARIOS}/reviews")

    mapa={}

    for i in comentarios.json():
        id_cliente=i["id_cliente"]
        if(id_cliente not in mapa): mapa[id_cliente]=i["puntuacion"]
        else: mapa[id_cliente]+=i["puntuacion"]

    minn=100

    for i in mapa:
        if(minn>=mapa[i]): minn=mapa[i]
    
    respuesta=LibrosPeor(libros=[])

    for i in mapa:
        if(mapa[i]==minn):
            
            libros_req=requests.get(f"{API_LIBROS}/libros/{i}")

            libros_req=libros_req.json()

            respuesta.libros.append(PrecioPeor(titulo=libros_req["titulo"],puntuacion=minn,precio=libros_req["precio"]))

    return respuesta
