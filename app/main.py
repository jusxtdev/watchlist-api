from fastapi import FastAPI
from app.routers import users
from app.core.database import engine, Base, init_db
from app.models import user

app = FastAPI()

@app.on_event('startup')
def on_startup():
    init_db()

@app.get('/')
def root():
    return {
        "msg" : "Watchlist API 🍿🥤"
    }

app.include_router(users.router)