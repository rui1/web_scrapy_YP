# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapyYpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class YPItem(scrapy.Item):
    YPrank = scrapy.Field()
    YPimglink = scrapy.Field()
    menuLink = scrapy.Field()
    businessName = scrapy.Field()
    YPreveiwStar=scrapy.Field()
    YPreviewNum= scrapy.Field()
    streetAddress = scrapy.Field()
    addressLocality = scrapy.Field()
    addressRegion = scrapy.Field()
    postalCode = scrapy.Field()
    addressTotal = scrapy.Field()
    telephone=scrapy.Field()
    categories = scrapy.Field()
    website = scrapy.Field()
    directions = scrapy.Field()
    more_info = scrapy.Field()
    yp_ad = scrapy.Field()


