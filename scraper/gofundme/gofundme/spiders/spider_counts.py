import scrapy
import re
import json
from datetime import datetime


class CountsSpider(scrapy.Spider):
    name = "counts"

    with open("test1000/1000counts.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    # start_urls = ['https://gateway.gofundme.com/web-gateway/v1/feed/angel-yang-cassidy-yang/counts']

    def parse(self, response):
        data = json.loads(response.text)
        counts = data['references']['counts']
        dj = {
            "counts":counts,
            "url":response.request.url.replace("https://gateway.gofundme.com/web-gateway/v1/feed/", "https://www.gofundme.com/f/").replace("/counts", ""),
            "data_date": str(datetime.now())
        }
        yield dj
