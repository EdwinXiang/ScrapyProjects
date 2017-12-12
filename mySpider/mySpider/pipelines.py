# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 将数据写入json
import json

class itcastJsonPipeline(object):

    def __init__(self):
        self.file = open('teacher.json','w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()

class tencentPipeline(object):
    def __init__(self):
        self.file = open('tencent.json','w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()

    # def default(self, obj):
    #     if isinstance(obj, item):
    #         return obj.name
    #     return json.JSONEncoder.default(self, obj)