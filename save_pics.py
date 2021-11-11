import os
import urllib.request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs


class ImageScraper:
    def __init__(self, url, download_path):
        self.url = url
        self.download_path = download_path
        self.session = requests.Session()

    def scrape_images(self):
        path = self.download_path
        html = urlopen(self.url)
        bs4 = Bs(html, 'html.parser')
        images = bs4.find_all('img', {})

        for image in images:
            # get the img url
            img_url = image.get('src').replace('\\', '/')
            real_url = "http://www.photobirdireland.com/" + img_url
            print(real_url)
            # get the image name
            img_name = str(img_url.split('/')[-1])
            print(img_name)
            print("downloading {}".format(img_url))
            urllib.request.urlretrieve(real_url, os.path.join(path, img_name))


scraper = ImageScraper(
    url="http://www.photobirdireland.com/garden-birds.html", download_path=r"F:\Test")
scraper.scrape_images()