from fastapi import APIRouter, Depends
from app.models.user import User
from pydantic import BaseModel

router: APIRouter = APIRouter(
    prefix='/api/v1'
)
