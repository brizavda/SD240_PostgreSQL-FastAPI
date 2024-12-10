import orm.modelos as modelos
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