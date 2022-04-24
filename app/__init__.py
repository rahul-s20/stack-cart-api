from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.route import router


def create_app():
    app = FastAPI()
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
