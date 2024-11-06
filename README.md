# PoetryDB API Testing Project

This repository contains a test suite for the PoetryDB API, using Behavior-Driven Development (BDD) to verify various endpoints. The tests are written with pytest and pytest-bdd, and they validate API responses against expected data using DeepDiff. Any discrepancies between the actual and expected responses are logged in a timestamped JSON file in a compared_results directory.

## Project Structure:
```
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
```

## Prerequisites
Python 3.x
PoetryDB API running or accessible online.

## Install Dependencies
```bash: pip install -r requirements.txt```

## Dependencies Used
	- pytest: For running tests.
	- pytest-bdd: For behavior-driven testing with Gherkin syntax.
	- requests: For making HTTP requests to the PoetryDB API.
	- deepdiff: For comparing API responses against expected results.

## Running Tests
```bash: pytest -v```

You should see output indicating which tests have passed or failed, along with any differences found between actual and expected results.

## Test Cases
| Scenario                   | Steps                                                                                                                                                                                                                   | Expected Result                                                                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fetch a Random Poem**    | 1. Given the PoetryDB API is available<br>2. When I request a random poem<br>3. Then I should receive a poem with a title and author                                                                                    | A JSON response with a `"title"` and `"author"` field present in the poem data                                                                 |
| **Fetch Poems by Author**  | 1. Given the PoetryDB API is available  2. When I request poems by a specified author<br>3. Then I should get a 200 status code<br>4. And the request result should match the expected JSON file                        | HTTP 200 status code<br>with response data matching the expected JSON structure and contents for that author                                   |
| **Fetch List of Authors**  | 1. Given the PoetryDB API is available  2. When I request the list of authors<br>3. Then I should get a 200 status code<br>4. And the request result should match the authors list JSON file                            | HTTP 200 status code<br>with the JSON response containing the full<br>correct list of authors in `expected_results/authors_list_expected.json` |
| **Fetch Titles by Author** | 1. Given the PoetryDB API is available  2. When I request the list of titles by an author<br>3. Then I should get a 200 status code<br>4. And the request result should match the titles list JSON file for that author | HTTP 200 status code<br>with response JSON matching the expected list of titles in `expected_results` for the specific author                  |
	
## Customizing the Comparison
The compare_results method in ApiUtils uses DeepDiff to compare actual and expected JSON data with flexibility to:
- Ignore specific paths.
- Handle differences in ordering.
- Report any repetitions in the response.

If the compare_results method detects any differences, it will save the differences in a JSON file within the compared_results directory. The filename includes a timestamp for easy tracking.
This allows for easier debugging and tracking of mismatches between actual and expected API responses.

## Reason for Choosing DeepDiff
DeepDiff is used here due to its robustness in detecting even minor discrepancies between the API response and expected data.
It is especially helpful in validating dynamic API content, where slight changes may be introduced by the data source.
With DeepDiff, the tests can ignore minor ordering issues while detecting meaningful differences, and the results of failing tests are saved to JSON files in compared_results for easy debugging.

## Notes:
Encoding Issue: When Python read the request results, certain characters in the response were misinterpreted.
For example, 'And brought’st Thy sweets along with Thee.' was read as 'And broughtâ€™st Thy sweets along with Thee.'.
To handle this, "encoding='utf-8'" was added when reading the expected files.

One of the tests will fail to showcase how DeepDiff highlights differences might look like. Example of DeepDiff Output for failing tests:
```
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
```
This shows any differences between the actual and expected results in detail, such as value changes, added/removed items, and repetition changes.