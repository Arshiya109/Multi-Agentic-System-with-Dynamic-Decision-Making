import requests

class ArxivAgent:
    def search(self, query):
        url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": query,
            "start": 0,
            "max_results": 3
        }
        response = requests.get(url, params=params)
        return "Fetched 3 recent papers related to query."
