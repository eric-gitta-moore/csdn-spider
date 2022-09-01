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