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

    # Get the first paragraph of the news 
    news_p = news_soup.find("div", class_="article_teaser_body").get_text()

    #JPL Mars Space Images—Featured Image
    # URL path
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    image_soup = bs(html, "html.parser")

    image_soup = browser.find_by_tag('button')[1]
    image_soup.click()

    html = browser.html
    newpage_soup = bs(html, "html.parser")
  
    mars_image = newpage_soup.select_one('img.headerimage').get("src")
  

    featured_image_url = f'https://spaceimages-mars.com/{mars_image}'
   

    df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    df.head()

    table_data = df.values.tolist()
  

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hem_img_urls = []

    links = browser.find_by_css('a.product-item img')

    for i in range(4):
        hemisphere = {}
    
        browser.find_by_css('a.product-item img')[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
        hemisphere['title'] = browser.find_by_css('h2.title').text
        hem_img_urls.append(hemisphere)
    
        browser.back()

    hem_img_urls 

    browser.quit()        





