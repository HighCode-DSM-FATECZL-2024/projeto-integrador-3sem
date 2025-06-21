from fastapi import FastAPI

from app.handlers.exception_handlers import register_exception_handlers
from app.modules.users.routes import users as users_route
from app.modules.auth.routes import auth as auth_route

def create_app(title: str,version: str) -> FastAPI:
    app = FastAPI(title=title, version=version)

    register_exception_handlers(app)

    app.include_router(auth_route, prefix="/api")
    app.include_router(users_route, prefix="/api")

    return app
