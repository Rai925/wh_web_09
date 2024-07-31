import scrapy
from scrapy.crawler import CrawlerProcess
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    quotes_data = []

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = {
                'tags': quote.css('div.tags a.tag::text').getall(),
                'author': quote.css('small.author::text').get(),
                'quote': quote.css('span.text::text').get(),
            }
            self.quotes_data.append(quote_item)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            with open('quotes.json', 'w', encoding='utf-8') as f:
                json.dump(self.quotes_data, f, ensure_ascii=False, indent=2)


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    authors_data = []

    def parse(self, response):
        author_links = response.css('small.author ~ a::attr(href)').getall()
        for link in author_links:
            yield response.follow(link, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        author_item = {
            'fullname': response.css('h3.author-title::text').get().strip(),
            'born_date': response.css('span.author-born-date::text').get(),
            'born_location': response.css('span.author-born-location::text').get().strip(),
            'description': ' '.join(response.css('div.author-description::text').get().strip().split()),
        }
        self.authors_data.append(author_item)

        with open('authors.json', 'w', encoding='utf-8') as f:
            json.dump(self.authors_data, f, ensure_ascii=False, indent=2)


def run_spiders():
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()


if __name__ == "__main__":
    run_spiders()
