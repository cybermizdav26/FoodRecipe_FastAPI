from fastapi import FastAPI

from app.routers.users import router as user_router
from app.routers.recipes import router as recipe_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(user_router)
app.include_router(recipe_router)

