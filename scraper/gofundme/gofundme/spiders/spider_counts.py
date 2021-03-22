import scrapy
import re
import json
from datetime import datetime
import pkgutil


class CountsSpider(scrapy.Spider):
    name = "counts"
    counter = 0
    data = str(pkgutil.get_data("gofundme", "2020_urls/counts_urls_0.txt"), 'utf-8')
    start_urls = [url for url in data.split('\n')]
    start_urls = start_urls[:10]


    # with open("test1000/1000counts.txt", "rt") as f:
    #     start_urls = [url.strip() for url in f.readlines()]

    # start_urls = ['https://gateway.gofundme.com/web-gateway/v1/feed/angel-yang-cassidy-yang/counts']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={
                "proxy": "http://lum-customer-a_bubutanu-zone-gofundme_com:GFMscraper1@zproxy.lum-superproxy.io:22225"})

    def parse(self, response):
        self.counter = self.counter+1
        data = json.loads(response.text)
        counts = data['references']['counts']
        dj = {
            "counter" : self.counter,
            "counts":counts,
            "url":response.request.url.replace("https://gateway.gofundme.com/web-gateway/v1/feed/", "https://www.gofundme.com/f/").replace("/counts", ""),
            "data_date": str(datetime.now())
        }

        yield dj
