from fastapi import FastAPI
from app.routers import users

app = FastAPI()

@app.get('/')
def root():
    return {
        "msg" : "Watchlist API 🍿🥤"
    }

app.include_router(users.router)