from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./watchlist.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()