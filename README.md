# FastAPI BoilerPlate Application

A robust web application built using FastAPI.

## Features

- Fast: Very high performance, on par with NodeJS and Go.
- Strongly typed requests and responses with Pydantic.
- User registration and JWT authentication.
- CRUD operations on sample data using SQL databases.
- Automatic interactive API documentation with Swagger UI.
- Asynchronous database access.
- CORS, GZip, Static Files, Streaming responses.

## Prerequisites

- Python 3.7+
- pip
- virtualenv (optional)

## Setup & Installation

1. **Clone the Repository**

```
git clone https://github.com/your_username/fastapi_sample_app.git
cd fastapi_sample_app
```

2. **Set Up a Virtual Environment (Optional but Recommended)**

```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. **Install Dependencies**
``` 
pip install -r requirements.txt 
```

4. **Environment Variables**

Copy the sample environment variables:
```
DATABASE_URL=postgresql://username:password@host/test
```

Update the `.env` file with your actual data.

5. **Initialize the Database**

```
flask db init
flask db migrate
flask db upgrade
```

6. **Run the Application**

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Navigate to [http://localhost:8000](http://localhost:8000)

## Testing

To run the tests:

```
pytest
```

