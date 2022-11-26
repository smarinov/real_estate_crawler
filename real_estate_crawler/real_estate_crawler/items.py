# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateCrawlerItem(scrapy.Item):
    listing_id = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    construction_type = scrapy.Field()
    floor = scrapy.Field()
    square_meters = scrapy.Field()
    construction_year = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()


