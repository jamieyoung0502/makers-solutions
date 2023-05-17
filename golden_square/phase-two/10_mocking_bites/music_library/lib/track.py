class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        return (keyword in self.title or keyword in self.artist)