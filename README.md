# Vector Database Operations with Flask API

This project provides a Python implementation for managing a vector database using Flask API. It supports CRUD operations on text documents stored in a vector database (like FAISS) with vectorized representations. It allows you to create collections, insert, update, delete, and retrieve documents.

## Requirements

- Python 3.x
- Flask
- scikit-learn
- FAISS
- numpy

## Install Dependencies

To install the required dependencies, run:

`pip install -r requirements.txt`

### Example `requirements.txt`:

```
faiss-cpu==1.10.0
flask==3.1.0
flask-restful==0.3.10
numpy==2.2.3
pytest==8.3.4
scikit-learn==1.6.1
```

## Usage

### Running the Flask App

1. First, make sure all dependencies are installed:

   ``` pip install -r requirements.txt ```

2. Run the Flask application:

   ``` python main.py ```

3. The application will be available at ```http://localhost:5000/```.

### API Endpoints

#### 1. Create a Collection

- **Endpoint**: ```/create_collection```
- **Method**: POST
- **Request body**:
  ```
  {
    "collection_name": "my_collection"
  }
  ```
- **Response**:
  ```
  {
    "message": "Collection 'my_collection' created successfully."
  }
  ```

#### 2. Insert a Document

- **Endpoint**: ```/insert_document```
- **Method**: POST
- **Request body**:
  ```
  {
    "collection_name": "my_collection",
    "text": "This is a sample document."
  }
  ```
- **Response**:
  ```
  {
    "message": "Document inserted with ID 0 in collection 'my_collection'."
  }
  ```

#### 3. Update a Document

- **Endpoint**: ```/update_document/<doc_id>```
- **Method**: PUT
- **Request body**:
  ```
  {
    "collection_name": "my_collection",
    "text": "This is an updated document."
  }
  ```
- **Response**:
  ```
  {
    "message": "Document 0 updated successfully in collection 'my_collection'."
  }
  ```

#### 4. Delete a Document

- **Endpoint**: ```/delete_document/<doc_id>```
- **Method**: DELETE
- **Request body**:
  ```
  {
    "collection_name": "my_collection"
  }
  ```
- **Response**:
  ```
  {
    "message": "Document 0 deleted successfully from collection 'my_collection'."
  }
  ```

#### 5. Retrieve Documents

- **Endpoint**: ```/retrieve_documents```
- **Method**: POST
- **Request body**:
  ```
  {
    "collection_name": "my_collection",
    "text": "What is vector search?",
    "top_n": 5
  }
  ```
- **Response**:
  ```
  {
    "results": [
      {
        "doc_id": 0,
        "text": "This is a sample document.",
        "distance": 0.3254
      },
      {
        "doc_id": 1,
        "text": "This is another document.",
        "distance": 0.4536
      }
    ]
  }
  ```

## Code Structure

- **```app/api.py```**: Contains the route handlers for the Flask API.
- **```app/vector_db.py```**: Contains the `VectorDatabase` class to manage FAISS index and documents.
- **```main.py```**: The entry point to start the Flask application.
- **```requirements.txt```**: List of Python dependencies required for the project.

## Tests

To run the tests using `pytest`, execute:

``` pytest ```
