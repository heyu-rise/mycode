# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['moive.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        bs_in = BeautifulSoup(response.text, 'html.parser')
        title_list = bs_in.find_all('div', attrs={'class': 'hd'})
        for title in title_list:
            item = SpidersItem

        pass
