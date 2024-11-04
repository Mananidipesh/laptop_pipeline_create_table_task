# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose , TakeFirst
from w3lib.html import remove_tags
import re


def convertor(val):
    try:
        return (float(val))
    except:
        return 0
    
def convert_price(val):
    try:
        return re.sub(r'[₹,]', '', val)
    except:
        '0'


class LaptopItem(scrapy.Item):
    title = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    rating = scrapy.Field(input_processor = MapCompose(remove_tags,convertor),output_processor = TakeFirst())
    Details = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,convert_price,convertor),output_processor = TakeFirst())
    # define the fields for your item here like:
    # name = scrapy.Field()
    
