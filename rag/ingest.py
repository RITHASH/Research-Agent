import uuid

from rag.document_loader import DocumentLoader
from rag.chunker import TextChunker

from memory.memory_manager import (
    MemoryManager
)


class KnowledgeIngestor:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.memory = MemoryManager()

    def ingest_document(
        self,
        file_path
    ):

        text = self.loader.load_document(
            file_path
        )

        chunks = self.chunker.chunk_text(
            text
        )

        for chunk in chunks:

            self.memory.store.add_document(
                doc_id=str(uuid.uuid4()),
                text=chunk,
                metadata={
                    "source": file_path
                }
            )

        print(
            f"Ingested {len(chunks)} chunks"
        )