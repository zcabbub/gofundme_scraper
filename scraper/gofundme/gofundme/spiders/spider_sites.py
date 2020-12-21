import scrapy
import re
import json
from datetime import datetime


class HtmlSpider(scrapy.Spider):
    name = "sites"

    with open("test1000/1000htmls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    #start_urls = ['https://www.gofundme.com/f/angel-yang-cassidy-yang']

    def parse(self, response):
        data = re.findall("<script>window.initialState =(.+?);</script>", response.body.decode("utf-8"), re.S)
        jsn = {
        "url": response.url,
        "data_date": str(datetime.now()),
        "category": response.css('.m-campaign-byline-type::text').get(),
        "category_URL": response.css('.m-campaign-byline-type::attr(href)').get(),
        "data": json.loads(data[0])['feed']['campaign'],
        }
        yield jsn
