import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship

from sql_app.database import Base, engine


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Ingredients(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    ingredient_name = Column(String, nullable=False)
    recipes = relationship("Recipe", secondary="recipe_ingredients_association", back_populates="ingredients")

    def __repr__(self):
        return self.ingredient_name


recipe_ingredients_association = Table(
    'recipe_ingredients_association',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    title = Column(String(100), nullable=False)
    tags_id = Column(Integer, )
    time_minutes = Column(Integer, nullable=False)
    ingredients = relationship("Ingredients", secondary=recipe_ingredients_association, back_populates="recipes")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return self.title


class RecipeRate(Base):
    __tablename__ = "recipe_rates"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    rate = Column(Integer, nullable=False)


class RecipePreparation(Base):
    __tablename__ = "recipe_preparations"
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    step = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

    def __repr__(self):
        return self.recipe_id


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return self.content


class CommentLike(Base):
    __tablename__ = "comment_likes"
    id = Column(Integer, primary_key=True, index=True)
    comment_id = Column(Integer, ForeignKey("comments.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    like = Column(Boolean, default=False)
    dislike = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return self.user_id


Base.metadata.create_all(bind=engine)