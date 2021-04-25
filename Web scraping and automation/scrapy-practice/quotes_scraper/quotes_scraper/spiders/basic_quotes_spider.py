import scrapy


class QuotesSpider(scrapy.Spider):
    name = "basic_quotes_scraper"
    start_urls = [
        "https://quotes.toscrape.com/",
    ]

    def parse(self, response,**kwargs):

        title = response.css('title::text').extract()  # ['Quotes to Scrape']
        # response.css("title::text").extract_first() :-> 'Quotes to Scrape'

        # using css selector
        quotes_list = response.css('span.text::text').extract()
        authors_list = response.css('small.author::text').extract()

        # using xpath
        # quotes_list = response.xpath('//span[@class="text"]/text()').extract()
        # authors_list = response.xpath('//small[@class="author"]/text()').extract()
        # print(f"Authors List: {authors_list}")
        # print(f"Quotes List: {quotes_list}")

        quotes_authors_dict = dict(zip(quotes_list, authors_list))
        with open('quotes_authors.txt', 'a') as quotes_authors:
            for quote, author in quotes_authors_dict.items():
                quotes_authors.write(f"{quote}, by {author}\n ")

        yield {"title": title,
               "quotes": quotes_list}  # {'title': ['Quotes to Scrape']}

# scrapy shell "quotes.toscrape.com"
