import scrapy
from ..items import AmazonBestSellerBooksItem


class AmazonBestSeller(scrapy.Spider):
    name = "books_spider"
    page_number = 2
    start_urls = [
        'https://www.amazon.com/gp/bestsellers/books',
    ]

    def parse(self, response, **kwargs):
        items = AmazonBestSellerBooksItem()
        items['title'] = response.css('.p13n-sc-truncated::text').extract()
        items['author'] = response.css('.a-link-child::text').extract()
        items['price'] = response.css('.p13n-sc-price::text').extract()
        items['image'] = response.css('img::attr(src)').extract()
        yield items

        # yielding the content of the next pages
        next_page = f'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_' \
                    f'{AmazonBestSeller.page_number}?_encoding=UTF8&pg={AmazonBestSeller.page_number}'
        yield response.follow(next_page, callback=self.parse)
