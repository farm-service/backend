from fastapi import FastAPI
from app.configuration.server import Server
from fastapi.middleware.cors import CORSMiddleware


def create_app(_=None) -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
        "https://localhost:5173",
        "http://localhost:5173"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    return Server(app).get_app()
