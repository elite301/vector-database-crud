import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class VectorDatabase:
    def __init__(self, dim=100):
        self.collections = {}
        self.vectorizer = TfidfVectorizer(max_features=dim)
        self.dim = dim

    def create_collection(self, collection_name):
        if collection_name in self.collections:
            raise ValueError(f"Collection '{collection_name}' already exists.")
        
        index = faiss.IndexFlatL2(self.dim)
        self.collections[collection_name] = {
            'index': index,
            'documents': []
        }
    
    def get_collection(self, collection_name):
        if collection_name not in self.collections:
            raise ValueError(f"Collection '{collection_name}' does not exist.")
        return self.collections[collection_name]
    
    def _vectorize_text(self, text):
        tfidf_matrix = self.vectorizer.fit_transform([text]).toarray()
        vector = np.zeros((1, self.dim), dtype=np.float32)
        vector[0, : min(self.dim, tfidf_matrix.shape[1])] = tfidf_matrix[0, : self.dim]
        return vector

    def insert_document(self, collection_name, text):
        collection = self.get_collection(collection_name)
        documents = collection['documents']
                
        documents.append(text)
        
        collection['index'].add(self._vectorize_text(text))
        
        return len(documents) - 1
    
    def update_document(self, collection_name, doc_id, text):
        collection = self.get_collection(collection_name)
        documents = collection['documents']
        
        if doc_id < 0 or doc_id >= len(documents):
            raise ValueError("Invalid document ID")
        
        documents[doc_id] = text
        
        collection['index'].reconstruct(doc_id, self._vectorize_text(text)[0])
    
    def delete_document(self, collection_name, doc_id):
        collection = self.get_collection(collection_name)
        documents = collection['documents']
        
        if doc_id < 0 or doc_id >= len(documents):
            raise ValueError("Invalid document ID")
        
        documents.pop(doc_id)
        
        new_index = faiss.IndexFlatL2(self.dim)
        for text in documents:
            vector = self._vectorize_text(text)
            new_index.add(vector)

        collection['index'] = new_index
    
    def retrieve_documents(self, collection_name, query_text, top_n=5):
        collection = self.get_collection(collection_name)
        documents = collection['documents']
        
        if len(documents) == 0:
            return []
        
        query_vector = self._vectorize_text(query_text)
        
        distances, indices = collection['index'].search(query_vector, top_n)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(documents):
                results.append({
                    "doc_id": int(idx),
                    "text": documents[idx],
                    "distance": float(distances[0][i])
                })
        
        return results
