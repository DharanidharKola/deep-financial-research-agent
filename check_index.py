# check_index.py

from backend.rag.vector_store import VECTOR_DB

docs = VECTOR_DB.similarity_search(
    "annual report",
    k=50
)

companies = set()

for doc in docs:
    companies.add(
        doc.metadata.get(
            "company"
        )
    )

print(companies)