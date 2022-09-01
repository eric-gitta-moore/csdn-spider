BOT_NAME = 'socialClubCrawl'

SPIDER_MODULES = ['socialClubCrawl.spiders']
NEWSPIDER_MODULE = 'socialClubCrawl.spiders'
# LOGSTATS_INTERVAL = 1

DUPEFILTER_DEBUG = True
# SCHEDULER_DEBUG = True
# LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 999
CONCURRENT_REQUESTS_PER_DOMAIN = 999

# COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_USERNAME = 'scrapy'
TELNETCONSOLE_PASSWORD = 'scrapy'

# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
DOWNLOADER_MIDDLEWARES = {
    # 'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'socialClubCrawl.middlewares.CustomUserAgentMiddleware': 545,
    'socialClubCrawl.middlewares.DownloadLoggerMiddleware': 555,
    # 'mkz.middlewares.HttpProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    # 'socialClubCrawl.pipelines.MongoPipeline': 300,
    'socialClubCrawl.pipelines.JsonWriterPipeline': 301,
}

MONGO_URI = 'mongodb://192.168.44.181:27017/'
# MONGO_DATABASE = 'social'
