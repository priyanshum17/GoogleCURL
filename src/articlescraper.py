import requests
from bs4 import BeautifulSoup

class WebPageScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  

            soup = BeautifulSoup(response.text, 'html.parser')

            title = self.extract_title(soup)

            description = self.extract_description(soup)

            result = {
                'title': title,
                'description': description,
                'link': self.url
            }

            return result

        except requests.exceptions.RequestException as e:
            return None

    def extract_title(self, soup):
        title_tags = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        for tag in title_tags:
            title_element = soup.find(tag)
            if title_element:
                return title_element.get_text(strip=True)
        return None

    def extract_description(self, soup):
        description_tags = ['meta[name="description"]', 'meta[property="og:description"]', 'meta[property="twitter:description"]', 'p', 'span']
        for tag in description_tags:
            description_element = soup.select_one(tag)
            if description_element:
                return description_element.get_text(strip=True)
        return None
