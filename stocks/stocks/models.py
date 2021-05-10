from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.engine import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, SmallInteger, String, Date, DateTime, Float,
                        Boolean, Text, LargeBinary)
import datetime

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """ 
    Performs Database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """

    return create_engine(get_project_settings().get("CONNECTION_STRING"), pool_recycle=3600)


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class PensionDB(DeclarativeBase):
    """Sqlalchemy model"""
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)
    company = Column('company', Text())
    closing_price = Column('closing_price', Text())
    trading_date = Column('trading_date', Text())
    date = Column('date', DateTime, default = datetime.datetime.utcnow, nullable=True)  