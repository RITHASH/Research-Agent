from tavily import TavilyClient

from config import TAVILY_API_KEY


class WebSearchTool:

    def __init__(self):

        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def search(
        self,
        query: str,
        max_results: int = 5
    ):

        response = self.client.search(
            query=query,
            max_results=max_results
        )

        return response.get("results", [])

