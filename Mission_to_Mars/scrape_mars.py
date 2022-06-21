# Import Libraries
import os
import pandas as pd
import requests as request
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Chromedriver execution
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #URL path
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Save HTML and parser
    html = browser.html
    news_soup = bs(html, "html.parser")


    # Get the first news from the url 
    news_title = news_soup.find("div", class_="content_title").get_text()

    # 

