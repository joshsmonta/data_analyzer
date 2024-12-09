import json
import glob
import os
from psycopg import Connection, conninfo
from concurrent.futures import ProcessPoolExecutor
import time

TABLE_NAME = "product_reviews"

conn_str = conninfo.make_conninfo(
    host="127.0.0.1", 
    port=5432, 
    dbname="data_analyzer", 
    user="postgres",
    password="admin"
)

def import_data(file_path: str):
    with Connection.connect(conninfo="postgresql://postgres:admin@postgres:5432/data_analyzer") as conn:
        with conn.cursor() as cursor:
            # Ensure the table exists
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id SERIAL PRIMARY KEY,
                product_brand VARCHAR(255),
                customer_review_rating INTEGER,
                customer_review_title TEXT,
                customer_review_desc TEXT,
                child_asin VARCHAR(255)
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
        
            with open(file_path, "r") as f:
                data = json.load(f)
            insert_query = f"""
            INSERT INTO {TABLE_NAME} (
                product_brand, customer_review_rating, customer_review_title, customer_review_desc, child_asin
            ) VALUES (%s, %s, %s, %s, %s);
            """
            for record in data:
                cursor.execute(insert_query, (
                    record["PRODUCT_BRAND"],
                    record["CUSTOMER_REVIEW_RATING"],
                    record["CUSTOMER_REVIEW_TITLE"],
                    record["CUSTOMER_REVIEW_DESCRIPTION"],
                    record["CHILD_ASIN"]
                ))
                conn.commit()

            cursor.close()
            conn.close()
    return f"Finished importing {file_path}"

def process_data():
    start_time = time.perf_counter()
    # Dynamically find all JSON files in the "raw_data" folder
    file_paths = glob.glob(os.path.join("./data/raw_data", "*.json"))

    if not file_paths:
        print(file_paths[0])
        print("No JSON files found in the 'raw_data' folder.")
        return

    print(f"Found {len(file_paths)} JSON files to process.")
    # Use ProcessPoolExecutor for parallel imports
    import_data("./data/raw_data/reviews_part_1.json")
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     results = [executor.submit(import_data, file_path) for file_path in file_paths]
        
    #     # Process results as they complete
    #     for f in results:
    #         print(f.result())
         
    finish_time = time.perf_counter()
    print(f'Finished in {(finish_time-start_time)} second(s)')

if __name__ == "__main__":
    process_data()


        
    
