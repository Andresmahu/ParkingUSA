# Usa una imagen oficial de Python
FROM python:3.12

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt /app/requirements.txt


# Instala las dependencias sin caché
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# Expone el puerto 8000 para FastAPI
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
