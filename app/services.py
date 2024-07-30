from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import get_db
from sql_app.models.user import User


def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
