# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class RealtorItem(scrapy.Item):
    origin_URL = Field()
    address = Field()
    beds = Field()
    baths = Field()
    full_baths = Field()
    half_baths = Field()
    sq_ft = Field()
    sq_ft_lot = Field()
    price = Field()
    photo_amount = Field()
    #photo_download_file = Field()
    built = Field()
    type = Field()
    description = Field()

