from fastapi import APIRouter

router: APIRouter = APIRouter(
    prefix='/api/v1'
)


@router.get('/test')
def get_test():
    return {
        'test': True,
        'version': "0.0.0"
    }
