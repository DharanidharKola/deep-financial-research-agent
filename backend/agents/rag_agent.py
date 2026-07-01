from backend.rag.retriever import (
    retrieve_documents
)


def retrieve_context(state):

    sector = state.get(
        "sector",
        ""
    )

    query = state.get(
        "query",
        ""
    )

    print("\n")
    print("=" * 50)
    print("RAG DEBUG")
    print("=" * 50)

    print(
        f"Sector = [{sector}]"
    )

    print(
        f"Query = [{query}]"
    )

    rag_query = f"""
    Sector: {sector}

    Research Topic:
    {query}

    Focus on:

    - Financial performance
    - AI initiatives
    - Growth strategy
    - Risks
    - Opportunities
    - Future outlook
    """

    docs = retrieve_documents(
        query=rag_query,
        sector=sector,
        k=5
    )

    print(
        f"Documents Retrieved = {len(docs)}"
    )

    rag_context = []

    sources = []

    companies_seen = set()

    print("\nRetrieved Companies:")

    for doc in docs:

        print(doc.metadata)

        company = doc.metadata.get(
            "company",
            "Unknown"
        )

        if company not in companies_seen:

            companies_seen.add(
                company
            )

            rag_context.append(
                doc.page_content[:500]
            )

            sources.append({

                "company":
                doc.metadata.get(
                    "company"
                ),

                "sector":
                doc.metadata.get(
                    "sector"
                ),

                "source":
                doc.metadata.get(
                    "source"
                )

            })

    state["rag_context"] = (
        "\n\n".join(
            rag_context
        )
    )

    state["source_documents"] = (
        sources
    )

    print("\n")
    print("=" * 50)
    print("RAG SOURCES")
    print("=" * 50)

    for source in sources:

        print(
            f"{source['company']} "
            f"({source['source']})"
        )

    return state