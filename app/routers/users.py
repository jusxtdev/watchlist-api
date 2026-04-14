from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User

router = APIRouter(
    prefix = '/users',     # Specify prefix for this route
    tags = ['User']
)

@router.get('/')
def all_users(db : Session = Depends(get_db)):
    return db.query(User).all()

@router.post('/')
def add_user(db : Session = Depends(get_db)):
    user = User(
        username="Dev",
        password="123",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user