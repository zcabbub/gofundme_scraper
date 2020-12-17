import scrapy
import re
import json
from datetime import datetime

class TestFundSpider(scrapy.Spider):
    name = "counts"

    #with open("./URLS/URLS_500.txt", "rt") as f:
    #    start_urls = [
    #        url.strip().replace("https://www.gofundme.com/f/", "https://gateway.gofundme.com/web-gateway/v1/feed/") + "/counts" for url in f.readlines()
    #        ]


    def parse(self, response):
        data = json.loads(response.text)
        counts = data['references']['counts']
        dj = {
            "counts":counts,
            "url":response.request.url.replace("https://gateway.gofundme.com/web-gateway/v1/feed/", "https://www.gofundme.com/f/").replace("/counts", ""),
            "date_time": str(datetime.now())
        }
        yield dj
