# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import KonachanItem


class KonachanSpiderSpider(CrawlSpider):
    name = 'Konachan_spider'
    allowed_domains = ['konachan.net']
    start_urls = ['http://konachan.net/post?page=1&tags=']

    rules = (
        Rule(LinkExtractor(allow=r'.+/post.+page=\d+.+tags='), follow=True),
        Rule(LinkExtractor(allow=r'http://konachan.net/post/show/.+'), callback="parse_item", follow=False),
    )

    def myprint(self, value):
        print("="*30)
        print(value)
        print("="*30)

    def parse_item(self, response):
        image_urls = response.xpath("//div[@class='content']//img/@src").getall()
        item = KonachanItem(image_urls=image_urls)
        return item
