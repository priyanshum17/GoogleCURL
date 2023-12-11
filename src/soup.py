import requests
from bs4 import BeautifulSoup

class LinkScraper:
    def __init__(self, url) -> None:
        self.url = url

    def link_scraper(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            search_results = soup.find_all("a")
            news_links = [result.get("href") for result in search_results if result.get("href", "").startswith("http") and "google" not in result.get("href")]
            return news_links
        return []
