from fastapi import APIRouter, Depends
from app.models.user import User
from app.auth.auth import current_active_user

router = APIRouter(
    prefix='/api/v1'
)


@router.get('/me')
async def authenticated_me(user: User = Depends(current_active_user)):
    return user
