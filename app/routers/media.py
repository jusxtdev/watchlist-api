from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.media import Media
from app.schemas.media import MediaCreate, MediaUpdate

router = APIRouter(prefix="/media", tags=["Media"])

@router.get('/')
def all_media(db : Session = Depends(get_db)):
    return db.query(Media).all()

@router.post('/')
def add_media(data : MediaCreate, db : Session = Depends(get_db)):
     new_media = Media(
         title = data.title,
         watched = data.watched,
         genre = data.genre
     )
     db.add(new_media)
     db.commit()
     db.refresh(new_media)
     return new_media
 
@router.put('/{media_id}')
def update_media(media_id : int, data : MediaUpdate, db : Session = Depends(get_db)):
    update_data = data.model_dump(exclude_unset=True)
    existing = db.query(Media).where(Media.id == media_id).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Media not found"
        )

    for key, val in update_data.items():
        setattr(existing, key, val)
        
    db.commit()
    db.refresh(existing)
    return existing