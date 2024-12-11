# Define main here
from api import app
from data.import_script import main as process_data()
from data.database import PostgresDB

# Run the data import script before starting the API
@app.on_event("startup")
async def startup_event():
    print("Running data import before API startup...")
    process_data()
    print("Data import completed. Starting API...")
    # Initialize the singleton instance
    await PostgresDB.init()
    print("Start Mongo DB instance")

@app.get("/")
async def home():
    return { "message": "API is working" }