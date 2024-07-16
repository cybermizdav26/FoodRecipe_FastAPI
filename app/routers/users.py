from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.utils import get_hashed_password
from sql_app.database import get_db
from sql_app.models.user import User
from sql_app.schemas.users import UserOutput, UserCreate, UserUpdate, FollowingCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/user-create", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_hashed_password(user.password)
    user = User(email=user.email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{user_id}", response_model=UserOutput, status_code=status.HTTP_201_CREATED)
def user_update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id==user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    db_user.username = user.username
    db_user.fullname = user.fullname
    db_user.birthday = user.birthday
    db_user.phone = user.phone
    db_user.about_me = user.about_me
    db.add(db_user)
    db.commit()
    return db_user


@router.post("/user-following", status_code=status.HTTP_201_CREATED)
def following_create(following: int, follow: FollowingCreate, db: Session = Depends(get_db)):
    pass

