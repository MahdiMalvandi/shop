from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.users import User
from schemas.products import UserWithProducts
from schemas.users import *
from dependencies import get_db
from tools.authentication.token import get_current_user

router = APIRouter()


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return 'deleted'


# region profile
@router.get(path="/profile", response_model=UserWithProducts)
def profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user

# endregion
