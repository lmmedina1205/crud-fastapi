from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Bienvenido a tu primera api con FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
