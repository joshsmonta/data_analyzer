# Technical Interview Task: Amazon Product Performance Analyzer

## Background Context
At SellerX, we manage multiple brands and thousands of products across various Amazon marketplaces. One of our key challenges is monitoring product performance and quickly identifying issues that need attention. We'd like you to create a prototype system that could help automate this process.

## The Challenge
Design and implement a prototype system that helps our brand managers monitor product performance across our portfolio. This system should automatically collect product data, analyze customer sentiment, and provide actionable insights.

## What We're Looking For
We want to see how you approach building scalable systems and solving real business problems. There's no single "right" answer - we're interested in your thought process, engineering decisions, and how you handle trade-offs.

## Core Requirements

### 1. Data Collection
Load product data from provided JSON files containing information about products and their associated reviews.

```
{
        "PRODUCT_BRAND": "Rhino USA",
        "CUSTOMER_REVIEW_RATING": 5,
        "CUSTOMER_REVIEW_TITLE": "Good option for portable potty",
        "CUSTOMER_REVIEW_DESCRIPTION": "Ordered for a camping \"cassette\" style Bathroom set up. Works well, Good quality for the price.",
        "CHILD_ASIN": "B0BTTL9LTC"
    },
```

### 2. Data Analysis
Process the collected data and use LLMs to extract useful insights, such as:
    - Most common issues (e.g., extracted from review text) to extract useful insights.
    - Number of reviews per product.
    - Percentage of positive/negative reviews.
You will be provided with an OpenAI API key for this purpose.


### 3. Data Storage
Design a database schema that efficiently stores and retrieves insights:

**Key Considerations:**
- Store raw data and processed insights separately
- Enable efficient querying for dashboards
- Support historical trend analysis
- Handle updates without data loss

### 4. API Design
Create endpoints that serve the processed insights:

**Required Endpoints:**
- GET /api/v1/products
  - List all products with summarized insights
  - Support filtering and pagination
- GET /api/v1/products/{product_id}
  - Detailed insights for a specific product
  - Include historical trends

### 5. (Bonus) 

5.1 Frontend Dashboard: Build a simple React dashboard to visualize the insights:

**Suggested Features:**
- Product overview grid
- Filtering by category/sentiment
- Basic trend visualizations
- Issue highlight cards


5.2 While this is a prototype, please include comments or documentation about how you would enhance the system for production use, considering aspects like:
- Docker configuration
- Unit tests
- Performance optimization
- Monitoring setup
- CI/CD considerations


## Implementation Guidelines

### Technology Stack
- Backend: Python (e.g., FastAPI)
- Database: Any SQL database (e.g., SQLite)
- LLM Integration: OpenAI API
- (Optional) Frontend: React with any UI library

### Getting Started
1. Create a mock dataset 
2. Implement the core data collection and processing pipeline
3. Add the API layer
4. (Optional) Build the frontend


## Submission Guidelines
1. Share your code via this GitHub repository
2. Include a README with:
   - Setup instructions
   - Architecture overview
   - Key decisions and trade-offs
   - Future improvements
3. Be prepared to discuss your implementation in detail

## Questions?
Feel free to ask for clarification on any aspects of the task. We want you to have a clear understanding of the requirements while leaving room for creativity in the implementation.
