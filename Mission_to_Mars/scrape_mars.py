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
    news_soup


    # Get the first news from the url 
    news_title = news_soup.find("div", class_="content_title").get_text()
    news_title

    # Get the first paragraph of the news 
    news_p = news_soup.find("div", class_="article_teaser_body").get_text()
    news_p

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
    newpage_soup

    mars_image = newpage_soup.select_one('img.headerimage').get("src")
    mars_image

    featured_image_url = f'https://spaceimages-mars.com/{mars_image}'
    featured_image_url

    df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    df.head()

    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    df

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []

    links = browser.find_by_css('a.product-item img')

    for i in range(4):
        hemisphere = {}
    
        browser.find_by_css('a.product-item img')[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
        hemisphere['title'] = browser.find_by_css('h2.title').text
        hemisphere_image_urls.append(hemisphere)
    
        browser.back()

    hemisphere_image_urls 


        # DataBase dictionary
    mars_web_dict={
    'news_title': news_title, 'news_text': news_p,
    'featured_image_url': featured_image_url,
    'row1_title': table_data[0]['title'], 'row1_value': table_data[0]['value'],
    'row2_title': table_data[1]['title'], 'row2_value': table_data[1]['value'],
    'row3_title': table_data[2]['title'], 'row3_value': table_data[2]['value'], 
    'row4_title': table_data[3]['title'], 'row4_value': table_data[3]['value'], 
    'row5_title': table_data[4]['title'], 'row5_value': table_data[4]['value'], 
    'row6_title': table_data[5]['title'], 'row6_value': table_data[5]['value'], 
    'row7_title': table_data[6]['title'], 'row7_value': table_data[6]['value'], 
    'row8_title': table_data[7]['title'], 'row8_value': table_data[7]['value'], 
    'row9_title': table_data[8]['title'], 'row9_value': table_data[8]['value'],  
    'url1_title': hem_img_urls[0]['title'], 'url1_img': hem_img_urls[0]['img_url'],
    'url2_title': hem_img_urls[1]['title'], 'url2_img': hem_img_urls[1]['img_url'],
    'url3_title': hem_img_urls[2]['title'], 'url3_img': hem_img_urls[2]['img_url'],
    'url4_title': hem_img_urls[3]['title'], 'url4_img': hem_img_urls[3]['img_url']              
    }

    browser.quit()        





