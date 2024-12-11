from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from amazon_client import AmazonAPIClient, ProductReview

app = FastAPI(title="Amazon Product Intelligence")
amazon_api = AmazonAPIClient(rate_limit=10)

@app.get("/api/v1/products/{product_id}/insights")
async def get_product_insights(product_id: str):
    cursor = await amazon_api.get_product(product_id)
    return cursor
    # results = [
    #     ProductReview(
    #         product_brand=row.get("product_brand", "Unknown"),
    #         customer_review_rating=row.get("customer_review_rating", 0),
    #         customer_review_title=row.get("customer_review_title", "No Title"),
    #         customer_review_desc=row.get("customer_review_desc", "No Description"),
    #         child_asin=row.get("child_asin", "Unknown")
    #     )
    #     for row in cursor["result"]
    # ]

@app.get("/api/v1/products")
async def get_products(page: int = 1, page_size: int = 50):
    """
    Get all products with pagination
    """
    # TODO: Implement product listing
    pass