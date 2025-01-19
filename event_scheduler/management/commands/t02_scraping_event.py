from datetime import datetime
import time
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from ...views import EventScraping


class Command(BaseCommand):
    help = "イベントのスクレイピング"

    def handle(self, *args, **options):
        today = datetime.today()
        formatted_today = today.strftime("%-m/%-d")
        print(formatted_today)

        driver = webdriver.Chrome()
        # 武道館
        driver.get('https://eplus.jp/sf/venue/1020080/events')
        time.sleep(10)
        dates = driver.find_elements(By.CLASS_NAME, "ticket-item__mmdd")
        full_texts = [date.text for date in dates]
        print(full_texts)
        date_texts = [full_text.split("(")[0] for full_text in full_texts]
        print(date_texts)

        if formatted_today in date_texts:
            index_num = date_texts.index(formatted_today)
            print(index_num)
            link = driver.find_elements(By.CLASS_NAME, "ticket-item--kouen")[index_num]
            print(link)
            time.sleep(10)
            link.click()
            title = driver.find_element(By.CLASS_NAME, "s4-main-title").text
            print(title)
            event_title = title.split("(")[0]
            print(event_title)
            date_text = driver.find_element(By.CLASS_NAME, "block-ticket-article__date").text
            date_t = date_text.split("(")[0]
            time_text = driver.find_element(By.CLASS_NAME, "block-ticket-article__time").text
            time_t = time_text.split("：")[1].split("～")[0]
            start_date_time = date_t + ' '+ time_t
            print(start_date_time)

            event_scraping = EventScraping()
            event_scraping.import_event(
                event_title=event_title,
                start_date=start_date_time
            )

        # # 武道館
        # res = requests.get('https://eplus.jp/sf/venue/1020080/events')
        # # res = requests.get('https://eplus.jp/sf/detail/0472810001-P0030020P021003?P1=0817')
        # soup = BeautifulSoup(res.text, 'html.parser')
        # # title_text = soup.find('title').get_text()
        # print(soup)

        # event_scraping = EventScraping()
