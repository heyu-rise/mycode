# -*- coding: utf-8 -*-
import scrapy


class RandomSpider(scrapy.Spider):
    name = 'random'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)


