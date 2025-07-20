from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)  
#It tells SQLAlchemy to create the database tables defined in your models (if they don’t already exist).

