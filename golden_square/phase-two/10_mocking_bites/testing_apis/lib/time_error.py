class TimeError:
    def __init__(self, requester, current_time):
        self._requester = requester
        self._current_time = current_time

    def error(self):
        return self._get_server_time() - self._current_time.time()

    def _get_server_time(self):
        response = self._requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]
