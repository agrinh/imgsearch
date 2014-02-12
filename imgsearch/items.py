import scrapy.item

class ImgItem(scrapy.item.Item):
    image_urls = scrapy.item.Field()
    images = scrapy.item.Field()
