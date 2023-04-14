import scrapy


class MagazineSpider(scrapy.Spider):
    name = "Magazine"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/"]

    def parse(self, response):
        quotes = response.css("p.sc-kDvujY.jDmBNY.sc-hYufOg.duAQZa::text").getall()
        for i in quotes:
            yield {
                'avaliacao': i
            }
