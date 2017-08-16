# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from realtor.items import RealtorItem


class EstateSpider(scrapy.Spider):
    name = 'estateSpider'
    allowed_domains = ['www.realtor.com']
    start_urls = ['https://www.realtor.com/realestateandhomes-search/Houston_TX']
    self.pagination_index = 1

    def parse(self, response):
        origin_page_urls = response.css('div.srp-item-ldp-link.hidden-xs.hidden-xxs > a.btn.btn-default ::attr(href)')\
            .extract()
        base_url = 'https://www.realtor.com/'
        for link in origin_page_urls:
            absolute_url = urljoin(base_url,link)
            print(absolute_url)
            yield Request(absolute_url, callback=self.parse_detail_page,
                          meta={})

        self.pagination_index += 1
        next_pagination_url =

    def parse_detail_page(self, response):
        item = RealtorItem()
        item['beds'] = response.css("#ldp-property-meta > ul > li:nth-child(1) > span ::text").extract()
        item['baths'] = response.css('#ldp-property-meta > ul > li.property-baths-count span ::text').extract()
        item['full_baths'] = response.css('#ldp-property-meta > ul > li:nth-child(2) > div:nth-child(1) > span ::text').extract()
        item['half_baths'] = response.css('#ldp-property-meta > ul > li:nth-child(2) > div:nth-child(2) > span ::text').extract()
        item['sq_ft'] = response.css('#ldp-property-meta > ul > li:nth-child(3) > span ::text').extract()
        item['sq_ft_lot'] = response.css('#ldp-property-meta > ul > li:nth-child(4) > span ::text').extract()
        item['price'] = response.css('#ldp-pricewrap > div > div > span ::text').extract()
        item['photo_amount'] = response.css("#hero-view-photo > span:nth-child(4) ::text").extract()
        item['type'] = response.css('.key-fact-data')[3].css("::text").extract()
        item['built'] = response.css('.key-fact-data')[4].css("::text").extract()
        item['description'] = response.css("#ldp-detail-romance ::text").extract()
        yield item

    def parse_next_page(self,response):
        next_url = response.css("#ResultsPerPageBottom > nav > span.next > a ::attr(href)").extract()
