import scrapy
from brickset.items import BricksetItem

class BricksetSpider(scrapy.Spider):
    name = "brickset"
    allowed_domains = ["brickset.com"]
    start_urls = ["https://brickset.com/sets/year-2016"]

    def parse(self, response): # Define parse() function. 
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            yield {
            'Name': brickset.css('h1 ::text').extract_first(),
            'Pieces': brickset.xpath('.//dl[dt/text() = "Pieces"]/dd/a/text()').extract_first(),
            'Minifigs': brickset.xpath('.//dl[dt/text() = "Minifigs"]/dd[2]/a/text()').extract_first()
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )