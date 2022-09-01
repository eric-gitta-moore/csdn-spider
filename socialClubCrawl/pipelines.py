import pymongo
from itemadapter import ItemAdapter
from .items import *
import json


class SocialclubcrawlPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'spider')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, RecommendDataItem):
            self.db['article'].insert_one(ItemAdapter(item).asdict())
        elif isinstance(item, UserDataItem):
            self.db['user'].insert_one(ItemAdapter(item).asdict())
        return item


class JsonWriterPipeline:

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        if isinstance(item, RecommendDataItem):
            self.file = open('article.jl', 'w')
        elif isinstance(item, UserDataItem):
            self.file = open('user.jl', 'w')
        self.file.write(line)
        self.file.close()
        return item
