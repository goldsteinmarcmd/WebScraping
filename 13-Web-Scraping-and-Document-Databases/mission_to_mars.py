from bs4 import BeautifulSoup
import requests
import re
from splinter import Browser
import pandas as pd

# URL of Python reddit
url = 'http://mars.nasa.gov/news/'

# Retrieve page with the requests module

browser = Browser('chrome', headless=False)
browser.visit(url)

# Retrieve page with the requests module
response = requests.get(url)

# results are# Loop through returned results

    # HTML object
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book informationt
results = soup.find_all('ul', class_="item_list")
    # Retrieve all elements that contain book information
for result in results:
    htitle = soup.find('div', class_='content_title').text.strip()
    p = soup.find('div', class_='article_teaser_body').text.strip()
# {"class":"wrapper"}
    print(htitle)
    print("\n")
    print(p)
    print("\n")

### JPL Mars Space Images - Featured Image

url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

# Retrieve page with the requests module

browser = Browser('chrome', headless=False)
browser.visit(url2)

# Retrieve page with the requests module
response = requests.get(url2)

# results are# Loop through returned results

    # HTML object
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book informationt
results = soup.find_all('div', class_="carousel_items")
    # Retrieve all elements that contain book information
for result in results:
    imgurl = result.article['style']
    print(imgurl)

### Mars Weather
twitterurl = 'https://twitter.com/marswxreport?lang=en'

# Retrieve page with the requests module

browser = Browser('chrome', headless=False)
browser.visit(twitterurl)

# Retrieve page with the requests module
response = requests.get(twitterurl)

# results are# Loop through returned results

    # HTML object
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book informationt
results = soup.find('div', class_="js-tweet-text-container")
    # Retrieve all elements that contain book information
for result in results:
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
    print(mars_weather)

### Mars Facts

pandasurl = 'http://space-facts.com/mars/'

# Retrieve page with the requests module

browser = Browser('chrome', headless=False)
browser.visit(pandasurl)

# Retrieve page with the requests module
response = requests.get(pandasurl)

tables = pd.read_html(pandasurl)
tables

df = tables[0]
df.columns = ['Metric', 'Value',
              ]
df.head()

html_table = df.to_html()
print(html_table)

### Mars Hemisperes

hemiurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# Retrieve page with the requests module

browser = Browser('chrome', headless=False)
browser.visit(hemiurl)

# Retrieve page with the requests module
response = requests.get(hemiurl)

value_stores = ['img', 'title']

# results are# Loop through returned results

    # HTML object
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book informationt
results = soup.find('a', class_="itemLink product-item")
    # Retrieve all elements that contain book information
for result in results:
    img_url = soup.find('img', 'src')
    print(img_url)

    