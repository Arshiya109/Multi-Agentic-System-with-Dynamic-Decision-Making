import requests
import os

class WebSearchAgent:
    def __init__(self):
        self.api_key = os.getenv("8f35062c16178432f8518bbfefe75d59319d9c35616a3d3d243c3e85daeb3a08")  # Set environment variable
    
    def search(self, query):
        # Use SerpAPI or alternative
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": 3
        }
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json()
        # Parse results
        snippets = [res['snippet'] for res in results.get('organic_results', [])]
        return "Top snippets: " + " | ".join(snippets)
