from unittest.mock import Mock
from lib.time_error import TimeError

def test_calls_api_to_provide_time_diff():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    current_time_mock = Mock(name="current_time")

    requester_mock.get.return_value = response_mock
    current_time_mock.time.return_value = 1682950924

    response_mock.json.return_value = {
        "unixtime": 1682950964
    }

    time_error = TimeError(requester_mock, current_time_mock)
    result = time_error.error()
    assert result == 40