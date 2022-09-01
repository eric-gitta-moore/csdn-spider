from fake_useragent import UserAgent


class DownloadLoggerMiddleware:
    def process_request(self, request, spider):
        spider.logger.info('开始请求: {url}'.format(url=request.url))


class CustomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers['User-Agent'] = UserAgent().chrome


class HttpProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://127.0.0.1:8888'
