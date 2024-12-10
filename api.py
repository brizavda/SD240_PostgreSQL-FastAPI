from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo # Para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_session # Generador de sesiones


# creación del servidor
app = FastAPI()

#definición de la base del usuario
class UsuarioBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str    
    
usuarios = [{
    "id": 0,
    "nombre": "Homero Simpson",
    "edad": 40,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 1,
    "nombre": "Marge Simpson",
    "edad": 38,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 2,
    "nombre": "Lisa Simpson",
    "edad": 8,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 3,
    "nombre": "Bart Simpson",
    "edad": 10,
    "domicilio": "Av. Simpre Viva"
}]


# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta

# ---------- Consultas a Usuarios ----------
@app.get("/usuarios/{id}/compras/{id_compra}")
def compras_usuario_por_id(id: int, id_compra: int):
    print("buscando compra con id:", id_compra, " del usuario con id:", id)
    # simulamos la consulta
    compra = {
        "id_compra": 787,
        "producto": "TV",
        "precio": 14000
    }

    return compra

@app.get("/usuarios/{id}")
def usuario_por_id(id:int, sesion:Session=Depends(generador_session)):
    print("Api consultando usuario por id")
    return repo.usuario_por_id(sesion, id)

    # simulamos consulta a la base:
    #return usuarios[id]

@app.get("/usuarios")
def lista_usuarios(e1:int, e2:int, sesion:Session=Depends(generador_session)):
    print("/usuarios?edad>{e1}&edad<{e2}")
    return repo.usuarios_por_edad(sesion, e1, e2)
#def lista_usuarios(*,lote:int=10,pag:int,orden:Optional[str]=None): #parametros de consulta ?lote=10&pag=1
    #print("lote:",lote, " pag:", pag, " orden:", orden)
    #simulamos la consulta
    #return usuarios

@app.post("/usuarios")
def guardar_usuario(usuario:UsuarioBase, parametro1:str):
    print("usuario a guardar:", usuario, ", parametro1:", parametro1)
    #simulamos guardado en la base.
    
    usr_nuevo = {}
    usr_nuevo["id"] = len(usuarios)
    usr_nuevo["nombre"] = usuario.nombre
    usr_nuevo["edad"] = usuario.edad
    usr_nuevo["domicilio"] = usuario.domicilio

    usuarios.append(usuario)

    return usr_nuevo

@app.put("/usuario/{id}")
def actualizar_usuario(id:int, usuario:UsuarioBase):
    #simulamos consulta
    usr_act = usuarios[id]
    #simulamos la actualización
    usr_act["nombre"] = usuario.nombre
    usr_act["edad"] = usuario.edad
    usr_act["domicilio"] = usuario.domicilio    

    return usr_act
    
@app.delete("/usuario/{id}")
def borrar_usuario(id:int, sesion:Session=Depends(generador_session)):
    repo.borra_usuario_por_id(sesion,id)
    return {"usuario_borrado", "ok"}

# ---------- Consultas a Compras ----------

@app.get("/compras/{id}")
def compra_por_id(id:int, sesion:Session=Depends(generador_session)):
    print("Api consultando compra por id")
    return repo.compra_por_id(sesion, id)

@app.get("/compras")
def lista_compras(id_usuario:int, precio:float, sesion:Session=Depends(generador_session)):
    print("/compras?id_usuario={id_usr}&precio={precio}")
    return repo.compras_usuario_precio(sesion, id_usuario, precio)

# ---------- Consultas a Fotos ----------

@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generador_session)):
    print("Api consultando foto por id")
    return repo.foto_por_id(sesion, id)

@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_session)):
    print("API consultando todas las fotos")
    return repo.lista_fotos(sesion)

@app.get("/usuarios/{id}/fotos")
def fotos_por_id_usr(id:int, sesion:Session=Depends(generador_session)):
    print("API consultando fotos de usuario")
    return repo.fotos_por_id_usuario(sesion,id)

@app.post("/fotos")
async def guardar_foto(titulo:str=Form(None), descripcion:str=Form(...), foto:UploadFile=File(...)):
    print("titulo:", titulo)
    print("descripcion:", descripcion)

    home_usuario=os.path.expanduser("~")
    nombre_archivo=uuid.uuid4().hex  #generamos nombre único en formato hexadecimal
    extension = os.path.splitext(foto.filename)[1]
    ruta_imagen=f'{home_usuario}/fotos-ejemplo/{nombre_archivo}{extension}'
    print("guardando imagen en ruta:", ruta_imagen)

    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read() #read funciona de manera asyncrona
        imagen.write(contenido)

    return {"titulo":titulo, "descripcion":descripcion, "foto":foto.filename}