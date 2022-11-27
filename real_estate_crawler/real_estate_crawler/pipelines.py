# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time

from itemadapter import ItemAdapter
import sqlite3


class RealEstateCrawlerPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('properties.db')
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS properties_tb(
                        listing_id INT Unique,
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

    def close_spider(self, spider):
        tsv_request = input('Do you want to export the results in a .tsv file? [Y/N]? ')
        time.sleep(1)
        if tsv_request == 'N':
            return
        elif tsv_request == 'Y':
            print('Generating .tsv file...')
            time.sleep(1)
            self.export_in_tsv_format()
            print('"properties.tsv" created.')
            time.sleep(1)
            print('File Location: ..\\real_estate_crawler\\properties.tsv\nYou can open the file via Excel.')
            time.sleep(1)
        else:
            print('Please press "Y" or "N" to proceed.')
            self.close_spider(spider)

    def export_in_tsv_format(self):
        with open('properties.tsv', 'w+', encoding='utf-16') as file:
            file.write('ID\tTITLE\tCONSTRUCTION TYPE\tFLOOR\tSQUARE METERS\tCONSTRUCTION YEAR\tPRICE\tLOCATION\tURL')
            file.write('\n')
            for row in self.curr.execute('SELECT * FROM properties_tb'):
                string_data = tuple(map(str, row))
                file.write('\t'.join(string_data))
                file.write('\n')
