from fastapi import FastAPI

# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

# Endpoint de ejemplo
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
