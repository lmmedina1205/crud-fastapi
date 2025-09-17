from fastapi import APIRouter, Depends
from app.schemas import User, UserId, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []
   
@router.get("/", response_model = list[ShowUser])
def obtener_usuarios(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data

@router.post("/")
def crear_usuario(user: User, db: Session = Depends(get_db)):
    usuario = user.model_dump()

    # ✅ Verificar si ya existe por username o correo
    usuario_existente = db.query(models.User).filter(
        (models.User.username == usuario["username"]) |
        (models.User.correo == usuario["correo"])
    ).first()

    if usuario_existente:
        return {"error": "El usuario ya existe con ese username o correo"}

    # Crear nuevo usuario
    nuevo_usuario = models.User(
        username=usuario["username"],
        password=usuario["password"],   # ⚠️ ideal: hashear antes de guardar
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
        correo=usuario["correo"]
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {
        "mensaje": "Usuario creado satisfactoriamente",
        "usuario": nuevo_usuario
    }

@router.get('/{user_id}', response_model = ShowUser)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"respuesta": "Usuario no encontrado"}    
    return usuario

@router.post('/obtener_usuarios')
def obtener_usuario_2(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            print(user, type(user))
            if user["id"] == user_id.id:
                return {"usuario":user}
        return {"respuesta": "Usuario no encontrado"}

@router.delete("/{user_id}")
def eliminar_usuario(user_id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"respuesta": "Usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    db.commit()
    return {"respuesta": "Usuario eliminado correctamente"}

@router.patch("/{user_id}")
def actualizar_usuario(user_id:int, updateUser: UpdateUser, db: Session = Depends(get_db) ):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"respuesta": "Usuario no encontrado"}
    usuario.update(updateUser.model_dump( exclude_unset=True ))
    db.commit()
    return {"respuesta": "Usuario actualizado correctamente"}