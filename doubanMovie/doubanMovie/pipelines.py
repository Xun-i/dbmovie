# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanmoviePipeline:
    def process_item(self, item, spider):
        db = pymysql.connect(host="127.0.0.1", user="zack", password="123456", db='db', charset="utf8")
        cursor = db.cursor()
        id =  item["id"]
        title =  item["title"]
        rate =  item["rate"]
        url =  item["url"]
        cover =  item["cover"]
        cover_x =  item["cover_x"]
        cover_y =  item["cover_y"]
        playable =  item["playable"]
        is_new =  item["is_new"]
        cursor.execute(
            'INSERT INTO db_movie(id, title, rate, url, cover, cover_x, cover_y, playable, is_new) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (id, title, rate, url, cover, cover_x, cover_y, playable, is_new)
        )
        db.commit()
        cursor.close()
        return item
