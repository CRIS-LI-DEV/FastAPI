from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


    
@app.get("/usuarios")
async def root():
    data_list = [
    {"nombre": f"juan_{i+1}", "edad": 12 + i, "pais": "chile"} 
    for i in range(50)
]
    return data_list