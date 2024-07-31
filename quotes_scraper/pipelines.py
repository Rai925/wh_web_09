import json
from quotes_scraper.items import AuthorScraperItem, QuotesScraperItem

class QuotesScraperPipeline:

    def __init__(self):
        self.authors_file = open('authors.json', 'w', encoding='utf-8')
        self.quotes_file = open('quotes.json', 'w', encoding='utf-8')
        self.authors_data = []
        self.quotes_data = []

    def process_item(self, item, spider):
        if isinstance(item, QuotesScraperItem):
            self.quotes_data.append(dict(item))
        elif isinstance(item, AuthorScraperItem):
            self.authors_data.append(dict(item))
        return item

    def close_spider(self, spider):
        try:
            json_data = json.dumps(self.authors_data, ensure_ascii=False, indent=4)
            self.authors_file.write(json_data)
        except json.JSONDecodeError as e:
            print(f"Error in authors.json: {e}")
        except Exception as e:
            print(f"Unexpected error while writing authors.json: {e}")

        try:
            json_data = json.dumps(self.quotes_data, ensure_ascii=False, indent=4)
            self.quotes_file.write(json_data)
        except json.JSONDecodeError as e:
            print(f"Error in quotes.json: {e}")
        except Exception as e:
            print(f"Unexpected error while writing quotes.json: {e}")

        self.authors_file.close()
        self.quotes_file.close()
