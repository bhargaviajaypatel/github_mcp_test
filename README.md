# Simple FastAPI

A simple RESTful API built with FastAPI that manages a collection of items.

## Features

- RESTful API with CRUD operations for items
- Automatic API documentation with Swagger UI
- Data validation with Pydantic models

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhargaviajaypatel/github_mcp_test.git
cd github_mcp_test
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the application with:

```bash
python main.py
```

Or directly with uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | / | Welcome message |
| GET | /items | List all items |
| GET | /items/{item_id} | Get a specific item |
| POST | /items | Create a new item |
| PUT | /items/{item_id} | Update an existing item |
| DELETE | /items/{item_id} | Delete an item |

## Example Usage

### Create an item

```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Example Item", "description": "This is an example", "price": 42.99}'
```

### Get all items

```bash
curl -X GET "http://localhost:8000/items"
```

## License

MIT