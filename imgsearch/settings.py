# Scrapy settings for imgsearch project
#

BOT_NAME = 'imgsearch'

SPIDER_MODULES = ['imgsearch.spiders']
NEWSPIDER_MODULE = 'imgsearch.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT          = "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0"
DEFAULT_ITEM_CLASS  = 'imgsearch.items.ImgItem'

# ImgSearchSpider
BASE_URL = 'https://www.google.com/search?q=%s&tbm=isch'
DOMAIN = 'https://www.google.com'

# Image settings
DOWNLOAD_DELAY      = 1
IMAGES_MIN_HEIGHT   = 10
IMAGES_MIN_WIDTH    = 10
IMAGES_STORE        = './captured/'
ITEM_PIPELINES      = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
