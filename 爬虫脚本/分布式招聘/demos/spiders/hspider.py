# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider



class TencentSpider(RedisCrawlSpider):
    name = 'hspider'
    # allowed_domains = ['[图片]tencent.com']
    redis_key = 'hspider:start_urls'
    # start_urls = ['[图片]http://tencent.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'position.php\?tid=')), follow=True),
        Rule(LinkExtractor(allow=(r'position_detail')), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        name = response.xpath('//tr[@class="h"]/td/text()')
        for i in name:
            names = i.extract()
            yield {
                'name': response.css('title::text').extract_first(),
                'url': response.url,
            }
