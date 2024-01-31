from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.users import User

from dependencies import get_db

router = APIRouter()


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return 'deleted'
