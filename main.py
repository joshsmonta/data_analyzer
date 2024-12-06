# Define main here
from api import app
from data.import_script import main as import_all_data

# Run the data import script before starting the API
@app.on_event("startup")
async def startup_event():
    print("Running data import before API startup...")
    import_all_data()
    print("Data import completed. Starting API...")

@app.get("/")
async def home():
    return { "message": "API is working" }