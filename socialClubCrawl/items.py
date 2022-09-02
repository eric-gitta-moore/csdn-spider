# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SocialclubcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RecommendDataItem(scrapy.Item):
    # """avatar: 头像"""
    # avatar = scrapy.Field()

    """picList: 多图展示的图片，第一张就是头图"""
    pic_list = scrapy.Field()

    """csdnTag: CSDN分类标签"""
    tags = scrapy.Field()

    """user_name: 用户id"""
    user_name = scrapy.Field()

    """created_at: 创作时间"""
    create_time = scrapy.Field()

    """title: 文章标题"""
    title = scrapy.Field()

    """certificate_info: 认证信息，e.g. 全栈领域优质创作者"""
    certificate_info = scrapy.Field()

    # """nickname: 昵称"""
    # nickname = scrapy.Field()
    #
    # """company: 所在公司"""
    # company = scrapy.Field()

    """views: 阅读量"""
    views = scrapy.Field()

    """comments: 评论量"""
    comments = scrapy.Field()

    """url: 文章链接"""
    url = scrapy.Field()


class UserDataItem(scrapy.Item):
    """昵称"""
    nickname = scrapy.Field()

    """user_name: 用户id"""
    user_name = scrapy.Field()

    """码龄"""
    age = scrapy.Field()

    """总访问量"""
    total_views = scrapy.Field()

    """加入CSDN时间"""
    join_time = scrapy.Field()

    """原创数量"""
    original_article_count = scrapy.Field()

    """排名"""
    rank = scrapy.Field()

    """粉丝数"""
    fans = scrapy.Field()

    """个人简介"""
    intro = scrapy.Field()

    """IP归属地"""
    ip_address = scrapy.Field()

    """博客介绍"""
    blog_intro = scrapy.Field()

    """头像链接"""
    avatar = scrapy.Field()

    """性别"""
    sex = scrapy.Field()
