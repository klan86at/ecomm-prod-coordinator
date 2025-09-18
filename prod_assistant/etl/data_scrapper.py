# Libraries
import csv
import time
import re
import os
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class FlipkartScrapper:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def get_top_reviews(self, product_url, count=2):
        pass
    def scrape_flipkart_products(self, query, max_products=1, review_counts=2):
        pass
    def save_to_csv(self, data, filename="product_reviews.csv"):
        pass

