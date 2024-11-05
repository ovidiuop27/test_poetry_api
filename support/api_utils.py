import requests
from deepdiff import DeepDiff
import json
import os
from datetime import datetime

class ApiUtils:
    BASE_URL = "https://poetrydb.org"
    compared_results_path = "compared_results"

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
        """Compare the response text with the expected text and save the diff to a JSON file if differences are found."""
        if ignore_list is None:
            ignore_list = []

        try:
            with open(f"expected_results/{expected_results_filename}", "r", encoding='utf-8') as f:
                expected_results = f.read()
        except FileNotFoundError:
            return f"Expected results file '{expected_results_filename}' not found."

        diff = DeepDiff(
            json.loads(expected_results),
            json.loads(actual_results),
            exclude_paths=ignore_list,
            ignore_order=ignore_order,
            report_repetition=report_repetition
        )

        # If no differences, return a message
        if not diff:
            return "No differences found."

        # If differences found, create the JSON file
        timestamp = datetime.now().strftime("%m%d%Y_%H%M%S")
        diff_filename = f"{expected_results_filename.split('.')[0]}_{timestamp}.json"
        diff_filepath = os.path.join(self.compared_results_path, diff_filename)

        # Ensure the compared_results directory exists
        os.makedirs(self.compared_results_path, exist_ok=True)

        # Write the diff to the json file in pretty-print format
        with open(diff_filepath, "w", encoding='utf-8') as f:
            json.dump(diff, f, indent=4)

        return f"Differences found: {diff}"
