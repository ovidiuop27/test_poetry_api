# PoetryDB API Testing Project

This repository contains a test suite for the PoetryDB API, using Behavior-Driven Development (BDD) to verify various endpoints.
The tests are written with pytest and pytest-bdd, and they validate API responses against expected data using DeepDiff.
Any discrepancies between the actual and expected responses are logged in a timestamped JSON file in a compared_results directory.

## Project Structure:
.
├── expected_results/                 # Contains JSON files with expected API responses
│   ├── aly_levy_expected.json
│   ├── george_herbert_expected.json
│   └── ...                           # Other expected result files
├── compared_results/                 # Stores JSON files of any response mismatches found
├── features/
│   └── poetry_api.feature            # Feature file containing BDD scenarios for the PoetryDB API
├── support/
│   └── api_utils.py                  # Helper class with methods to interact with the PoetryDB API
└── tests/
    └── test_poetry_api.py            # Test file with step definitions for the feature scenarios


## Prerequisites
Python 3.x
PoetryDB API running or accessible online.

## Install Dependencies
bash: pip install -r requirements.txt

## Dependencies Used
	- pytest: For running tests.
	- pytest-bdd: For behavior-driven testing with Gherkin syntax.
	- requests: For making HTTP requests to the PoetryDB API.
	- deepdiff: For comparing API responses against expected results.

## Running Tests
bash: pytest -v
You should see output indicating which tests have passed or failed, along with any differences found between actual and expected results.

## Test Cases
The test suite includes the following scenarios:

Fetch a Random Poem
	Given the PoetryDB API is available
	When I request a random poem
	Then I should receive a poem with a title and author
	Fetch Poems by Author

Given the PoetryDB API is available
	When I request poems by a specific author
	Then I should get a 200 status code
	And the request result should match the expected results file
	Fetch List of Authors

Given the PoetryDB API is available
	When I request the list of authors
	Then I should get a 200 status code
	And the request result should match the expected results file
	Fetch Titles by Author

Given the PoetryDB API is available
	When I request the list of titles by a specific author
	Then I should get a 200 status code
	And the request result should match the expected results file
	
## Customizing the Comparison
The compare_results method in ApiUtils uses DeepDiff to compare actual and expected JSON data with flexibility to:
	Ignore specific paths.
	Handle differences in ordering.
	Report any repetitions in the response.


If the compare_results method detects any differences, it will save the differences in a JSON file within the compared_results directory. The filename includes a timestamp for easy tracking.
This allows for easier debugging and tracking of mismatches between actual and expected API responses.

## Notes:
Encoding Issue: When Python read the request results, certain characters in the response were misinterpreted.
For example, 'And brought’st Thy sweets along with Thee.' was read as 'And broughtâ€™st Thy sweets along with Thee.'.
To handle this, "encoding='utf-8'" was added when reading the expected files.

One of the tests will fail to showcase how DeepDiff highlights differences might look like. Example of DeepDiff Output for failing tests:

'values_changed': {
    "root[53]['title']": {
        'new_value': "Sonnet XXIII: To Aetna's Scorching Sands",
        'old_value': "Sonnet XXIII: To Aetna's Lukewarm Sands"
    }
},
'iterable_item_added': {
    'root[52]': {'title': 'The Haunted Beach'}
},
'iterable_item_removed': {
    'root[54]': {'title': "Who are you people and where's my horse?!"}
},
'repetition_change': {
    'root[51]': {
        'old_repeat': 2,
        'new_repeat': 1,
        'old_indexes': [51, 52],
        'new_indexes': [51],
        'value': {'title': 'Ode to the Muse'}
    }
}

This shows any differences between the actual and expected results in detail, such as value changes, added/removed items, and repetition changes.