from fastapi import APIRouter

users = APIRouter(prefix="/users", tags=["Users"])

@users.get("/")
async def get_all_users():
    return {"msg": "Lista de usuários"}

@users.get("/{id}")
async def get_user_by_id(id: str):
    return {"msg": f"Usuário {id}"}

@users.post("/")
async def post_user():
    return {"msg": "Usuário criado"}

@users.delete("/{id}")
async def delete_user_by_id(id: str):
    return {"msg": f"Usuário {id} deletado"}

@users.put("/{id}")
async def put_user_by_id(id: str):
    return {"msg": f"Usuário {id} atualizado"}

@users.get("/me")
async def get_current_user():
    return {"msg": "Usuário logado"}
