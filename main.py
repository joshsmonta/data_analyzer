# Define main here
from api import app

@app.get("/")
async def home():
    return { "message": "Working" }