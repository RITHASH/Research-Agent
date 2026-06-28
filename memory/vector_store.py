import chromadb

from memory.embeddings import get_embedding_function


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./storage/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="research_memory",
            embedding_function=get_embedding_function()
        )

    def add_document(
        self,
        doc_id,
        text,
        metadata=None
    ):

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            metadatas=[metadata or {}]
        )

    def search(
        self,
        query,
        n_results=5
    ):

        return self.collection.query(
            query_texts=[query],
            n_results=n_results
        )


