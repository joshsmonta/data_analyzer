# Technical Interview Task: Amazon Product Performance Analyzer

## Background Context
At SellerX, we manage multiple brands and thousands of products across various Amazon marketplaces. One of our key challenges is monitoring product performance and quickly identifying issues that need attention. We'd like you to create a prototype system that could help automate this process.

## The Challenge
Design and implement a prototype system that helps our brand managers monitor product performance across our portfolio. This system should automatically collect product data, analyze customer sentiment, and provide actionable insights.

## What We're Looking For
We want to see how you approach building scalable systems and solving real business problems. There's no single "right" answer - we're interested in your thought process, engineering decisions, and how you handle trade-offs.

## Core Requirements

### 1. Data Collection
Build a system that simulates fetching product data from Amazon's API:

```python
# Example product data structure
{
    "product_id": "B07X6C9RMF",
    "title": "Premium Kitchen Knife Set",
    "price": 89.99,
    "category": "Kitchen",
    "reviews": [
        {
            "review_id": "R123ABC",
            "text": "Great quality knives, but the holder could be better",
            "rating": 4,
            "date": "2024-01-15"
        }
    ]
}
```

**Requirements:**
- Create a mock API that simulates realistic Amazon API behavior
- Handle pagination (typical page size: 100 items)
- Implement rate limiting (e.g., 5 requests per second)
- Add realistic error scenarios (timeout, server errors)

### 2. Data Analysis
Process the collected data to extract useful insights:

**Required Analysis:**
- Calculate key metrics:
  - Average rating over time
  - Review velocity (reviews per week)
  - Sentiment trends
- Use an LLM to:
  - Categorize common issues from reviews
  - Extract product feature feedback
  - Identify potential quality concerns

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

### 5. (Optional) Frontend Dashboard
Build a simple React dashboard to visualize the insights:

**Suggested Features:**
- Product overview grid
- Filtering by category/sentiment
- Basic trend visualizations
- Issue highlight cards

## Implementation Guidelines

### Technology Stack
- Backend: Python (FastAPI or Flask)
- Database: Any SQL database (PostgreSQL recommended)
- LLM Integration: OpenAI API or similar
- (Optional) Frontend: React with any UI library

### Getting Started
1. Create a mock dataset of 1000 products with realistic data
2. Implement the core data collection and processing pipeline
3. Add the API layer
4. (Optional) Build the frontend

## Evaluation Criteria

### 1. Code Quality (30%)
- Clean, readable code structure
- Proper error handling
- Good documentation
- Type hints and validation

### 2. System Design (30%)
- Scalable architecture
- Efficient data processing
- Proper separation of concerns
- Production-ready considerations

### 3. Data Processing & AI Integration (20%)
- Effective use of LLMs
- Efficient data processing
- Meaningful insights extraction
- Error handling for AI components

### 4. Problem Solving (20%)
- Creative solutions
- Performance optimization
- Edge case handling
- Business value focus

## Bonus Points For:
- Docker configuration
- Unit tests
- Performance optimization
- Monitoring setup
- CI/CD considerations

## Time Expectation
- Core Implementation: 2-3 hours
- Optional Frontend: 1-2 additional hours

## Submission Guidelines
1. Share your code via a private GitHub repository
2. Include a README with:
   - Setup instructions
   - Architecture overview
   - Key decisions and trade-offs
   - Future improvements
3. Be prepared to discuss your implementation in detail

## Questions?
Feel free to ask for clarification on any aspects of the task. We want you to have a clear understanding of the requirements while leaving room for creativity in the implementation.

## Note on Production Readiness
While this is a prototype, please include comments or documentation about how you would enhance the system for production use, considering aspects like:
- Scaling to handle larger datasets
- Monitoring and alerting
- Security considerations
- Performance optimization
