from fastapi import APIRouter, Depends
from app.auth.models import User
from app.auth.auth import current_active_user
from app.auth import get_async_session

router = APIRouter(
    prefix='/api/v1'
)


@router.get('/me')
async def authenticated_me(user: User = Depends(current_active_user)):
    db_session = await get_async_session()
    user_with_role = db_session.query(User).options(joinedload(User.role)).filter_by(id=user.id).first()

    return {"permissions": user_with_role}
