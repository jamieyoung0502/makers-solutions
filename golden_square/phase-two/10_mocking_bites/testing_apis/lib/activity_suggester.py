# File: lib/activity_suggester.py

class ActivitySuggester:
    def __init__(self, requester):  # requester is usually `requests`
        # this will allow us to inject a mock object instead of using the real requests module
        # this is called dependency injection (i.e. the dependency on requests)
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    def _make_request_to_api(self):
        # We use 'self.requester' rather than 'requests'
        response = self.requester.get("http://www.boredapi.com/api/activity")
        return response.json()

# Usage
# Now, to test the actual requests module, we just put it in in place of our Mock
# =====
# import requests
# activity_suggester = ActivitySuggester(requests)
# activity_suggester.suggest() # => "Why not: Learn how to use a french press"
# activity_suggester.suggest() # => "Why not: Hold a video game tournament with some friends"