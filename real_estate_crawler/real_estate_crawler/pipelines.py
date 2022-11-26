# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class RealEstateCrawlerPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('properties.db')
        self.curr = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS properties_tb(
                        listing_id TEXT,
                        title TEXT,
                        construction_type TEXT,
                        floor TEXT,
                        square_meters TEXT,
                        construction_year TEXT,
                        price TEXT,
                        location TEXT,
                        url TEXT
                        )""")

    def store_db(self, item):
        self.curr.execute("""INSERT or IGNORE INTO properties_tb VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            item['listing_id'],
            item['title'],
            item['construction_type'],
            item['floor'],
            item['square_meters'],
            item['construction_year'],
            item['price'],
            item['location'],
            item['url'],
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
