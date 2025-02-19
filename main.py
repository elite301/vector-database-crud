from flask import Flask
from app.api import create_collection, insert_document, update_document, delete_document, retrieve_documents
from app.vector_db import VectorDatabase

app = Flask(__name__)

vector_db = VectorDatabase()

app.add_url_rule('/create_collection', 'create_collection', create_collection, methods=['POST'])
app.add_url_rule('/insert_document', 'insert_document', insert_document, methods=['POST'])
app.add_url_rule('/update_document/<int:doc_id>', 'update_document', update_document, methods=['PUT'])
app.add_url_rule('/delete_document/<int:doc_id>', 'delete_document', delete_document, methods=['DELETE'])
app.add_url_rule('/retrieve_documents', 'retrieve_documents', retrieve_documents, methods=['POST'])

if __name__ == '__main__':
    app.run()
