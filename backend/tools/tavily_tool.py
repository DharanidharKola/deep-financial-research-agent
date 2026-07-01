from tavily import TavilyClient

from backend.config import TAVILY_API_KEY

client = TavilyClient(
    api_key=TAVILY_API_KEY
)

def web_search(query: str):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response