# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    imagesUrls = scrapy.Field()
    imagesPath = scrapy.Field()


class DongguanItem(scrapy.Item):
    # 每个帖子的标题
    title = scrapy.Field()
    # 每个帖子的编号
    number = scrapy.Field()
    # 每个帖子的内容
    content = scrapy.Field()
    # 每个帖子的url
    url = scrapy.Field()