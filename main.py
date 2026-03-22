from database import engine, Base
from models import User, Note


#this creates the table from models.py
Base.metadata.create_all(bind=engine)