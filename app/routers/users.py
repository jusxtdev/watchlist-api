from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["User"])  # Specify prefix for this route


@router.get("/")
def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/")
def add_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=data.username,
        password=data.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{user_id}")
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    update_data = data.model_dump(exclude_unset=True)

    existing = db.query(User).where(User.id == user_id).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    for key, value in update_data.items():
        setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing = db.query(User).where(User.id == user_id).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    db.delete(existing)
    db.commit()
    return existing
