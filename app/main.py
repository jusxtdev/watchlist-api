from fastapi import FastAPI
from app.routers import users, media
from app.core.database import init_db

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
app.include_router(media.router)