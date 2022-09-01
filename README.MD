# CSDN推荐列表spider

## 使用方法

开启抓取
```shell
# 下载代码
git clone https://github.com/james-curtis/csdn-spider.git
cd csdn-spider
# 安装依赖
pip install -r requirements.txt
# 开始采集
# COMIC_PUBLISH_URL 替换成你对应的漫画发布地址
# CHAPTER_PUBLISH_URL 替换成你对应的章节发布地址
# PUBLISH_PWD 替换成你对应的发布密码
# 后续更新的话重新执行下面这一条命令就可以了
# 注意要配置MongoDB链接
scrapy crawl CSDN -s MONGO_URI='mongodb://192.168.44.181:27017/'
```

暂停/恢复
```shell
telnet 127.0.0.1 6023
# 暂停
engine.pause()
# 恢复
engine.unpause()
```