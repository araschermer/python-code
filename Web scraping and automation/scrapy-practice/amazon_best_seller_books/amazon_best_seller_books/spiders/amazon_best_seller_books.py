import scrapy


# scrapy startproject amazon_best_seller_books
class BestSellerBooksSpider(scrapy.Spider):
    name = "amazon_best_seller_books"
    start_urls = [
        "https://www.amazon.com/gp/bestsellers/books"
    ]

    def parse(self, response, **kwargs):
        webpage_title = response.css('title::text').extract()
        titles_list = response.css('span.a.div.p13n-sc-truncated::text').extract()
        titles_list = response.xpath('//div[@class="p13n-sc-truncated"]/text()').extract()
        authors_list = response.css('.a-link-child::text').extract()
        prices_list = response.css('.p13n-sc-price::text').extract()
        links_list = response.css("a.a-link-normal").xpath("@href").extract()
        with open("links_list.txt", 'a') as f:
            for link in titles_list:
                f.write(f"https://www.amazon.com{link}\n")

        print(f"best seller books\n  {titles_list}")
        print(f"best seller prices\n  {prices_list}")
        print(f"best seller authors\n   {authors_list}")
        # books_authors = dict(zip(titles_list, authors_list))
        yield titles_list
