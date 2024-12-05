import json
import sqlite3
import asyncio
import time

async def import_data(file_path: str, cursor, connection):
    with open(file_path, "r") as f:
        data = json.load(f)
    for record in data:
        cursor.execute("""
        INSERT INTO product_reviews (
            product_brand,
            customer_review_rating,
            customer_review_title,
            customer_review_desc,
            child_asin
        ) VALUES (?, ?, ?, ?, ?)
        """, (
            record["PRODUCT_BRAND"], 
            record["CUSTOMER_REVIEW_RATING"], 
            record["CUSTOMER_REVIEW_TITLE"], 
            record["CUSTOMER_REVIEW_DESCRIPTION"],
            record["CHILD_ASIN"]
        ))
        connection.commit()
    return f"finished importing {file_path}"

async def main():
    start_time = time.perf_counter()
    connection = sqlite3.connect('./data/db.sqlite3')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_reviews (
            product_brand VARCHAR,
            customer_review_rating INTEGER,
            customer_review_title VARCHAR,
            customer_review_desc TEXT,
            child_asin VARCHAR
        )
    """)
    connection.commit()
    await asyncio.gather(
        import_data("./data/reviews_part_1.json", cursor, connection),
        import_data("./data/reviews_part_2.json", cursor, connection),
        import_data("./data/reviews_part_3.json", cursor, connection),
        import_data("./data/reviews_part_4.json", cursor, connection)
    )
    connection.close()
    finish_time = time.perf_counter()
    print(f'Finished in {(finish_time-start_time)} second(s)')
    
asyncio.run(main())

        
    
