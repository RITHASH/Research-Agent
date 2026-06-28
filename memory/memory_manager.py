import uuid

from memory.vector_store import VectorStore


class MemoryManager:

    def __init__(self):

        self.store = VectorStore()

    def save_research(
        self,
        topic,
        content
    ):

        self.store.add_document(
            doc_id=str(uuid.uuid4()),
            text=content,
            metadata={
                "topic": topic
            }
        )

    def retrieve(
        self,
        query
    ):

        return self.store.search(
            query=query,
            n_results=5
        )