
import requests
from fake_useragent import UserAgent #导入随机请求头
from lxml import etree
from bs4 import BeautifulSoup
import re

class AyuSpider():
    def __init__(self):
        pass
    # 爬虫第一步，从请求开始
    @staticmethod
    def request_url(url,decode):
        ua = UserAgent() #随机请求头
        headers = {'user-agent': ua.random} #随机请求头
        r = requests.get(url,headers=headers) #请求url
        r.encoding = decode
        indexs = r.text #将请求到的html代码返回
        return indexs

# xpath数据清洗
    @staticmethod
    def xpath_url(info,xapths): #传入两个实参 html代码 和xapth 规则
        res = etree.HTML(info) #将HTML代码变为XML
        info = res.xpath(xapths) #执行xpath清洗操作
        return info

# 正则清洗
    @staticmethod
    def re_url(pattern,info): # 正则匹配模式 默认search pattern为正则匹配规则 info为正则匹配信息
        patt = re.compile(eval(pattern))
        m = patt.search(info)
        return m

#bs4 选择器 慎用 待更新 有BUG
    @staticmethod
    def bs4_url(info,bs4):
        soup = BeautifulSoup(info)
        str = 'soup.'+bs4
        res = eval(str)
        return res
#下载功能
    @staticmethod
    def download_url(url,name):
        downloads = requests.get(url,stream=True)
        with open(name, "wb") as file:
            for chunk in downloads.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
