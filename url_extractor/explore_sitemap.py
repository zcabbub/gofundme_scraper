# Import selenium
import io

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from os import mkdir, listdir, remove
import shutil
import gzip
import time
import xml.etree.ElementTree as etree
import csv


# Helper functions
def get_counts_url(url):
    first_part = 'https://gateway.gofundme.com/web-gateway/v1/feed/'
    last_part = '/' + 'counts'

    middle_part = url.replace('https://www.gofundme.com/f/', '')

    api_url = first_part + middle_part + last_part

    return api_url


def write(list_chunks, html):
    if html:
        for part in range(0, 3):
            with io.open('urls/html_urls_{part}.txt'.format(part=part), 'w', encoding="utf-8") as f:
                f.writelines('\n'.join(list_chunks[part]))
    else:
        for part in range(0, 3):
            with io.open('urls/counts_urls_{part}.txt'.format(part=part), 'w', encoding="utf-8") as f:
                f.writelines('\n'.join(list_chunks[part]))


def split(a, n):
    k, m = divmod(len(a), n)
    return list(a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


root = listdir()
if "sitemaps" in root:
    shutil.rmtree("sitemaps/")
mkdir("sitemaps/")

# To launch in headfull mode, comment out these options
options = ChromeOptions()
# NEEDS TO NOT BE HEADLESS
options.add_argument("--window-size=1920,1080")
options.add_argument("--log-level=3")  # fatal

options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\UCL053368\Documents\Research\Enrico\Scraper\url_extractor\sitemaps",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

print('Starting to SCRAPE the sitemap...')
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://www.gofundme.com/sitemap.xml")
driver.maximize_window()

sitemap_lastMod = driver.find_element_by_tag_name("lastmod").get_attribute("innerHTML")

xmlGzLocations = driver.find_elements_by_tag_name("loc")
xmlGzLinks = []
for location in xmlGzLocations:
    text = location.get_attribute("innerHTML")
    if text != "https://www.gofundme.com/sitemaps/sitemap_marketing.xml.gz" and ("34" in text):
        xmlGzLinks.append(text)

print('Downloading the .gz archived files...')
for link in xmlGzLinks:
    driver.get(link)

time.sleep(5)
driver.close()

print('Extracting the HTML urls')
html_urls = []
sitemaps = listdir("sitemaps/")
for sitemap in sitemaps:
    with gzip.open("sitemaps/" + sitemap, "r") as gzXmlFile:
        xml = etree.parse(gzXmlFile)
        gzXmlFile.close()

        root = xml.getroot()
        for url in root:
            loc = url[0]
            lastmod = url[1]
            linkData = loc.text
            html_urls.append(linkData)
print('Done.')

print('Creating the COUNTS urls')
counts_urls = [get_counts_url(url) for url in html_urls]
print('Done')

print('Splitting the urls...')
html_chunks = split(html_urls, 3)
counts_chunks = split(counts_urls, 3)
print('Done.')

print('Writing HTML urls...')
write(html_chunks, True)
print('Done.')

print('Writing COUNTS urls...')
write(counts_chunks, False)
print('Done.')
