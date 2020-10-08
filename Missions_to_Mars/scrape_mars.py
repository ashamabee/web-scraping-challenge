from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path':r'C:\Users\ashle\OneDrive\Desktop\chromedriver.exe'}
    return browser = Browser('chrome',**executable_path, headless=False)

def scrape():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    slides = soup.select_one('ul.item_list li.slide')

    news_title = slides.find("div",class_="content_title").text

    news_p = slides.find("div",class_="article_teaser_body").text

    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA01322_ip.jpg"

    url2 = 'https://space-facts.com/mars/'
    browser.visit(url2)

    html2 = browser.html
    soup = BeautifulSoup(html2,'html.parser')

    facts_table = pd.read_html(url2)
    facts = facts_table[0]

    facts=facts.set_index(0)

    facts.to_html()

    facts_soup = BeautifulSoup(html_facts, 'html.parser')

    return facts