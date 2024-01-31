from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import authentication as schemas
from dependencies import get_db
from models.users import User
from schemas.token import Token
from tools.authentication.hashing import *
from tools.authentication.token import create_access_token

router = APIRouter()


@router.post('/login')
def login(data: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password is incorrect")
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post('/register')
def register(data: schemas.Register, db: Session = Depends(get_db)):
    hashed_password = hash_password(data.password)
    if db.query(User).filter(User.username == data.username).first() or db.query(User).filter(
            User.email == data.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or Email already exists")
    user = User(first_name=data.first_name, last_name=data.last_name, username=data.username, email=data.email,
                password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return Token(access_token=access_token, token_type="bearer")

