# FastAPI Patient Management API

A RESTful Patient Management API built with Python and FastAPI.

This project was developed as a hands-on learning project to understand how APIs work, how to validate request data, how CRUD operations are implemented, and how API data can be persisted using JSON.

## Features

- Create, read, update, and delete patient records
- Path parameters for individual patient operations
- Query parameters for filtering patients
- Pydantic models for request validation
- Field-level validation using Pydantic `Field`
- Duplicate patient ID validation
- HTTP exception handling
- Proper HTTP status codes
- Full updates using PUT
- Partial updates using PATCH
- JSON-based data persistence
- Interactive API documentation using Swagger UI
- Git and GitHub version control

## Tech Stack

- Python
- FastAPI
- Pydantic
- JSON
- Uvicorn
- Git
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/patients` | Get all patients |
| GET | `/patients/{patient_id}` | Get a patient by ID |
| GET | `/patients?gender=Male` | Filter patients by gender |
| GET | `/patients?admitted=true` | Filter patients by admission status |
| POST | `/patients` | Create a new patient |
| PUT | `/patients/{patient_id}` | Fully update a patient |
| PATCH | `/patients/{patient_id}` | Partially update a patient |
| DELETE | `/patients/{patient_id}` | Delete a patient |

## Data Validation

Patient data is validated using Pydantic models.

For example, the patient's age is restricted to a valid range:

```python
age: int = Field(..., ge=0, le=120)

Invalid data such as an incorrect type, missing required field, or an invalid age results in a validation error.

The API also checks for duplicate patient IDs and returns a 409 Conflict response when a duplicate ID is submitted.

Error Handling

The API uses FastAPI's HTTPException for API errors.

Examples:

404 Not Found - Patient does not exist
409 Conflict - Patient ID already exists
422 Unprocessable Entity - Request validation failed

Data Persistence

Patient records are stored in patients.json.

The application loads the data when the server starts:

patients = json.load(file)

After a successful POST, PUT, PATCH, or DELETE operation, the updated data is written back to the JSON file using:

json.dump(patients, file, indent=4)

This allows changes to remain available after restarting the server.

Project Structure
FastAPI-Learning/
│
├── main.py
├── models.py
├── patients.json
├── .gitignore
└── README.md

How to Run
1. Clone the repository
git clone https://github.com/nausheenara56-ops/FastAPI-Learning.git

2. Navigate to the project
cd FastAPI-Learning

3. Install dependencies
python -m pip install fastapi uvicorn

4. Start the server
python -m uvicorn main:app --reload

5. Open the API documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI can be used to test all API endpoints interactively.


Example Request
Create a Patient
{
  "patient_id": "P011",
  "name": "John Doe",
  "age": 35,
  "gender": "Male",
  "blood_group": "B+",
  "diagnosis": "Diabetes",
  "admitted": false
}
Partial Update

PATCH can be used when only selected fields need to be changed.

For example:

{
  "age": 36
}
What I Learned

Through this project, I practiced:

Designing REST API endpoints
Working with HTTP methods
Path and query parameters
Request body validation
Pydantic models
HTTP status codes and exception handling
CRUD operations
PUT vs PATCH
JSON data persistence
Testing APIs using Swagger UI
Git and GitHub workflow
Future Improvements

Possible future improvements include:

Database integration using SQLite/PostgreSQL
SQLAlchemy integration
Authentication and authorization
Automated API testing
Better project modularization
Dockerization
Deployment to a cloud platform
Project Status

Completed as a hands-on FastAPI learning project.

The project may be extended with database integration, testing, authentication, and deployment as part of continued learning.