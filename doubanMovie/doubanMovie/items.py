# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    id = scrapy.Field()    # 电影编号
    title = scrapy.Field()    # 名称
    rate = scrapy.Field()    # 评分
    url = scrapy.Field()    # 地址
    cover = scrapy.Field()    # 图片地址
    cover_x = scrapy.Field()    # 显示x轴
    cover_y = scrapy.Field()    # 显示y轴
    playable = scrapy.Field()    # 是否热映
    is_new = scrapy.Field()    # 是否新上映
