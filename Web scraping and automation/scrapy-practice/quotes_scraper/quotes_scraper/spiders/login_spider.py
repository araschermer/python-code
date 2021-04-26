import scrapy
from scrapy.http import FormRequest
import os
from ..items import QuotetutorialItem
from  scrapy.utils.response import open_in_browser

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')


class QuoteSpider(scrapy.Spider):
    name = 'login_spider'
    start_urls = [
        'http://quotes.toscrape.com/login',
    ]

    def parse(self, response, **kwargs):
        csrf_token = response.css('form input::attr(value)').extract_first()
        print(f"csrf_token={csrf_token}")
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf_token,
            'username': username,
            'password': password,
        },
                                         callback=self.start_spider)

    def start_spider(self, response):
        # To confirm a successful login, open the page after logging into the website in the browser
        open_in_browser(response)
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
        # to get the spider crawling the next pages of the website
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            #  scrape the pages recursively
            yield response.follow(next_page, callback=self.parse)
