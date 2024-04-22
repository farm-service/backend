import logging
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
SECRET_JWT = os.getenv('SECRET_JWT')
SECRET_VERIFICATION = os.getenv('SECRET_VERIFICATION')
URL_FORECAST = os.getenv('URL_FORECAST')

DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

BUILD_FULL_SEMANTIC_VERSION = "dev-build"

logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)
