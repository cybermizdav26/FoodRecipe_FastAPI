from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.utils import get_hashed_password
from sql_app.database import get_db
from sql_app.models.user import User, Follow
from sql_app.schemas.users import UserOutput, UserCreate, UserUpdate, FollowCreate, FollowerList, \
    FollowOutPut, FollowingList

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
    db_user = db.query(User).filter(User.id == user_id).first()
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


@router.post("/follow", response_model=FollowOutPut, status_code=status.HTTP_201_CREATED)
def create_follow(follow: FollowCreate, db: Session = Depends(get_db)):
    follower_user = db.query(User).filter(User.id == follow.follower).first()
    following_user = db.query(User).filter(User.id == follow.following).first()

    if not follower_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Follower not found!")
    if not following_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Following user not found!")

    existing_follow = db.query(Follow).filter(
        Follow.follower == follow.follower,
        Follow.following == follow.following
    ).first()

    if existing_follow:
        existing_follow.is_following = follow.is_following
        db.add(existing_follow)
    else:
        new_follow = Follow(
            follower=follow.follower,
            following=follow.following,
            is_following=follow.is_following
        )
        db.add(new_follow)

    db.commit()
    db.refresh(existing_follow or new_follow)

    return existing_follow or new_follow


@router.get("/follower_list/{user_id}", response_model=List[FollowerList])
def followers_list(user_id: int, db: Session = Depends(get_db)):
    followers = db.query(Follow).filter(Follow.following == user_id).all()
    if not followers:
        return []
    return followers


@router.get("/following_list/{user_id}", response_model=List[FollowingList])
def followings_list(user_id: int, db: Session = Depends(get_db)):
    followings = db.query(Follow).filter(Follow.follower == user_id).all()
    if not followings:
        return []
    return followings





