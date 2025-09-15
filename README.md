# crud-fastapi

# Dos formas para ejecutar fastapi 

1 uvicorn main:app
2 agregar import uvicorn 
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
    y lugo correr python main.py