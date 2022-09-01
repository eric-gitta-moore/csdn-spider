import scrapy


class DouyinspiderSpider(scrapy.Spider):
    name = 'DouyinSpider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
