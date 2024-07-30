from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from sql_app.database import get_db
from sql_app.models.recipe import Category, Tags, Recipe, Ingredients
from sql_app.schemas.recipes import CategoryCreate, CategoryAndTagsOutput, TagsCreate, RecipeOutput, RecipeCreate

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.post("/category-create", response_model=CategoryAndTagsOutput, status_code=status.HTTP_201_CREATED)
def category_create(category: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(name=category.name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.get("/categories", response_model=list[CategoryAndTagsOutput], status_code=status.HTTP_200_OK)
def categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories


@router.post("/tags-create", response_model=CategoryAndTagsOutput, status_code=status.HTTP_201_CREATED)
def tags_create(tag: TagsCreate, db: Session = Depends(get_db)):
    tag = Tags(name=tag.name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.post("/create", response_model=RecipeOutput, status_code=status.HTTP_201_CREATED)
def recipe_create(recipe: RecipeCreate, db: Session = Depends(get_db)):
    new_recipe = Recipe(
        title=recipe.title,
        image=recipe.image,
        time_minutes=recipe.time_minutes,
        category_id=recipe.category_id,
        user_id=recipe.user_id,
        tags_id=recipe.tags_id
    )

    for ing in recipe.ingredients:
        ingredient = Ingredients(
            ingredient_name=ing.ingredient_name,
            ingredient_image=ing.ingredient_image
        )
        db.add(ingredient)
        db.commit()
        new_recipe.ingredients.append(ingredient)

    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return new_recipe
