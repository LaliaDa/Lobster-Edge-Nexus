from qdrant_client import QdrantClient
from qdrant_client.http import models

class NexusVectorStore:
    def __init__(self, host="localhost", port=6333):
        self.client = QdrantClient(host=host, port=port)

    def create_nexus_collection(self, collection_name, vector_size):
   
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
            hnsw_config=models.HnswConfigDiff(on_disk=False) 
        print(f"Collection {collection_name} created with in-memory optimization.")