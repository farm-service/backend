from fastapi import APIRouter, Depends
from app.auth.models import User
from pydantic import BaseModel

router: APIRouter = APIRouter(
    prefix='/api/v1'
)
