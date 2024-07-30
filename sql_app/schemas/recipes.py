from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "recipe category"
                }
            ]
        }
    }


class CategoryAndTagsOutput(BaseModel):
    id: int
    name: str


class TagsCreate(BaseModel):
    name: str


class RecipeIngredient(BaseModel):
    ingredient_name: str
    ingredient_image: Optional[str]


class RecipeCreate(BaseModel):
    category_id: int
    user_id: int
    tags_id: int
    title: str
    image: str
    time_minutes: int
    ingredients: list[RecipeIngredient]


class RecipeOutput(BaseModel):
    id: int
    title: str
    created_at: datetime
