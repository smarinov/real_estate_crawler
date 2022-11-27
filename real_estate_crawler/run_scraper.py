from real_estate_crawler.real_estate_crawler.spiders.real_estate_spider import RealEstateSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'real_estate_crawler.real_estate_crawler.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = RealEstateSpider

    def run_spiders(self):
        self.process.crawl(self.spider)
        self.process.start()