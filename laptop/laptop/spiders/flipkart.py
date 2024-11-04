import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.loader import ItemLoader
from laptop.items import LaptopItem

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com/search?q=lap&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"]

    def start_requests(self):
        # GET request
        yield scrapy.Request(self.start_urls[0], meta={"playwright": True, "playwright_page_methods": [
                PageMethod("wait_for_timeout", 1000) ]})  # waiting for 1 second just to make sure page is loaded
            

    def parse(self, response):
        laptops = response.css('div.tUxRFH')
        for i in laptops:
            flip_item = ItemLoader(item=LaptopItem() , selector=i)
            flip_item.add_css('title' , 'div.KzDlHZ::text')
            flip_item.add_css('rating' , 'div._5OesEi div.XQDdHH::text')
            flip_item.add_css('Details' , 'div._6NESgJ ul.G4BRas li::text')
            flip_item.add_css('price' , 'div.hl05eU div._4b5DiR::text')
            yield flip_item.load_item()

            # title =  i.css('div.KzDlHZ::text').get()
            # rating = i.css('div._5OesEi div.XQDdHH::text').get()
            # Details = i.css('div._6NESgJ ul.G4BRas li::text').getall()
            # price = i.css('div.hl05eU div._4b5DiR::text').get()
            
            # laptop_details = {
            #     'title' : title , 
            #     'rating' : rating , 
            #     'Detsils' : Details , 
            #     'price' : price
            # }
            # yield laptop_details 

    




       

