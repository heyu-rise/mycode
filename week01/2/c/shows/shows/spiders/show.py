# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from shows.items import ShowsItem


class ShowSpider(scrapy.Spider):
    name = 'show'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        urls = (f'https://movie.douban.com/top250?start={i * 25}' for i in range(0, 1))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.url)
        moives = Selector(response=response).xpath('//div[@class="hd"]')
        for moive in moives:
            item = ShowsItem()
            title = moive.xpath('./a/span/text()')
            link = moive.xpath('./a/@href')
            print('-----------------')
            title = title.extract_first().strip()
            link = link.extract_first().strip()
            print(title)
            print(link)
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        info = Selector(response=response).xpath('//*[@id="link-report"]/span/text()')
        content = info.extract_first().strip()
        item['content'] = content
        yield item

