import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
db_config = {
    "host": "localhost",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": "parkside"
}

# Inicializar el pool de conexiones
connection_pool = None

try:
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=5,
        **db_config
    )
    print("✅ Pool de conexiones creado correctamente")
except mysql.connector.Error as e:
    print(f"Error al crear el pool de conexiones: {e}")

# Función para obtener una conexión
def get_db_connection():
    if connection_pool is None:
        print("El pool de conexiones no está disponible")
        return None
    
    try:
        return connection_pool.get_connection()
    except mysql.connector.Error as e:
        print(f"Error al obtener una conexión de la base de datos: {e}")
        return None
