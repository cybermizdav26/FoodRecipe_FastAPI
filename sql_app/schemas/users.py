from datetime import date, datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "food_recipe@gmail.com",
                    "password": "string"
                }
            ]
        }
    }


class UserOutput(BaseModel):
    email: EmailStr


class UserUpdate(BaseModel):
    username: str = Field(examples=["food_recipe"])
    fullname: str = Field(examples=["Mizrobov Abbosbek"])
    birthday: date | None = Field(default=None, examples=["YYYY-MM-DD"])
    phone: str = Field(examples=["+9989XXXXXXXX"])
    about_me: str | None = Field(default=None, examples=["information about yourself"])


class UserProfile(BaseModel):
    username: str
    fullname: str
    birthday: date
    phone: str
    about_me: str


class FollowCreate(BaseModel):
    follower: int
    following: int
    is_following: bool


class FollowOutPut(BaseModel):
    id: int
    follower: int
    following: int
    is_following: bool
    created_at: datetime


class FollowerList(BaseModel):
    id: int
    follower: int
    is_following: bool
    created_at: datetime


class FollowingList(BaseModel):
    id: int
    following: int
    is_following: bool
    created_at: datetime


