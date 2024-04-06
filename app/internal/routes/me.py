import uuid

from fastapi import APIRouter, Depends
from app.models.user import User
from app.auth.auth import current_active_user
from pydantic import BaseModel

router = APIRouter(
    prefix='/api/v1'
)


class Me(BaseModel):
    id: uuid.UUID
    role_id: int


@router.get('/me')
async def authenticated_me(user: User = Depends(current_active_user)):
    return Me(id=user.id, role_id=user.role_id)
