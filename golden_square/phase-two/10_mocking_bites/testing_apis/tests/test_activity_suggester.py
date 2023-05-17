# File: tests/test_activity_suggester.py
from unittest.mock import Mock
from lib.activity_suggester import ActivitySuggester

def test_calls_api_to_provide_suggested_activity():
    requester_mock = Mock(name="requester") # This name is just for readability, you don't have to include it
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock`
    # when we call `get()` on it.
    # we can have a Mock return a Mock!
    requester_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {
        "activity": "Write a short story",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "",
        "key": "6301585",
        "accessibility": 0.1
    }

    activity_suggester = ActivitySuggester(requester_mock)
    result = activity_suggester.suggest()
    assert result == "Why not: Write a short story"

    # alternatively, we don't have to create another Mock here, we could:

    requester_mock = Mock()
    requester_mock.get().json.return_value = {
        "activity": "Write a short story"
    }

    assert result == "Why not: Write a short story"