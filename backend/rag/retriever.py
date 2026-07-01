from backend.rag.vector_store import (
    VECTOR_DB
)


def retrieve_documents(
    query,
    sector=None,
    k=5
):

    if sector:

        return VECTOR_DB.similarity_search(
            query,
            k=k,
            filter={
                "sector": sector
            }
        )

    return VECTOR_DB.similarity_search(
        query,
        k=k
    )