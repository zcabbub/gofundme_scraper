import scrapy
import re
import json
from datetime import datetime

class TestFundSpider(scrapy.Spider):
    name = "counts"

    start_urls = ['https://gateway.gofundme.com/web-gateway/v1/feed/angel-yang-cassidy-yang/counts']

    def parse(self, response):
        data = json.loads(response.text)
        counts = data['references']['counts']
        dj = {
            "counts":counts,
            "url":response.request.url.replace("https://gateway.gofundme.com/web-gateway/v1/feed/", "https://www.gofundme.com/f/").replace("/counts", ""),
            "date_time": str(datetime.now())
        }
        yield dj
