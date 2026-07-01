from backend.rag.retriever import retrieve_documents

docs = retrieve_documents(
    "Infosys AI investments"
)

for i, doc in enumerate(docs):

    print("\n" + "=" * 50)

    print(f"DOCUMENT {i+1}")

    print("\nMETADATA:")
    print(doc.metadata)

    print("\nCONTENT:")
    print(doc.page_content[:300])