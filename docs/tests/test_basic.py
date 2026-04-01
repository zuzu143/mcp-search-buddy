import unittest
from main import MCPSearchBuddy

class TestSearchBuddy(unittest.TestCase):
    def test_indexing(self):
        buddy = MCPSearchBuddy(docs_path="./docs")
        buddy.index_files()
        self.assertIn("api_endpoints.md", buddy.index)

    def test_search(self):
        buddy = MCPSearchBuddy(docs_path="./docs")
        buddy.index_files()
        results = buddy.search_query("api")
        self.assertTrue(len(results) > 0)

if __name__ == "__main__":
    unittest.main()
