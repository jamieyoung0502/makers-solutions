# File: lib/activity_suggester.py
import requests


class ActivitySuggester:
    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    # This method calls an 'API' on the internet to get a random activity.
    # An API is a way of allowing programs to request data from other programs.
    def _make_request_to_api(self):
        # .get() is provided by the requests module sends a GET request to the specified URL and returns the server's response.
        # It takes a URL as its argument and returns a Response object, which contains the server's response to the request.
        response = requests.get("http://www.boredapi.com/api/activity")

        # .json() is provided by the Response object, which parses the server's response (in JSON format) and returns it as a Python dictionary.
        # JSON stands for JavaScript Object Notation, which is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
        return response.json()


# Usage
# =====
activity_suggester = ActivitySuggester()
# activity_suggester.suggest() will return a different value every time

print(activity_suggester.suggest())
# Why not: Learn how to use a french press

print(activity_suggester.suggest())
# Why not: Hold a video game tournament with some friends
