# import all necessary dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser

def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # NASA Mars news website URL
        # splinter
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    
    #html object
    # soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #scrape title and text from latest news article, first article on top
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    return scrape