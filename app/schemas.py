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