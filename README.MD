# CSDN推荐列表spider

请先安装MongoDB

## 爬虫使用方法

开启抓取
```shell
# 下载代码
git clone https://github.com/james-curtis/csdn-spider.git
cd csdn-spider
# 安装依赖
pip install -r requirements.txt
# 开始采集
# 注意要配置MongoDB链接
scrapy crawl CSDN -s MONGO_URI="mongodb://192.168.44.181:27017/"
```

暂停/恢复
```shell
telnet 127.0.0.1 6023
# 暂停
engine.pause()
# 恢复
engine.unpause()
```

## Jupyter使用方法

```shell
# 安装依赖
pip install -r requirements.txt
# 启动jupyter实验室
jupyter lab
```

## 使用MongoDB数据库备份

备份文件在 `/dump/spider` 目录下，如有需要可以使用

`mongodump` 和 `mongorestore` 没有这两个命令的话，请先下载 [database-tools](https://www.mongodb.com/try/download/database-tools)

## TODO
- [x] 性别 码龄 创建时间 关系

- [x] 发布博客量与发布地 地图

- [x] tag词云

- [ ] title词云、desc词云、博客名称词云、博客介绍词云、昵称词云

- [ ] 地域平均码龄

- [ ] 浏览量、评论量、粉丝量、博客量、排名、总浏览量与码龄

- [ ] 热门标签

  