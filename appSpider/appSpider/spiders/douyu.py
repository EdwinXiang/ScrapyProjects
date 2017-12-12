# -*- coding: utf-8 -*-
import scrapy
import json
from appSpider.items import AppspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['http://capi.douyucdn.cn']

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url+str(offset)]

    def parse(self, response):
        # 返回从json里面获取数据的集合
        file = open('douyu.html','w',encoding='utf-8')
        file.write(response.text)
        file.close()
        data = json.loads(response.text)['data']

        for each in data:
            item = AppspiderItem()
            item['name'] = each['nickname']
            item['imagesUrls'] = each['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

