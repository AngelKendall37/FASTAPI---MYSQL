from fastapi import FastAPI
from routers.user import user


app = FastAPI()
app.include_router(user)
posts = []

