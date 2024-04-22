import logging

from fastapi import FastAPI
from app.configuration.server import Server
from app.configuration.settings import BUILD_FULL_SEMANTIC_VERSION
from fastapi.middleware.cors import CORSMiddleware


def create_app(_=None) -> FastAPI:
    app = FastAPI(version=BUILD_FULL_SEMANTIC_VERSION)
    print(f"Build version: {BUILD_FULL_SEMANTIC_VERSION}")

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
