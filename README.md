# Calculator App

A simple calculator application that exposes basic mathematical operations via HTTP endpoints, running on Nginx port 80.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- RESTful API endpoints
- Web interface for API documentation
- Containerized with Docker and Nginx
- Health check endpoint for monitoring
- Security headers for enhanced protection
- Non-root user execution for improved security

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Installation and Running

1. Clone this repository:
   ```
   git clone <repository-url>
   cd calculator-app
   ```

2. Build and run the Docker container:
   ```
   docker-compose up -d
   ```

3. The calculator app is now running on http://localhost:80

## API Usage

The calculator app provides the following API endpoints:

### Health Check

```
GET /health
```

Response:
```json
{
    "status": "healthy",
    "timestamp": "2023-07-01T12:34:56.789012",
    "version": "1.0.0"
}
```

### Addition

```
POST /api/add
Content-Type: application/json

{
    "a": 10,
    "b": 5
}
```

Response:
```json
{
    "result": 15
}
```

### Subtraction

```
POST /api/subtract
Content-Type: application/json

{
    "a": 10,
    "b": 5
}
```

Response:
```json
{
    "result": 5
}
```

### Multiplication

```
POST /api/multiply
Content-Type: application/json

{
    "a": 10,
    "b": 5
}
```

Response:
```json
{
    "result": 50
}
```

### Division

```
POST /api/divide
Content-Type: application/json

{
    "a": 10,
    "b": 5
}
```

Response:
```json
{
    "result": 2.0
}
```

## Example Usage with curl

```bash
# Health Check
curl -X GET http://localhost/health

# Addition
curl -X POST http://localhost/api/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'

# Subtraction
curl -X POST http://localhost/api/subtract \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'

# Multiplication
curl -X POST http://localhost/api/multiply \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'

# Division
curl -X POST http://localhost/api/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
```

## Running Without Docker

If you prefer to run the application without Docker:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install and configure Nginx:
   - Copy the nginx.conf file to your Nginx configuration directory
   - Restart Nginx

3. Run the Flask application:
   ```
   gunicorn --bind 127.0.0.1:5000 app:app
   ```

## Development

### Running Tests

To run the tests for the calculator functions:

```
python -m unittest test_calculator.py
```