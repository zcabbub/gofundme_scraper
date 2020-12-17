import scrapy
import re
import json
from datetime import datetime


class HtmlSpider(scrapy.Spider):
    name = "sites"

    start_urls = ['https://www.gofundme.com/f/angel-yang-cassidy-yang']

    def parse(self, response):
        data = re.findall("<script>window.initialState =(.+?);</script>", response.body.decode("utf-8"), re.S)
        dj = data[0]
        dj = json.loads(dj)
        dj["url"] = response.request.url
        dj["date_time"] = str(datetime.now())
        dj["category_text"] = response.css('.m-campaign-byline-type::text').get()
        dj["category_URL"] = response.css('.m-campaign-byline-type::attr(href)').get()
        yield dj
