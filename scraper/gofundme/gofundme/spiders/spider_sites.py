import scrapy
import re
import json
from datetime import datetime
import pkgutil


class HtmlSpider(scrapy.Spider):
    name = "sites"
    data = str(pkgutil.get_data("gofundme", "2020_urls/html_urls_0.txt"), 'utf-8')
    start_urls = [url for url in data.split('\n')]
    start_urls = start_urls[:10]

    # with open("test1000/1000htmls.txt", "rt") as f:
    #     start_urls = [url.strip() for url in f.readlines()]

    #start_urls = ['https://www.gofundme.com/f/angel-yang-cassidy-yang']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={
                "proxy": "http://lum-customer-a_bubutanu-zone-gofundme_com:GFMscraper1@zproxy.lum-superproxy.io:22225"})

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
