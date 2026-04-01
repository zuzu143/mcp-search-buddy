import os
import json
from typing import List, Dict

class MCPSearchBuddy:
    """
    A starter framework for a Model Context Protocol (MCP) server.
    This tool helps Claude search through local technical documentation.
    """
    def __init__(self, docs_path: str):
        self.docs_path = docs_path
        self.index = []

    def index_files(self):
        """Simulates indexing local markdown files."""
        print(f"Indexing documents in: {self.docs_path}")
        # In a real app, this would use Claude to summarize files
        self.index = ["setup.md", "api_endpoints.md", "config.json"]

    def search_query(self, query: str) -> List[str]:
        """Simple keyword search for demonstration."""
        return [doc for doc in self.index if query.lower() in doc.lower()]

if __name__ == "__main__":
    buddy = MCPSearchBuddy(docs_path="./docs")
    buddy.index_files()
    results = buddy.search_query("api")
    print(f"Search Results: {results}")
