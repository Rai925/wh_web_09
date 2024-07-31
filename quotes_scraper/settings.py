BOT_NAME = 'quotes_scraper'

# Шлях до модулів
SPIDER_MODULES = ['quotes_scraper.spiders']
NEWSPIDER_MODULE = 'quotes_scraper.spiders'

# User-Agent, який буде використовуватися при скрапінгу
USER_AGENT = 'quotes_scraper (+http://www.quotes.toscrape.com)'

# Параметри для визначення, як часто Scrapy буде робити запити до сервера
DOWNLOAD_DELAY = 0  # секунди між запитами
CONCURRENT_REQUESTS = 32  # кількість одночасних запитів

# Налаштування для визначення, скільки запитів буде робити Scrapy одночасно
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Налаштування для політики обробки помилок
RETRY_ENABLED = True
RETRY_TIMES = 4  # кількість спроб повторення запиту при помилці

# Налаштування для збереження даних у форматі JSON
FEEDS = {
    'authors.json': {
        'format': 'json',
        'overwrite': True,  # переписати файл, якщо вже існує
        'encoding': 'utf-8',
    },
    'quotes.json': {
        'format': 'json',
        'overwrite': True,  # переписати файл, якщо вже існує
        'encoding': 'utf-8',
    },
}

# Включення pipeline для обробки даних
ITEM_PIPELINES = {
    'quotes_scraper.pipelines.QuotesScraperPipeline': 1,
}

# Налаштування для логування
LOG_LEVEL = 'DEBUG'
LOG_FILE = 'scrapy.log'  # файл для зберігання логів
LOG_ENABLED = True
LOG_STDOUT = True

# Налаштування для уникання проблем з капчами та перевантаженням сервера
ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False

# Налаштування для обробки HTML та JSON
FEED_EXPORT_ENCODING = 'utf-8'

# Налаштування для роботи з проксі (необов'язково)
# HTTP_PROXY = 'http://your_proxy:port'

# Налаштування для обробки JavaScript (необов'язково, якщо використовуєте Scrapy-Splash)
# SPLASH_URL = 'http://localhost:8050'
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Налаштування для обробки CSV (якщо потрібно)
# FEEDS = {
#     'items.csv': {
#         'format': 'csv',
#         'overwrite': True,
#         'encoding': 'utf-8',
#     },
# }