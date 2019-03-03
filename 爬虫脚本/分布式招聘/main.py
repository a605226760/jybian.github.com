from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl hao123'.split())
os.chdir('demos/spiders')
# 运行分布式爬虫命令
cmdline.execute('scrapy runspider hspider.py'.split())