import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllproductsSpider(CrawlSpider):
    name = 'AllProducts'
    allowed_domains = ['www.webscraper.io']
    start_urls = ['https://www.webscraper.io/test-sites/e-commerce/static/computers/laptops?fbclid=IwAR0Q5k8H779qsVmQ536batIZ4qh7c1UqiaZ1h6uteL8udcHcGGbeIVr59zA/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='col-sm-4 col-lg-4 col-md-4']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@rel='next']"))
    )


    def parse_item(self, response):
        yield{
            "Product Title": response.xpath("(//div[@class='caption']/h4)[2]/text()").get(),
            "Product Description" : response.xpath("//p[@class='description']/text()").get()
        }
