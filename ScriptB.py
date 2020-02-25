import scrapy
class NewSpider(scrapy.Spider):
 name = "myCrawler"
 start_urls = ['http://172.17.50.43']
