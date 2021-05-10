# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
from sqlalchemy.orm import sessionmaker
from stocks.models import PensionDB, db_connect, create_table

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StocksPipeline:
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    """docstring for JsonPipeline"""
    def open_spider(self, spider):
        self.file = open('item.json', 'w')

    def close_spider(self, spider):
        self.file.close()
    
    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item


class DatabasePipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates pension table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save pensions in the database.
        This method is called for every item pipeline component.
        """

        session = self.Session()
        pensiondb = PensionDB()
        pensiondb.company = item['company']
        pensiondb.closing_price = item['closing_price']
        pensiondb.trading_date = item['trading_date']
        pensiondb.date = item['date']
        
        try:
            session.add(pensiondb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item