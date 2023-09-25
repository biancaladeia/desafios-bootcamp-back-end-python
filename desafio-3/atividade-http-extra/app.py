from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(id=UUID("6b5f94a3-f34b-440a-a75f-f69119b78325"), 
        first_name="Ana", 
        last_name="Maria", 
        email="email@gmail.com", 
        role=[Role.role_1]
        ),
    User(id=UUID("6055eddf-e120-4108-b93e-b16b68f857a5"), 
        first_name="Cynthia", 
        last_name="Zanoni", 
        email="email@gmail.com", 
        role=[Role.role_2]
        ),
    User(id=UUID("a3542bf7-a3c5-4481-aeed-228f2c220e5e"), 
        first_name="Camila", 
        last_name="Silva", 
        email="email@gmail.com", 
        role=[Role.role_3]
        )        
]

@app.get("/api/users")
async def get_users():
    return db # O retorno será a lista de usuários pré cadastrados

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user # O retorno será a pesquisa do usuário especificado pelo id
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def create_user(user: User):
    '''
    Adiciona um novo usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    '''
    db.append(user)
    return {"id": user.id}  # O retorno será o número do usuário após o cadastro

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException( # O retorno será o status code 404 caso o usuário não seja encontrado
        status_code=404, 
        detail=f"Usuário usuário com o id {id} não encontrado!"
    )