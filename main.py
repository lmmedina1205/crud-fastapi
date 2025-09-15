from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
    id:int
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    creacion_user:datetime = datetime.now()

class UserId(BaseModel):
    id:int


app = FastAPI()
usuarios = []

@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Bienvenido a tu primera api con FastAPI"}
    
@app.get('/user')
def obtener_usuarios():
    return usuarios

@app.post("/user")
def crear_usuario(user: User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"mensaje": "Usuario creado satisfactoriamente", "usuario": usuario}

@app.get("/user/{user_id}")
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            print(user, type(user))
            if user["id"] == user_id:
                return {"usuario":user}
        return {"respuesta": "Usuario no encontrado"}

@app.post('/obtener_usuarios')
def obtener_usuario_2(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            print(user, type(user))
            if user["id"] == user_id.id:
                return {"usuario":user}
        return {"respuesta": "Usuario no encontrado"}

@app.delete("/user/{user_id}")
def eliminar_usuario(user_id:int):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente"}
    return {"respuesta": "Usuario no encontrado"}


@app.put("/user/{user_id}")
def actualizar_usuario(user_id:int, updateUser: User ):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["id"] = updateUser.dict()["id"]
            usuarios[index]["nombre"] = updateUser.dict()["nombre"]
            usuarios[index]["apellido"] = updateUser.dict()["apellido"]
            usuarios[index]["direccion"] = updateUser.dict()["direccion"]
            usuarios[index]["telefono"] = updateUser.dict()["telefono"]
            return {"respuesta": "Usuario actualizado correctamente"}
    return {"respuesta": "Usuario no encontrado"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
