# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanmoive.items import DoubanmoiveItem


class MoiveSpider(scrapy.Spider):
    name = 'moive'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(0, 1):
            url = f'https://movie.douban.com/top250?start={i * 25}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        bs_in = BeautifulSoup(response.text, 'html.parser')
        title_list = bs_in.find_all('div', attrs={'class': 'hd'})
        for titleItem in title_list:
            item = DoubanmoiveItem()
            title = titleItem.find('a').find('span').text
            link = titleItem.find('a').get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        # return items

    def parse2(self, response):
        item = response.meta['item']
        bs_in = BeautifulSoup(response.text, 'html.parser')
        content = bs_in.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item
