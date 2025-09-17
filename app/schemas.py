from pydantic import BaseModel
from typing import Optional
from datetime import datetime



#User Model
class User(BaseModel): #Schema
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion:datetime = datetime.now()

#Update User Model
class UpdateUser(BaseModel):
    username: str | None = None
    password: str | None = None
    nombre: str | None = None
    apellido: str | None = None
    direccion: str | None = None
    telefono: int | None = None
    correo: str | None = None

class ShowUser(BaseModel):
    username:str
    nombre:str
    correo:str
    apellido:str
    class Config():
        from_attributes = True


        