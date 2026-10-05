from langchain_groq import ChatGroq

from backend.config import (
    GROQ_API_KEY
)

llm = ChatGroq(

    model="openai/gpt-oss-20b",

    api_key=GROQ_API_KEY,

    temperature=0
)

#from langchain_openai import ChatOpenAI

#from backend.config import (
#    OPENROUTER_API_KEY,
#    MODEL_NAME
#)

#llm = ChatOpenAI(
#    model="mistralai/mistral-7b-instruct:free",
#    api_key=OPENROUTER_API_KEY,
#    base_url="https://openrouter.ai/api/v1",
#    max_tokens=512,
#    temperature=0
#)