import json

import scrapy
from ..settings import headers
from ..items import DoubanmovieItem

class MovieSpider(scrapy.Spider):
    name = 'db'   # 爬虫名称
    allowed_domains = ['movie.douban.com']  # 根域名
    starts_url = []  # 开启启动项

    def start_requests(self):  # 开始请求直接执行
        url = 'https://movie.douban.com/j/search_tags'
        yield scrapy.Request(url, self.parse,headers=headers)

    def parse(self, response, **kwargs):  # 根据开始请求获取tags再次发起获取电影回执json
        tags = json.loads(response.text).get("tags")
        for tag in tags:  # 获取电影分类名称
            for page_start in range(0, 400, 20):  # 计算开始页
                nextPage = 'https://movie.douban.com/j/search_subjects?type={}&tag={}&page_limit={}&page_start={}'.format('movie', tag, 20, page_start)
                yield scrapy.Request(url=nextPage, callback=self.Pageparse,headers=headers)


    def Pageparse(self, response):
        html = json.loads(response.text)  # 获取电影内容
        for movie in html["subjects"]:  # 解析
            item = DoubanmovieItem()  #初始化属性项
            item['id'] = movie['id']  # 将编号及相关信息存入存储对象中
            item['title'] = movie['title']
            item['rate'] = movie['rate']
            item['url'] = movie['url']
            item['cover'] = movie['cover']
            item['cover_x'] = movie['cover_x']
            item['cover_y'] = movie['cover_y']
            item['playable'] = movie['playable']
            item['is_new'] = movie['is_new']

            yield item  # 返回对象
