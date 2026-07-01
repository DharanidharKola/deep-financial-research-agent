# test_sector_rag.py

from backend.rag.retriever import (
    retrieve_documents
)

docs = retrieve_documents(
    query="AI strategy and future outlook",
    sector="Pharma",
    k=10
)

for doc in docs:
    print(
        doc.metadata.get(
            "company"
        )
    )