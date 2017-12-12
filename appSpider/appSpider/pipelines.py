# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

#文件处理类 可以指定编码格式
import codecs
import json

class ImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self,item,info):
        image_url = item["imagesUrls"]
        yield scrapy.Request(image_url)


    def item_completed(self,results,item,info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到image_path里
        image_path = [x['path'] for ok,x in results if ok]

        os.rename(self.IMAGES_STORE+'/'+image_path[0],self.IMAGES_STORE+'/'+item['name']+'.jpg')
        item['imagesPath'] = self.IMAGES_STORE + '/' + item['name']

        return item
    # def process_item(self, item, spider):
    #     return item


class JsonWriterPipeline(object):

    def __init__(self):
        # 创建一个只写文件，指定文本编码格式为utf-8
        self.filename = codecs.open('sunwz.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def spider_closed(self, spider):
        self.file.close()


# class JsonWriterPipeline(object):
#
#
#     def __init__(self):
#         #创建一个只写文件，指定文本编码格式utf-8
#         self.filename = codecs.open('sunwz.json','w',encoding='utf-8')
#
#
#     def process_item(self,item,spider):
#         content = json.dumps(dict(item),ensure_ascii=False)+'\n'
#         self.filename.write(content)
#         # self.filename.close()
#         return item
#
#     def spider_item(self):
#         self.filename.close()
