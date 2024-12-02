from typing import Dict, List, Optional
import asyncio

class AmazonAPIClient:
    def __init__(self, rate_limit: int = 5):
        self.rate_limit = rate_limit
        self._semaphore = asyncio.Semaphore(rate_limit)
    
    async def get_product(self, product_id: str) -> Dict:
        """
        Fetch a single product by ID.
        Implement pagination and rate limiting here.
        """
        # TODO: Implement product fetching logic
        pass

    async def get_products(self, page: int = 1, page_size: int = 100) -> List[Dict]:
        """
        Fetch multiple products with pagination support
        """
        # TODO: Implement batch product fetching
        pass