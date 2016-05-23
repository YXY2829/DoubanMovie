# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem

class Top250movieSpider(Spider):
    name = "top250movie"
    download_delay = 1
    allowed_domains = ["movie.douban.com"]
    start_urls=["https://movie.douban.com/top250?start=%d"% i for i in range(0,251,25)]

    def parse(self,response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="item"]/div[@class="info"]')
        items = []
        for site in sites:
            item = DoubanmovieItem()
            item['title'] = site.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0].extract()
            item['rating_num'] = site.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['link'] = site.xpath('div[@class="hd"]/a/@href').extract()
            items.append(item)
            yield item
		
		

