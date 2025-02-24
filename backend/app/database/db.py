import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración del pool de conexiones
db_config = {
    "host": "localhost",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": "parkside"
}

try:
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=5,
        **db_config
    )
except mysql.connector.Error as e:
    print(f"Error al crear el pool de conexiones: {e}")

# Función para obtener una conexión del pool
def get_db_connection():
    try:
        return connection_pool.get_connection()
    except mysql.connector.Error as e:
        print(f"Error al obtener conexión de la base de datos: {e}")
        return None
