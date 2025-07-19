from django.core.management.base import BaseCommand
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
logger = logging.getLogger(__name__)


from Task02_01_00_News_Page_App.models import News, Tag

class Command(BaseCommand):
    help = 'Run Zoomit Scraper with Selenium and save news to DB'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting Zoomit Scraper"))
        driver = webdriver.Chrome()

        try:
            driver.get("https://www.zoomit.ir/search/news/")
            time.sleep(3)

            counter = 0
            while counter <= 5:
                try:
                    button_view_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
                        By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul/button/div"
                    )))
                    button_view_more.click()
                    time.sleep(10)
                    counter += 1
                except Exception as exc:
                    print("Erro for button view more.")
                    logger.error("An Error occurred: %s", str(exc))
                    break


            page_source = driver.page_source
            scrapy_selector = Selector(text=page_source)
            news_page_link =  scrapy_selector.xpath("//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul//li/div/div/div/div/a/@href").getall()

            for news_page_link_follow in news_page_link:                
                self.scrape_article(driver, news_page_link_follow)

        finally:
            driver.quit()
            self.stdout.write(self.style.SUCCESS("Scraper finished."))

    def scrape_article(self, news_page_driver, news_page_url_source):
        news_page_driver = webdriver.Chrome()
        news_page_driver.get(news_page_url_source)
        time.sleep(3)
        news_page_response = Selector(text=news_page_driver.page_source)

        news_page_header = news_page_response.xpath("//*[@id='__next']/div[2]/div[1]/main/article/header/div/div")
        
        news_page_title = news_page_header.xpath(".//h1/text()").get()
        news_page_date = news_page_header.xpath(".//div[2]/span[1]/text()").get()
        news_page_author = news_page_header.xpath(".//div[3]/a/div/span/text()").get()
        news_page_tags = news_page_header.xpath(".//div[2]/div[1]/a/span/text()").getall()
        news_page_content = news_page_response.xpath("//*[@id='__next']/div[2]/div[1]/main/article/div/div[5]/div/div/div/p/text()").getall()
                                                      //*[@id='__next']/div[2]/div[1]/main/article/div/div[5]/div/div/div/p/text()

        if not news_page_title or not news_page_content:
            logger.warning(f"Skipping article: Missing title or content in {news_page_url_source}")
            return

        tag_list = []
        for tag in news_page_tags:

            if tag.strip():
                tag_obj, _ = Tag.objects.get_or_create(tag_name=tag)
                tag_list.append(tag_obj)

        news_obj, created = News.objects.get_or_create(
            news_title=news_page_title,
            defaults={
                "news_content": " ".join(news_page_content),
                "news_source": news_page_url_source,
            }
        )
        if created:
            news_obj.news_tags.set(tag_list)
            news_obj.save()
