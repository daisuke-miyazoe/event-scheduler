from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from ...views import EventScraping


class Command(BaseCommand):
    help = "イベントのスクレイピング"

    def handle(self, *args, **options):
        driver = webdriver.Chrome()
        driver.get('https://eplus.jp/sf/venue/1020080/events')
        # # 武道館
        # res = requests.get('https://eplus.jp/sf/venue/1020080/events')
        # # res = requests.get('https://eplus.jp/sf/detail/0472810001-P0030020P021003?P1=0817')
        # soup = BeautifulSoup(res.text, 'html.parser')
        # # title_text = soup.find('title').get_text()
        # print(soup)

        # event_scraping = EventScraping()