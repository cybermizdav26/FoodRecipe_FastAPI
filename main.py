from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.routers.recipes import router as recipe_router
from app.routers.users import router as user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str


app.include_router(user_router)
app.include_router(recipe_router)

