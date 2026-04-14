from fastapi import APIRouter
from app.routers import user_router


router = APIRouter(
    prefix = '',     # Specify prefix for this route
    tags = ['Root']
)

@router.get('/')
def root():
    return {"msg" : "Hello"}

router.include_router(user_router.router)
