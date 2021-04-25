import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes_scraper'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()

        div_quotes = response.css('div.quote')

        for quote_data in div_quotes:
            quote = quote_data.css('span.text::text').extract()
            author = quote_data.css('.author::text').extract()
            tags = quote_data.css('.tag::text').extract()

            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags

            yield items
