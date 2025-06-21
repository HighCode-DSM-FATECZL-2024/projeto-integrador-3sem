from fastapi import APIRouter

auth = APIRouter(prefix="/auth", tags=["Authentication"])

@auth.post("/login")
async def login(): pass

@auth.post("/logout")
async def logout():
    return {"msg": "Logout feito"}

@auth.post("/signup")
async def register():
    return {"msg": "Usuário criado"}