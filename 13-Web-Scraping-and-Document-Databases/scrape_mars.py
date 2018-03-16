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

# ### Mars Hemisperes

# hemiurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# # Retrieve page with the requests module

# browser = Browser('chrome', headless=False)
# browser.visit(hemiurl)

# # Retrieve page with the requests module
# response = requests.get(hemiurl)

# value_stores = ['img', 'title']

# # results are# Loop through returned results

#     # HTML object
# html = browser.html
#     # Parse HTML with Beautiful Soup
# soup = BeautifulSoup(html, 'html.parser')
#   # Retrieve all elements that contain book informationt
# results = soup.find('a', class_="itemLink product-item")
#     # Retrieve all elements that contain book information
# for result in results:
#     img_url = soup.find('img', 'src')
#     print(img_url)

# import necessary libraries
from flask import Flask, render_template
import pymongo

# create instance of Flask app
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Use database and create it if it does not exist
db = client.marsdb

# create route that renders index.html template
@app.route("/")
def scrape():
    htitle_dict = htitle.to_dict()
    p_dict = p.to_dict()
    imgurl_dict = imgurl.to_dict()
    mars_weather_dict = mars_weather.to_dict()
    html_table_dict = html_table.to_dict()

    mars_dictionary = {"htitle": "htitle_dict",
                            "p": "p_dict"}
    return render_template("index.html", mars_dict=mars_dictionary)
    print('hello marc eroigjeroigweofioeorg')
    print(mars_dict)

if __name__ == "__main__":
    app.run(debug=True)
