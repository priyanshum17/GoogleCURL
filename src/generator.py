from urllib.parse import urlparse, parse_qs, urlunparse, urlencode

class PageGenerator:
    def __init__(self, first_url, num_pages = 10):
        self.first_url = first_url

    def url_generator(self, num_pages=10, results_per_page=10):
        parsed_url = urlparse(self.first_url)
        query_params = parse_qs(parsed_url.query)
        start_param = query_params.get('start', ['0'])[0]
        start_value = int(start_param)
        generated_urls = [self.first_url]
        for _ in range(num_pages):
            start_value += results_per_page
            query_params['start'] = str(start_value)
            updated_url = urlunparse(parsed_url._replace(query=urlencode(query_params, doseq=True)))
            generated_urls.append(updated_url)
        return generated_urls