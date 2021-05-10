import scrapy
import logging
import datetime
from stocks.items import StockItem

class StocksSpider(scrapy.Spider):

    name = "stocks"

    rotate_user_agent = True

    start_urls = [
        'https://aptsecurities.com/nse-daily-price.php',
    ]


    def parse(self, response):

        stock = StockItem()


        for row in response.css('table.table tbody tr'):

            stock['company'] = row.css('td::text').get()
            stock['closing_price'] = row.css('td::text')[5].get()
            stock['trading_date'] = response.css('span.sectional-heading::text').re(r'\d+\W\d+\W\d+')[0]
            
            x = datetime.datetime.now()
            stock['date'] = x.strftime("%Y-%m-%d %H:%M:%S")

            yield stock 
        