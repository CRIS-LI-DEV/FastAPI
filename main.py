from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen (cambiar según tus necesidades)
    allow_methods=["GET"],  # Permitir solo el método GET (cambiar según tus necesidades)
    allow_headers=["*"],  # Permitir cualquier header (cambiar según tus necesidades)
)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


    
@app.get("/usuarios")
async def rxxx():
    data_list = [
    {"nombre": f"juan_{i+1}", "edad": 12 + i, "pais": "chile"} 
    for i in range(50)
]
    return data_list