from fastapi import FastAPI, HTTPException
from database.db import get_db_connection

# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

# Endpoint de ejemplo
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Ruta para testear la conexión a la base de datos
@app.get("/test-db")
async def test_db():
    connection = get_db_connection()
    
    if connection is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        return {"message": "Conexión exitosa a la base de datos", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {e}")
    finally:
        cursor.close()
        connection.close()

print("en el main")