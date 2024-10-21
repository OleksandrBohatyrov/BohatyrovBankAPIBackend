# User Balance Service API

## Description

This project is an API service for managing user balances. The main features include:

-   User creation
-   Viewing user balance
-   Updating user balance

## Technology Stack

-   **Django** - Backend framework
-   **Django Rest Framework (DRF)** - For creating the API
-   **drf-yasg** - For generating Swagger documentation
-   **SQLite** - Default database for Django

## Setup Instructions

To run this project on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone <repository_url>
cd user_balance_service
```

### 2. Install dependencies

Ensure that Python 3.x is installed on your system. Then run:

```bash
pip install -r requirements.txt
```

### 3. Run migrations

After installing the dependencies, apply the migrations to set up the database schema:

```bash
python manage.py migrate
```

### 4. Run the development server

Now, you can start the Django development server by running:

```bash
python manage.py runserver
```

Access the project at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Create a user

-   **Method**: POST
-   **URL**: `/balance/`
-   **Description**: Creates a new user.
-   **Request Example**:

```json
{
	"username": "john_doe",
	"password": "securepassword",
	"email": "john@example.com",
	"first_name": "John",
	"last_name": "Doe"
}
```

-   **Response Example**:

```json
{
	"id": 1,
	"username": "john_doe",
	"email": "john@example.com",
	"first_name": "John",
	"last_name": "Doe"
}
```

### 2. Retrieve user balance

-   **Method**: GET
-   **URL**: `/balance/{user_id}/`
-   **Description**: Retrieves the balance of a user by `user_id`.
-   **Response Example**:

```json
{
	"user_id": 1,
	"username": "john_doe",
	"balance": "100.00"
}
```

### 3. Update user balance

-   **Method**: PUT
-   **URL**: `/balance/{user_id}/`
-   **Description**: Updates the balance of a user.
-   **Request Example**:

```json
{
	"balance": "150.00"
}
```

-   **Response Example**:

```json
{
	"user_id": 1,
	"username": "john_doe",
	"balance": "150.00"
}
```

## Swagger Documentation

To view the Swagger documentation, open your browser and navigate to `http://127.0.0.1:8000/swagger/` after running the server. This will display the complete API documentation with interactive endpoints.

## Testing

To run tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License.
