# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class itcastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()




# 腾讯职业类
class tencentItem(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()

