# Weight Converter Backend API

This is a Flask-based REST API that converts weight between pounds and kilograms. It's built from the original CLI weight checker application.

## Features

- Convert weight between pounds and kilograms
- Input validation for weight and units
- JSON API responses
- CORS enabled for frontend integration
- Error handling and user-friendly messages

## Setup and Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET `/`
Health check endpoint that returns API information.

**Response:**
```json
{
  "message": "Weight Converter API is running!",
  "version": "1.0.0",
  "endpoints": {
    "convert": "/api/convert (POST)",
    "health": "/ (GET)"
  }
}
```

### POST `/api/convert`
Convert weight between pounds and kilograms.

**Request Body:**
```json
{
  "name": "John Doe",
  "weight": 150,
  "unit": "p"
}
```

**Parameters:**
- `name` (string, required): User's name
- `weight` (number, required): Weight value (0.1 - 1000)
- `unit` (string, required): Unit of measurement
  - `"p"` or `"pounds"` for pounds
  - `"k"` or `"kilograms"` for kilograms

**Success Response (200):**
```json
{
  "user": "John Doe",
  "conversion": {
    "original_weight": 150,
    "original_unit": "pounds",
    "converted_weight": 68.04,
    "converted_unit": "kilograms"
  },
  "message": "Hi John Doe! Your weight has been successfully converted."
}
```

**Error Response (400):**
```json
{
  "error": "Weight must be a positive number"
}
```

### GET `/api/health`
Detailed health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Weight Converter API",
  "timestamp": "2025-07-02"
}
```

## Frontend

Open `index.html` in your browser to use the web interface. Make sure the API server is running first.

## Testing with curl

### Convert pounds to kilograms:
```bash
curl -X POST http://localhost:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "weight": 150, "unit": "p"}'
```

### Convert kilograms to pounds:
```bash
curl -X POST http://localhost:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane", "weight": 70, "unit": "k"}'
```

## Error Handling

The API validates all inputs and returns appropriate error messages:

- Empty or missing name
- Invalid weight (non-numeric, negative, or > 1000)
- Invalid unit (not p/k/pounds/kilograms)
- Missing required fields

## Development

The API is built with:
- Flask (web framework)
- Flask-CORS (cross-origin requests)
- JSON responses
- Input validation
- Error handling

## Original CLI Version

The original CLI version is still available in `weightchecker.py`.
