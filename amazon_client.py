from data.database import PostgresDB
from typing import Dict, List, Optional
from fastapi.encoders import jsonable_encoder
from dataclasses import dataclass
from psycopg.rows import class_row
import asyncio

TABLE_NAME = "product_reviews"

@dataclass
class ProductReview:
    id: str
    product_brand: str
    customer_review_rating: int
    customer_review_title: str
    customer_review_desc: str
    child_asin: str

class AmazonAPIClient:
    def __init__(self, rate_limit: int = 5):
        self.rate_limit = rate_limit
        self._semaphore = asyncio.Semaphore(rate_limit)
    
    async def get_product(self, product_id: str) -> List[Dict]:
        # Get the singleton instance
        db = await PostgresDB.get_instance()

        # Get a connection from the pool
        conn = await db.get_connection()
        query = """
            SELECT * FROM product_reviews WHERE child_asin = %s;
        """
        async with conn.cursor(row_factory=class_row(ProductReview)) as cur:
            await cur.execute(query, (product_id,))
            result = await cur.fetchmany(size=100)
            return result

        # Close the connection pool when done
        await db.release_connection(conn)
        await db.close()

    async def get_products(self, page: int = 1, page_size: int = 100) -> List[Dict]:
        """
        Fetch multiple products with pagination support
        Implement pagination and rate limiting here.
        """
        # TODO: Implement batch product fetching
        async with self._semaphore:
            pass
        pass