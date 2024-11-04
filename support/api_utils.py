import requests
from deepdiff import DeepDiff
import json

class ApiUtils:
    BASE_URL = "https://poetrydb.org"

    def get_random_poem(self):
        """Fetch a random poem from PoetryDB."""
        return requests.get(f"{self.BASE_URL}/random")

    def get_authors_list(self):
        """Fetch a list of authors from PoetryDB."""
        return requests.get(f"{self.BASE_URL}/author")

    def get_poems_by_author(self, author):
        """Fetch poems by a specified author from PoetryDB."""
        return requests.get(f"{self.BASE_URL}/author/{author}")

    def get_author_titles_list(self, author):
        """Fetch a list of titles for a specific author from PoetryDB."""
        return requests.get(f"{self.BASE_URL}/author/{author}/title")

    def compare_results(self, expected_results_filename, actual_results, ignore_list=None, report_repetition=True, ignore_order=True):
        """Compare the response text with the expected text."""
        if ignore_list is None:
            ignore_list = []

        with open(f"expected_results/{expected_results_filename}", "r", encoding='utf-8') as f:
            expected_results = f.read()

        diff = DeepDiff(json.loads(expected_results), json.loads(actual_results), exclude_paths=ignore_list, ignore_order=ignore_order,
                        report_repetition=report_repetition)

        if diff:
            return f"Differences found: {diff}"
        else:
            return "No differences found."
