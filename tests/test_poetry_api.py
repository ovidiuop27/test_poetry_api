import pytest
from pytest_bdd import scenario, given, when, then, parsers
from support.api_utils import ApiUtils


@pytest.fixture
def api():
    return ApiUtils()


@pytest.fixture
def context():
    return {}


@scenario('../features/poetry_api.feature', 'Fetch a random poem')
def test_fetch_random_poem():
    """Test fetching a random poem from PoetryDB."""


@scenario('../features/poetry_api.feature', 'Fetch poems by author')
def test_fetch_poems_by_author():
    """Test fetching poems by author from PoetryDB."""


@scenario('../features/poetry_api.feature', 'Fetch list of authors')
def test_fetch_authors():
    """Test fetching a list of authors from PoetryDB."""


@scenario('../features/poetry_api.feature', 'Fetch list of titles by author')
def test_fetch_author_titles():
    """Test fetching a list of titles for a specific author from PoetryDB."""


@given('the PoetryDB API is available')
def poetrydb_api_available(api):
    """Check that the PoetryDB API is available."""
    response = api.get_poems_by_author("Ozymandias")
    assert response.status_code == 200, "PoetryDB API is not available."


@when('I request a random poem')
def request_random_poem(api):
    """Request a random poem from PoetryDB."""
    response = api.get_random_poem()
    assert response.status_code == 200, "Failed to fetch a random poem."
    # Store response for later use
    request_random_poem.response = response.json()[0]


@then('I should receive a poem with a title and author')
def check_random_poem():
    """Verify the random poem has title and author."""
    poem = request_random_poem.response
    assert "title" in poem, "Poem has no title."
    assert "author" in poem, "Poem has no author."
    assert "author" in poem, "Poem has no author."


@when(parsers.parse('I request poems by the author "{author}"'))
def request_poems_by_author(api, author, context):
    """Request poems by author from PoetryDB."""
    context['response'] = api.get_poems_by_author(author)


@then('I should get a 200 status code')
def check_status_code(context):
    """Check that the response status code is 200."""
    assert context['response'].status_code == 200, "Failed to fetch poems by author."


@then(parsers.parse('the request result should match the "{expected}" results file'))
def check_response_matches_expected(api, context, expected):
    """Check that the response matches the expected results."""
    assert api.compare_results(expected, context['response'].text) == "No differences found."


@when('I request the list of authors')
def request_authors_list(api, context):
    """Request the list of authors from PoetryDB."""
    context['response'] = api.get_authors_list()


@then('the request result should match the "authors_list_expected.json" results file')
def check_authors_list(api, context):
    """Check that the response matches the expected results."""
    with open("expected_results/authors_list_expected.json", "r", encoding='utf-8') as f:
        expected_result = f.read()
    assert api.compare_results(context['response'].text, expected_result) == "No differences found."


@when(parsers.parse('I request the list of titles from the "{author}"'))
def request_author_titles(api, author, context):
    """Request the list of titles for a specific author from PoetryDB."""
    context['response'] = api.get_author_titles_list(author)


@then(parsers.parse('the request result should match the "{expected}" results file'))
def check_author_titles(api, context, expected):
    """Check that the response matches the expected results."""
    assert api.compare_results(expected, context['response'].text) == "No differences found."
