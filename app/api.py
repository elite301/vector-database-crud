from flask import request, jsonify
from app.vector_db import VectorDatabase
from sklearn.feature_extraction.text import TfidfVectorizer

vector_db = VectorDatabase()

def create_collection():
    data = request.get_json()
    collection_name = data.get("collection_name")
    
    if not collection_name:
        return jsonify({"error": "collection_name is required"}), 400
    
    try:
        vector_db.create_collection(collection_name)
        return jsonify({"message": f"Collection '{collection_name}' created successfully."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def insert_document():
    data = request.get_json()
    collection_name = data.get("collection_name")
    text = data.get("text")
    
    if not collection_name or not text:
        return jsonify({"error": "collection_name and text are required"}), 400
    
    try:
        doc_id = vector_db.insert_document(collection_name, text)
        return jsonify({"message": f"Document inserted with ID {doc_id} in collection '{collection_name}'."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def update_document(doc_id):
    data = request.get_json()
    collection_name = data.get("collection_name")
    text = data.get("text")
    
    if not collection_name or not text:
        return jsonify({"error": "collection_name and text are required"}), 400
    
    try:
        vector_db.update_document(collection_name, doc_id, text)
        return jsonify({"message": f"Document {doc_id} updated successfully in collection '{collection_name}'."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def delete_document(doc_id):
    data = request.get_json()
    collection_name = data.get("collection_name")
    
    if not collection_name:
        return jsonify({"error": "collection_name is required"}), 400
    
    try:
        vector_db.delete_document(collection_name, doc_id)
        return jsonify({"message": f"Document {doc_id} deleted successfully from collection '{collection_name}'."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def retrieve_documents():
    data = request.get_json()
    collection_name = data.get("collection_name")
    query_text = data.get("text")
    top_n = data.get("top_n", 5)
    
    if not collection_name or not query_text:
        return jsonify({"error": "collection_name and query text are required"}), 400
    
    try:
        results = vector_db.retrieve_documents(collection_name, query_text, top_n)
        return jsonify({"results": results})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
