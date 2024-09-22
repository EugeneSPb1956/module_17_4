from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)
