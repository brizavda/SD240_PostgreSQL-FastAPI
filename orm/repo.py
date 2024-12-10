import orm.modelos as modelos
<<<<<<< HEAD
from sqlalchemy.orm import Session
from sqlalchemy import and_

# Esta función es llamada por api.py
# Para atender GET '/usuarios/(id)'
# select * from usuarios where id = id_usuarios

# ---------- Peticiones a Usuarios ----------
def usuario_por_id(sesion:Session, id_usuario:int):
    print("Select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def lista_usuarios(sesion:Session):
    print("Select * from app.usuarios")
    return sesion.query(modelos.Usuario).all()

#GET '/usuarios?edad={e1}&edad={e2}'
#select * from app.usuarios where edad > e1 and edad < e2
def usuarios_por_edad(sesion:Session, e1:int, e2:int):
    print("Select * from app.compras where edad > e1 and edad < e2")
    return sesion.query(modelos.Usuario).filter(and_(modelos.Usuario.edad > e1, modelos.Usuario.edad < e2)).all()

#DELETE'/usuarios/{id}'
# delete from app.usuarios where id=id_usuario
def borra_usuario_por_id(sesion:Session,id_usuario:int):
    print("# delete from app.usuarios where id= ", id_usuario)
    #1.select para ver si existe el usuario a borrar
    usr = usuario_por_id(sesion, id_usuario)
    #2.Borramos
    if usr is not None:
        #Borramos usuario
        sesion.delete(usr)
        #Confirmamos los cambios
        sesion.commit()
    respuesta = {
        "mensaje":"usuario eliminado"
    }
    return respuesta

# ---------- Peticiones a Compras ----------
def compra_por_id(sesion:Session, id_compra:int):
    print("Select * from app.compras where id = ", id_compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

def lista_compras(sesion:Session):
    print("Select * from app.")
    return sesion.query(modelos.Compra).all()

#GET '/compras?id_usuario={id_usr}&precio={precio}'
#select * from app.compras where id_usuario=id_usr and precio>=p
def compras_usuario_precio(sesion:Session, id_usr:int, p:float):
    print("Select * from app.compras where id_usuario = id_usr and precio >= p ")
    return sesion.query(modelos.Compra).filter(and_(modelos.Compra.id==id_usr, modelos.Compra.precio>=p)).all()


# ---------- Peticiones a Fotos ----------

def foto_por_id(sesion:Session, id_foto:int):
    print("Select * from app.fotos where id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

def lista_fotos(sesion:Session):
    print("Select * from app.fotos")
    return sesion.query(modelos.Foto).all()

#Buscar fotos por id de usuario
#GET '/usuario/{id}/fotos'
# select * from app.fotos where id_usuario=id
def fotos_por_id_usuario(sesion:Session, id_usuario:int):
    print("select * from app.fotos where id_usuario=",id_usuario)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_usuario==id_usuario).all()

#Borra fotos por id de usuario
#DELETE '/usuario/{id}/fotos'
def borra_foto_por_id_usuario(sesion:Session,id_usuario:int):
    print("# delete from app.fotos where id_usuario= ", id_usuario)
    #1.select para ver si existe el usuario a borrar
    fotos_usr = fotos_por_id_usuario(sesion, id_usuario)
    #2.Borramos
    
    if fotos_usr is not None:
        #Borramos usuario
        sesion.delete(fotos_usr)
        #Confirmamos los cambios
        sesion.commit()
    respuesta = {
        "mensaje":"foto eliminada"
    }
    return respuesta
=======
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ------------ Peticiones a usuarios ---------------------
# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

# Buscar fotos por id de usuario
# GET '/usuarios/{id}/fotos'
# select * from app.fotos where id_usuario=id
def fotos_por_id_usuario(sesion:Session,id_usuario:int):
    print("select * from app.fotos where id_usuario=", id_usuario)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_usuario==id_usuario).all() 

# select * from app.compras where id_usuario=id
def compras_por_id_usuario(sesion:Session,id_usuario:int):
    print("select * from app.compras where id_usuario=", id_usuario)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id_usuario==id_usuario).all() 

# Borra fotos por id de usuario
# DELETE '/usuarios/{id}/fotos'
# delete from app.fotos where id_usuario=id
def borrar_fotos_por_id_usuario(sesion:Session,id_usuario:int):
    print("delete from app.fotos where id_usuario=",id_usuario)
    fotos_usr = fotos_por_id_usuario(sesion, id_usuario)
    if fotos_usr is not None:
        for foto_usuario in fotos_usr:
            sesion.delete(foto_usuario)
        sesion.commit()

# Borra compras por id de usuario
# DELETE '/usuarios/{id}/compras'
# delete from app.compras where id_usuario=id
def borrar_compras_por_id_usuario(sesion:Session,id_usuario:int):
    print("delete from app.compras where id_usuario=",id_usuario)
    compras_usr = compras_por_id_usuario(sesion, id_usuario)
    if compras_usr is not None:
        for compra_usuario in compras_usr:
            sesion.delete(compra_usuario)
        sesion.commit()

# GET '/usuarios'
# select * from app.usuarios
def devuelve_usuarios(sesion:Session):
    print("select * from app.usuarios")
    return sesion.query(modelos.Usuario).all()

#PUT '/usuarios/{id}'
def actualiza_usuario(sesion:Session,id_usuario:int,usr_esquema:esquemas.UsuarioBase):
    #1.-Verificar que el usuario existe
    usr_bd = usuario_por_id(sesion,id_usuario)
    if usr_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        usr_bd.nombre = usr_esquema.nombre
        usr_bd.edad = usr_esquema.edad
        usr_bd.domicilio = usr_esquema.domicilio
        usr_bd.email = usr_esquema.email
        usr_bd.password = usr_esquema.password
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(usr_bd)
        #5.-Imprimir los datos nuevos
        print(usr_esquema)
        return usr_esquema
    else:
        respuesta = {"mensaje":"No existe el usuario"}
        return respuesta

# DELETE '/usuarios/{id}'
# delete from app.usuarios where id=id_usuario
def borra_usuario_por_id(sesion:Session,id_usuario:int):
    print("delete from app.usuarios where id=", id_usuario)
    #1.- borro compras del usuario
    borrar_compras_por_id_usuario(sesion, id_usuario)
    #2.-borro foto del usuario
    borrar_fotos_por_id_usuario(sesion, id_usuario)
    #3.- select para ver si existe el usuario a borrar
    usr = usuario_por_id(sesion, id_usuario)
    #4.- Borramos
    if usr is not None:
        #Borramos usuario
        sesion.delete(usr)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "usuario eliminado"
    }
    return respuesta

# ------------ Peticiones a fotos ---------------------
# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

# GET '/fotos'
# select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# ------------ Peticiones a compras ---------------------
# GET '/compras/{id}'
# select * from app.compras where id = id_compra
def compra_por_id(sesion:Session,id_compra:int):
    print("select * from compras where id = id_compra")
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

# GET '/compras'
# select * from app.compras
def devuelve_compras(sesion:Session):
    print("select * from app.compras")
    return sesion.query(modelos.Compra).all()

# GET '/compras?id_usuario={id_usr}&precio={p}'
# select * from app.compras where id_usuario=id_usr and precio>=p
def devuelve_compras_por_usuario_precio(sesion:Session, id_usr:int, p:float):
    print("select * from app.compras where id_usuario=id_usr and precio>=p")
    return sesion.query(modelos.Compra).filter(and_(modelos.Compra.id_usuario==id_usr, modelos.Compra.precio>=p)).all()
>>>>>>> fa3f46c90d27d8884fe85d2a3c1847f95f8b1fdb
