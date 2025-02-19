import pytest
from app.vector_db import VectorDatabase

@pytest.fixture
def db_instance():
    return VectorDatabase()

def test_insert_document(db_instance):
    doc_id = db_instance.insert_document("Sample document text.")
    assert doc_id == 0  # First document

def test_update_document(db_instance):
    doc_id = db_instance.insert_document("Old text.")
    db_instance.update_document(doc_id, "Updated text.")
    assert db_instance.id_map[doc_id] == "Updated text."

def test_delete_document(db_instance):
    doc_id = db_instance.insert_document("To be deleted.")
    db_instance.delete_document(doc_id)
    assert doc_id not in db_instance.id_map

def test_retrieve_documents(db_instance):
    doc_id = db_instance.insert_document("Relevant document for search.")
    results = db_instance.retrieve_documents("search", top_n=1)
    assert len(results) == 1
    assert results[0]["doc_id"] == doc_id
    assert results[0]["text"] == "Relevant document for search."
