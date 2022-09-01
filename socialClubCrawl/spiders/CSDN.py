import scrapy
from socialClubCrawl.items import *
from socialClubCrawl.config import *


class CSDNSpider(scrapy.Spider):
    name = 'CSDN'
    start_urls = [Config.getRecommendUrl(0)]

    """爬行页面限制，爬取多少个推荐页面"""
    crawl_page_limit = 100

    def parse(self, response, **kwargs):
        self.crawl_page_limit -= 1

        result = response.json()

        for item in result['data']['www-blog-recommend']['info']:
            item_data = item['extend']
            recommend_data_item = RecommendDataItem()

            """pic_list: 多图展示的图片，第一张就是头图"""
            recommend_data_item['pic_list'] = item_data['picList']

            """csdnTag: CSDN分类标签"""
            recommend_data_item['tags'] = item_data['csdnTag']

            """user_name: 用户id"""
            recommend_data_item['user_name'] = item_data['user_name']

            """created_at: 创作时间"""
            recommend_data_item['create_time'] = item_data['created_at']

            """title: 文章标题"""
            recommend_data_item['title'] = item_data['title']

            """certificate_info: 认证信息，e.g. 全栈领域优质创作者"""
            recommend_data_item['certificate_info'] = item_data['certificate_info']

            """views: 阅读量"""
            recommend_data_item['views'] = item_data['views']

            """comments: 评论量"""
            recommend_data_item['comments'] = item_data['comments']

            """url: 文章链接"""
            recommend_data_item['url'] = item_data['url']

            yield recommend_data_item

            """获取该用户信息"""
            yield scrapy.Request(Config.getUserInfoUrl(recommend_data_item['user_name']), callback=self.parseUserInfo)

        if self.crawl_page_limit <= 0:
            return
        """下一页推荐"""
        yield response.follow(Config.getRecommendUrl(self.crawl_page_limit), dont_filter=True)

    def parseUserInfo(self, response):
        user_data_item = UserDataItem()

        """昵称"""
        user_data_item['nickname'] = response.xpath("//div[@class='user-profile-head-name']/div[1]/text()").get()

        """user_name: 用户id"""
        user_data_item['user_name'] = response.xpath("//link[@rel='canonical']/@href").get().split('/')[-1]

        """码龄"""
        try:
            user_data_item['age'] = response.xpath("//div[@class='person-code-age']/span/text()").get() \
                .replace('码龄', '').replace('年', '').strip()
        except:
            pass

        """博客访问量"""
        try:
            user_data_item['total_views'] = \
                response.xpath(
                    "//div[@class='user-profile-statistics-name' and contains(text(),'总访问量')]/preceding-sibling::div[@class='user-profile-statistics-num']/text()") \
                    .get().split('：')[-1].replace(',', '')
        except:
            pass

        """加入CSDN时间"""
        try:
            user_data_item['join_time'] = \
                response.xpath("//span[contains(@class,'user-general-info-key-word')]/text()").get()
        except:
            pass

        """原创数量"""
        try:
            user_data_item['original_article_count'] = \
                response.xpath("//div[@class='user-profile-statistics-name' and contains(text(),"
                               "'原创')]/preceding-sibling::div[@class='user-profile-statistics-num']/text()") \
                    .get().replace(',', '')
        except:
            pass

        """排名"""
        try:
            user_data_item['rank'] = \
                response.xpath("//div[@class='user-profile-statistics-name' and contains(text(),"
                               "'排名')]/preceding-sibling::div[@class='user-profile-statistics-num']/text()") \
                    .get().replace(',', '')
        except:
            pass

        """粉丝数"""
        try:
            user_data_item['fans'] = \
                response.xpath("//div[@class='user-profile-statistics-name' and contains(text(),"
                               "'粉丝')]/preceding-sibling::div[@class='user-profile-statistics-num']/text()") \
                    .get().replace(',', '')
        except:
            pass

        """个人简介"""
        try:
            user_data_item['intro'] = \
                response.xpath("//p[contains(@class,'introduction-fold')]/text()").get()
        except:
            pass

        """IP归属地"""
        try:
            user_data_item['ip_address'] = response \
                .xpath("//div[contains(@class,'user-profile-head-address')]//span[@class='address']/text()") \
                .get().split('：')[1]
        except:
            pass

        """博客介绍"""
        try:
            user_data_item['blog_intro'] = \
                response.xpath("//h1[contains(@class,'user-profile-title')]/text()").get()
        except:
            pass

        """头像链接"""
        user_data_item['avatar'] = \
            response.xpath("//div[contains(@class,'user-profile-avatar')]/img/@src").get()

        yield user_data_item
