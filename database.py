from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:123@localhost:5432/notes_db')
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()