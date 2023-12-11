from urllib.parse import quote

class Parameters:
    def __init__(self, query, language="en", location=None, safe_search="on", time_range=None):
        self.query = query
        self.language = language
        self.location = location
        self.safe_search = safe_search
        self.time_range = time_range
        self.base_url = "https://www.google.com/search?"

    def query(self, query):
        self.query = query

    def language(self, language):
        self.language = language

    def location(self, location):
        self.location = location

    def safe_search(self, safe_search):
        if safe_search.lower() not in ["on", "off"]:
            raise ValueError("Invalid value for safe_search. Options: 'on', 'off'")
        self.safe_search = safe_search.lower()

    def time_range(self, time_range):
        self.time_range = time_range

    def link(self):
        query_params = {"q": self.query, "hl": self.language, "safe": self.safe_search}

        if self.location is not None:
            query_params["near"] = self.location

        if self.time_range is not None:
            query_params["tbs"] = self.time_range

        encoded_params = "&".join(f"{key}={quote(str(value))}" for key, value in query_params.items())
        link = f"{self.base_url}{encoded_params}"

        return link