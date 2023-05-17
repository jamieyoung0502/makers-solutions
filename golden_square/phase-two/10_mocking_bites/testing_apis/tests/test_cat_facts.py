from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_calls_api_to_provide_cat_fact():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
        "fact": "It may take as long as 2 weeks for a kitten to be able to hear well."
    }

    cat_fact = CatFacts(requester_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: It may take as long as 2 weeks for a kitten to be able to hear well."