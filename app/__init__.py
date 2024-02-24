from fastapi import FastAPI
from app.configuration.server import Server
from fastapi.middleware.cors import CORSMiddleware


def create_app(_=None) -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    return Server(app).get_app()
