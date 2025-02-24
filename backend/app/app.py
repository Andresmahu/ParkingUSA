from fastapi import FastAPI, HTTPException
from database.db import get_db_connection
from api.login.routes.loginRoute import router as login_router


# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

# Rutas del login
app.include_router(login_router, prefix="/login", tags=["Login"])

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