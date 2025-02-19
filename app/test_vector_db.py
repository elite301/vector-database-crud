import pytest
from app.vector_db import VectorDatabase

@pytest.fixture
def db_instance():
    vector = VectorDatabase()
    vector.create_collection("test")
    return vector

def test_insert_document(db_instance):
    doc_id = db_instance.insert_document("test", "Sample document text.")
    assert doc_id == 0

def test_update_document(db_instance):
    doc_id = db_instance.insert_document("test", "Old text.")
    db_instance.update_document("test", doc_id, "Updated text.")

def test_delete_document(db_instance):
    doc_id = db_instance.insert_document("test", "To be deleted.")
    db_instance.delete_document("test", doc_id)

def test_retrieve_documents(db_instance):
    doc_id = db_instance.insert_document("test", "Relevant document for search.")
    results = db_instance.retrieve_documents("test", "search", top_n=1)
    assert len(results) == 1
    assert results[0]["doc_id"] == doc_id
    assert results[0]["text"] == "Relevant document for search."
