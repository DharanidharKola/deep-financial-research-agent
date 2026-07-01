from pinecone import Pinecone

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_pinecone import (
    PineconeVectorStore
)

from backend.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

VECTOR_DB = PineconeVectorStore(
    index_name=PINECONE_INDEX,
    embedding=embeddings
)