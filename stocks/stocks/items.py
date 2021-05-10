# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StockItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    date = scrapy.Field()
    closing_price = scrapy.Field()
    trading_date = scrapy.Field()
