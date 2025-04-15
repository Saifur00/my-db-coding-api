from fastapi import FastAPI
from app import models
from app.database import engine

app = FastAPI()

# Create all tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Bug Tracker API is running!"}
