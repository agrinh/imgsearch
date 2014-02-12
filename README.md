imgsearch
=========

Download images in search result using scrapy

Does an imgsearch on google and downloads all images found on the first page. Images are saved to captured/ .
E.g. to download images of cats, do:
>>> scrapy crawl imgsearch -a search=cats

Requires scrapy.
