# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from coserSpider.items import CoserspiderItem

class CoserSpider(scrapy.Spider):
    name = 'coser'
    allowed_domains = ['byc.net']
    start_urls = [
        'http://bcy.net/cn125101',
        'http://bcy.net/cn126487',
        'http://bcy.net/cn126173'
    ]

    def parse(self, response):
        sel = Selector(response)

        for link in sel.xpath("//ul[@class='js-articles l-works']/li[@lass='l-work--big']/article[@class='work work--second-created']/h2/[@class='work_title']/a/@href").extract():
            link = 'http://bcy.net%s' % link
            request = scrapy.Request(link,callback=self.parase_item)
            yield request


    def parase_item(self,response):
        l = ItemLoader(item = CoserspiderItem(),response=response)
        l.add_xpath('name', "//h1[@class='js-post-title']/text()")
        l.add_xpath('info',"//div[@class='post__info']/div[@class='post__type post__info-group']/span/text()")
        urls = l.get_xpath('//img[@class="detail_std detail_clickable"]/@src')
        urls = [url.replace('/w650','') for url in urls]
        l.add_xpath('image_urls',urls)
        l.add_xpath('url',response.url)
        return l.load_item()