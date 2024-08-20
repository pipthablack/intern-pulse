
# Flask API Documentation

## Overview

This documentation outlines the API endpoints for managing users, including the expected request and response formats, error handling, and instructions on how to run the API locally.

## Base URL

All API requests should be made to the following base URL:

```
http://localhost:5000/api
```

## Endpoints

### 1. Create a User

**Endpoint:** `/users`

**Method:** `POST`

**Description:** Creates a new user with the provided name.

**Request Format:**

- `Content-Type`: `application/json`
- **Body:**

  ```json
  {
    "name": "John Doe"
  }
  ```

**Response Format:**

- **Success (201 Created):**

  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

- **Error (400 Bad Request):**

  ```json
  {
    "error": "Invalid data"
  }
  ```

### 2. Get User by ID

**Endpoint:** `/users/<id>`

**Method:** `GET`

**Description:** Retrieves a user by their ID.

**Request Format:** N/A

**Response Format:**

- **Success (200 OK):**

  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

### 3. Get User by Name

**Endpoint:** `/users/by_name/<name>`

**Method:** `GET`

**Description:** Retrieves a user by their name.

**Request Format:** N/A

**Response Format:**

- **Success (200 OK):**

  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

### 4. Update User by ID

**Endpoint:** `/users/<id>`

**Method:** `PUT`

**Description:** Updates the name of an existing user identified by their ID.

**Request Format:**

- `Content-Type`: `application/json`
- **Body:**

  ```json
  {
    "name": "Jane Doe"
  }
  ```

**Response Format:**

- **Success (200 OK):**

  ```json
  {
    "id": 1,
    "name": "Jane Doe"
  }
  ```

- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

### 5. Update User by Name

**Endpoint:** `/users/by_name/<name>`

**Method:** `PUT`

**Description:** Updates the name of an existing user identified by their name.

**Request Format:**

- `Content-Type`: `application/json`
- **Body:**

  ```json
  {
    "name": "Jane Smith"
  }
  ```

**Response Format:**

- **Success (200 OK):**

  ```json
  {
    "id": 1,
    "name": "Jane Smith"
  }
  ```

- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

### 6. Delete User by ID

**Endpoint:** `/users/<id>`

**Method:** `DELETE`

**Description:** Deletes an existing user identified by their ID.

**Request Format:** N/A

**Response Format:**

- **Success (204 No Content):** No body
- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

### 7. Delete User by Name

**Endpoint:** `/users/by_name/<name>`

**Method:** `DELETE`

**Description:** Deletes an existing user identified by their name.

**Request Format:** N/A

**Response Format:**

- **Success (204 No Content):** No body
- **Error (404 Not Found):**

  ```json
  {
    "error": "User not found"
  }
  ```

## Error Handling

- **400 Bad Request:** The server could not understand the request due to invalid syntax.
- **404 Not Found:** The requested resource could not be found.
- **500 Internal Server Error:** The server encountered an unexpected condition.

## Running the API Locally

To run the API locally, follow these steps:

1. **Clone the Repository:**

   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set Up a Virtual Environment:**

   ```
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
   ```

3. **Install Dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```
   export FLASK_APP=app.py        # On macOS/Linux
   export FLASK_ENV=development   # On macOS/Linux
   flask run                      # On macOS/Linux
   ```

   Or on Windows:

   ```
   set FLASK_APP=app.py           # On Windows
   set FLASK_ENV=development      # On Windows
   flask run                      # On Windows
   ```

The application will be running on [http://localhost:5000](http://localhost:5000).

```

This update adds the functionality to create, read, update, and delete users based on their name, in addition to their ID, providing more flexibility in accessing and modifying user data.
