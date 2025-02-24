# ParkSide

ParkSide es una aplicación para la gestión de estacionamientos, desarrollada con FastAPI y MySQL. Permite a los usuarios administrar empleados, usuarios y realizar operaciones de autenticación.

## Tecnologías Utilizadas

- **FastAPI** - Framework para desarrollar APIs en Python.
- **MySQL** - Base de datos relacional.
- **Uvicorn** - Servidor ASGI para ejecutar la aplicación.
- **Python 3.12.1** - Versión utilizada en el desarrollo.

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/Andresmahu/ParkSide.git
   cd ParkSide
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Configuración

1. Asegúrate de configurar correctamente la conexión a la base de datos en `database/db.py`.
2. La base de datos debe estar activa y accesible antes de ejecutar la aplicación.

## Ejecución del Proyecto

Ejecuta la aplicación con el siguiente comando:
```sh
uvicorn app:app --reload
```

## Endpoints Principales

- `GET /` - Página de bienvenida.
- `GET /test-db` - Prueba de conexión a la base de datos.
- `GET /login/employees` - Obtiene la lista de empleados.

## Estructura del Proyecto

```
ParkSide/
│── api/
│   └── login/
│       └── routes/
│           └── loginRoute.py
│── database/
│   └── db.py
│── app.py
│── requirements.txt
│── README.md
```


## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE` en el repositorio.
