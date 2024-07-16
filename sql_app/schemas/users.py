from datetime import date

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
    id: int
    email: EmailStr


class UserUpdate(BaseModel):
    username: str = Field(examples=["food_recipe"])
    fullname: str = Field(examples=["Mizrobov Abbosbek"])
    birthday: date | None = Field(default=None, examples=["YYYY-MM-DD"])
    phone: str = Field(examples=["+9989XXXXXXXX"])
    about_me: str | None = Field(default=None, examples=["information about yourself"])


class FollowingCreate(BaseModel):
    following: int
