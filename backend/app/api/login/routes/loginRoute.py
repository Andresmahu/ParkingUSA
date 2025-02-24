from fastapi import APIRouter, HTTPException
from database.db import get_db_connection

router = APIRouter()

@router.get("/employees")
async def get_employees():
    connection = get_db_connection()
    
    if connection is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos")
    try:
        cursor = connection.cursor(dictionary=True)  # Devuelve los resultados como JSON
        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()
        return {"employees": employees}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {e}")
    finally:
        cursor.close()
        connection.close()
