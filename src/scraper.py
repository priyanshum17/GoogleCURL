from . import soup
from . import generator
from . import parameters
from . import articlescraper

class Scraper:
    def __init__(self, query, num_pages = 1):
        self.query = query
        self.num_pages = num_pages
        self.params = parameters.Parameters(query)
    
    def link(self):
        return self.params.link()
    
    def additional_links(self, num_pages = 10):
        return generator.PageGenerator(self.link()).url_generator(num_pages, 10)
    
    def urls(self):
        links = set()

        urls = self.additional_links()
        for url in urls:
            list = soup.LinkScraper(url).link_scraper()

            for item in list:
                links.add(item)

        return links
    
    def search(self):
        urls = self.urls()
        results = []

        for url in urls:
            results.append(articlescraper.WebPageScraper(url).scrape())
        
        return results
    
    def print_results(self, n=10):
        search_results = self.search()[:n]
        
        for idx, result in enumerate(search_results, start=1):
            print(result['title'])
            print(result['link'])
            print()

Scraper("python").print_results()