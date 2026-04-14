from fastapi import APIRouter

router = APIRouter(
    prefix = '/users',     # Specify prefix for this route
    tags = ['User']
)

@router.get('/')
def users():
    return "HELLO"