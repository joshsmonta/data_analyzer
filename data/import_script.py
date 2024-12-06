import json
from pymongo import MongoClient
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor
import time

MONGO_URI = "mongodb://root:admin@mongo:27017/"
DATABASE_NAME = "data_analyzer"
COLLECTION_NAME = "product_reviews"

def import_data(file_path: str):
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Insert data into the collection
    for record in tqdm(data, desc=f"{file_path} - Inserting Records", unit="record"):
        # MongoDB will automatically create an `_id` field for each document
        collection.insert_one({
            "product_brand": record["PRODUCT_BRAND"],
            "customer_review_rating": record["CUSTOMER_REVIEW_RATING"],
            "customer_review_title": record["CUSTOMER_REVIEW_TITLE"],
            "customer_review_desc": record["CUSTOMER_REVIEW_DESCRIPTION"],
            "child_asin": record["CHILD_ASIN"]
        })
    
    client.close()  # Close the MongoDB connection
    return f"Finished importing {file_path}"

def main():
    start_time = time.perf_counter()
    # Use ProcessPoolExecutor for parallel imports
    with ProcessPoolExecutor(max_workers=4) as executor:
        file_paths = [f"./data/reviews_part_{x+1}.json" for x in range(4)]
        results = [executor.submit(import_data, file_path) for file_path in file_paths]
        
        # Process results as they complete
        for f in results:
            print(f.result())
         
    finish_time = time.perf_counter()
    print(f'Finished in {(finish_time-start_time)} second(s)')

if __name__ == "__main__":
    main()


        
    
