from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["User"])  # Specify prefix for this route

# TODO - Model error responses

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id : int, db : Session = Depends(get_db)):
    requested = db.query(User).where(User.id == user_id).first()
    
    if not requested:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return requested    
    
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def add_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=data.username,
        password=data.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.patch("/{user_id}", response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED)
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


@router.delete("/{user_id}", response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing = db.query(User).where(User.id == user_id).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    db.delete(existing)
    db.commit()
    return existing
