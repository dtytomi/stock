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

        rows = response.xpath(
            '//table[@class="table table-striped table-bordered table-hover table-condensed"]/tbody/tr')


        for row  in rows:

            stock['company'] = row.xpath('td[1]/text()').get()
            stock['closing_price'] = row.xpath('td[5]/text()').get()
            stock['trading_date'] = response.css('span.sectional-heading::text').re(r'\d+\W\d+\W\d+')[0]
            
            x = datetime.datetime.now()
            stock['date'] = x.strftime("%Y-%m-%d %H:%M:%S")

            yield stock 
        