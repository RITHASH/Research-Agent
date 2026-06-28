from memory.memory_manager import MemoryManager


class Retriever:

    def __init__(self):

        self.memory = MemoryManager()

    def retrieve_context(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.memory.retrieve(query)

        context_chunks = []

        documents = results.get("documents", [])

        if documents:

            for doc in documents[0][:top_k]:

                context_chunks.append(doc)

        return context_chunks