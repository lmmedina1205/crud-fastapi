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

app = FastAPI()

@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Bienvenido a tu primera api con FastAPI"}

@app.post("/ruta2")
def ruta2(user: User):
    usuario = user.dict()
    print(usuario)
    return True

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
