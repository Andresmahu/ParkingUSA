from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🛠️ Configurar CORS para permitir peticiones desde React Native
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir acceso desde cualquier origen (puedes cambiarlo)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# 📌 Ruta de prueba
@app.get("/")
def read_root():
    return {"message": "¡Hola desde FastAPI!"}

# 📌 Ruta de ejemplo con datos
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Usuario de prueba"}
