import time

import scrapy
import unicodedata
from scrapy import signals

from ..items import RealEstateCrawlerItem


class RealEstateSpider(scrapy.Spider):
    name = 'RealEstate'
    URL = input('Please input your "ALO.BG" link here: ')

    start_urls = [
        URL,
    ]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(RealEstateSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def parse(self, response, **kwargs):
        property_page_links = ['https://www.alo.bg' + x for x in response.xpath("//div[contains(@class, 'item-header')]").css('a::attr("href")').getall()]

        yield from response.follow_all(property_page_links, self.parse_property_data)

        pagination_links = response.xpath('//a[@rel="next"]/@href')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_property_data(self, response):
        items = RealEstateCrawlerItem()

        def extract_with_xpath(query):
            result = response.xpath(query).getall()

            if not result:
                return ['No Data']

            return result

        title = unicodedata.normalize('NFKD', extract_with_xpath('.//h1/text()')[0].strip())
        construction_type = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Вид строителство')]//following-sibling::div[1]/span/text()")[0].strip())
        floor = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Номер на етажа')]//following-sibling::div[1]/span/text()")[0].strip())
        square_meters = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Квадратура')]//following-sibling::div[1]/span/text()")[0].strip())
        construction_year = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Година на строителство')]//following-sibling::div[1]/span/text()")[0].strip())
        price = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Цена')]//following-sibling::div[1]/text()")[0].strip())
        location = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Местоположение')]//following-sibling::div[1]/text()")[0].strip())
        listing_id = unicodedata.normalize('NFKD', extract_with_xpath("//div[contains(text(), 'Обява №')]//following-sibling::div[1]/text()")[0].strip())
        url = response.request.url

        items['listing_id'] = listing_id
        items['title'] = title
        items['construction_type'] = construction_type
        items['floor'] = floor
        items['square_meters'] = square_meters
        items['construction_year'] = construction_year
        items['price'] = price
        items['location'] = location
        items['url'] = url
        yield items

    def spider_opened(self, spider):
        print(f'"{spider.name}" started crawling. This may take a while.')

    def spider_closed(self, spider):
        print(f'"{spider.name}" has successfully finished.')