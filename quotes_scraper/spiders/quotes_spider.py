import scrapy
from ..items import QuotesScraperItem, AuthorScraperItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        # Парсинг цитат
        for quote in response.css('div.quote'):
            # Створення і заповнення елемента цитати
            quote_item = QuotesScraperItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('span small::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            if all([quote_item['text'], quote_item['author'], quote_item['tags']]):
                yield quote_item
            else:
                self.log(f"Skipping incomplete quote data: {quote_item}")

            # Отримання URL автора і передача його на обробку
            author_url = quote.css('span a::attr(href)').get()
            if author_url:
                yield response.follow(author_url, self.parse_author)

        # Перехід до наступної сторінки
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        # Створення і заповнення елемента автора
        author_item = AuthorScraperItem()
        author_item['fullname'] = response.css('h3.author-title::text').get()
        author_item['born_date'] = response.css('span.author-born-date::text').get()
        author_item['born_location'] = response.css('span.author-born-location::text').get()
        author_item['description'] = response.css('div.author-description::text').get()
        if all([author_item['fullname'], author_item['born_date'], author_item['born_location'], author_item['description']]):
            yield author_item
        else:
            self.log(f"Skipping incomplete author data: {author_item}")
