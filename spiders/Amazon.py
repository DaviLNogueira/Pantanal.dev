import scrapy


class AmazonSpider(scrapy.Spider):
    name = "Amazon"
    allowed_domains = ["www.amazon.com.br"]
    start_urls = ["https://www.amazon.com.br/"]

    def parse(self, response):
        quotes = response.css('div.a-expander-content span::text').getall()

        for i in quotes:
            yield {
                'avaliacao': i
            }
