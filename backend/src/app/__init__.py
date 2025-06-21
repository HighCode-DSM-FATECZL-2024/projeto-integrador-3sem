from fastapi import FastAPI
from app.modules.users.routes import users as users_route
from app.modules.auth.routes import auth as auth_route

def create_app(title: str,version: str) -> FastAPI:
    app = FastAPI(title=title, version=version)

    app.include_router(auth_route, prefix="/api")
    app.include_router(users_route, prefix="/api")

    return app
