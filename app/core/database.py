from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.settings import settings

DATABASE_URL = settings.database_url

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()