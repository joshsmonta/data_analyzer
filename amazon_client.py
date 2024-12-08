from data.database import MongoDB
from typing import Dict, List, Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import asyncio

COLLECTION_NAME = "product_reviews"
class ProductReviewResponse(BaseModel):
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
        mongo_instance = MongoDB.get_instance()
        result = mongo_instance.get_collection(COLLECTION_NAME).find({"child_asin": product_id})
        print(result)
        return {"result": result}
        

    async def get_products(self, page: int = 1, page_size: int = 100) -> List[Dict]:
        """
        Fetch multiple products with pagination support
        Implement pagination and rate limiting here.
        """
        # TODO: Implement batch product fetching
        async with self._semaphore:
            pass
        pass