from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME"
)

PINECONE_API_KEY = os.getenv(
    "PINECONE_API_KEY"
)

PINECONE_INDEX = os.getenv(
    "PINECONE_INDEX"
)