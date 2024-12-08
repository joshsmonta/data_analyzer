# Define main here
from api import app
from data.import_script import process_data
from data.database import MongoDB

# Run the data import script before starting the API
@app.on_event("startup")
async def startup_event():
    print("Running data import before API startup...")
    process_data()
    print("Data import completed. Starting API...")
    MongoDB.get_instance()
    print("Start Mongo DB instance")

@app.get("/")
async def home():
    return { "message": "API is working" }