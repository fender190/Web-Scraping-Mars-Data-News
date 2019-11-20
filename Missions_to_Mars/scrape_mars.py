# import all necessary dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser

def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    ### NASA Mars News

    # NASA Mars news website URL
        # splinter
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    #html object
    # soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #scrape title and text from latest news article, first article on top
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text



    ### JPL Mars Space Images-Featured Images

    # Mars Space Images website URL
    #splinter
    mars_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_images_url)

    #html object
    # soup
    html_image = browser.html
    soup = bs(html_image, 'html.parser')

    # Find Image URL
    # Website URL
    image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    nasa_url = 'https://www.jpl.nasa.gov'

    # both URLs concatenated to get exact feature image URL
    featured_image_url = nasa_url + image_url



    ### Mars Weather Twitter

    # Mars Weather Twitter account URL
    # splinter
    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)

    #html object
    #soup
    html_weather = browser.html
    soup = bs(html_weather,'html.parser')

    # Collect all latest tweets
    last_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Use weather related words to exclude all other tweets
    for tweet in last_tweets: 
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet:
            mars_weather = weather_tweet




    #### Mars Facts

    # Mars Facts url
    # read html using pandas
    mars_facts_url = 'https://space-facts.com/mars/'
    fact_tables = pd.read_html(mars_facts_url)

    # get first table
    # change column numbers for column names 'description' and 'values'
    facts_df = fact_tables[0]
    facts_df.columns = ['description','values']

    # set index
    # save as html
    mars_facts_df = facts_df.set_index('description')
    mars_facts_html = mars_facts_df.to_html('mars_facts.html')




    ### Mars Hemispheres

    # Mars Hemispheres URL
    # splinter
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)

    #html object
    #soup
    hemispheres_html = browser.html
    soup = bs(hemispheres_html, 'html.parser')

    # use soup to find all urls with mars info
    # list to store all required URLs
    # main url, from usgs.gov
    items_url = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    hemisphere_url = 'https://astrogeology.usgs.gov'

    #loop through each item
    # retrieve image's url
    # use splinter to access every direct image url
    # get html and parse with soup
    # combined loops
    for i in items_url:
        titles = i.find('h3').text
        # partial URL
        images_url = i.find('a', class_='itemLink product-item')['href']
    
        # splinter
        browser.visit(hemisphere_url + images_url)
    
        # html object
        images_html = browser.html
    
        # soup 
        soup = bs(images_html,'html.parser')
    
        # Retrieve full image source 
        img_url = hemisphere_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : titles, "img_url" : img_url})


    ### All scraped data, placed into a dictionary 
    scraped_mars_data = {
            "news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "mars_weather": mars_weather,
            "mars_facts_html": mars_facts_html,
            "hemisphere_image_urls": hemisphere_image_urls
            }
    return scraped_mars_data