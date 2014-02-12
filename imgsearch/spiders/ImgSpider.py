import scrapy.spider

import imgsearch.settings
import imgsearch.items

class ImgSearchSpider(scrapy.spider.Spider):
    name = "imgsearch"
    allowed_domains = imgsearch.settings.DOMAIN

    def __init__(self, search='cats', *args, **kwargs):
        super(ImgSearchSpider, self).__init__(*args, **kwargs)
        search = search.replace(' ', '+')
        self.start_urls = [imgsearch.settings.BASE_URL % search]

    def parse(self, response):
        selector = scrapy.selector.Selector(response)
        image_urls = selector.xpath('//div//img/@src').extract()
        item = imgsearch.items.ImgItem()
        item['image_urls'] = image_urls
        return [item]
