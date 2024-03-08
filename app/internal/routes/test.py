from fastapi import APIRouter
from app.configuration.settings import BUILD_FULL_SEMANTIC_VERSION

router: APIRouter = APIRouter(
    prefix='/api/v1'
)


@router.get('/test')
def get_test():
    return {
        'test': True,
        'version': BUILD_FULL_SEMANTIC_VERSION,
    }
