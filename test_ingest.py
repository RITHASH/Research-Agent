# from rag.ingest import KnowledgeIngestor


# def main():

#     ingestor = KnowledgeIngestor()

#     ingestor.ingest_document(
#         "knowledge/docs/test.txt"
#     )


# if __name__ == "__main__":
#     main()

from rag.ingest import KnowledgeIngestor


def main():

    ingestor = KnowledgeIngestor()

    ingestor.ingest_document(
        "knowledge/docs/test.txt"
    )


if __name__ == "__main__":
    main()
    