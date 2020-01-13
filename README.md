

# Web Scraping - Mission to Mars



A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

### Languages Used

Python on a Jupyter Notebook using BeautifulSoup, Pandas, and Requests/Splinter libraries.

NoSQL for MongoDb database.

HTML to create a simple web page.

### Steps
* Web-Scraped data using chromedriver & Request/Splinter to navigate through multiple sites. and BeautifulSoup on a Jupyter notebook.

* Data was scraped from multiple websites related to the Mission To Mars: 

    Mars Mission Latest News - [NASA Mars News Site](https://mars.nasa.gov/news/)
    
    Mars Planet Images - [Mars_Images](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    
    Mars Latest Weather - [Mars_Weather](https://twitter.com/marswxreport?lang=en)
    
    Facts about the Mars Planet [Mars Facts](https://space-facts.com/mars/)
    
    Images of Mar's Hemispheres (HD) [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    

* Used Python on a separate .py file to re-copy all scraping steps from Jupyter Notebook. 

* Flask Routes were created on a separate .py file. This Flask App file will allow scraped data to be stored in a MongoDB local database, and re-route the scraped data to the HTML page.

* Using CRUD with MongoDB will overwrite new scraped Mars data.

* Used Pandas to convert the Mars Facts data to a HTML table string. This will display the Mars Fact as a table object.

* Final HTML page has a SCRAPE Button on top, that will scrape and display updated Mars data everytime the SCRAPE button is clicked.

# Final Screenshots of HTML page


![Top](Finished_Screenshots/Top_Portion.png)
![Bottom](Finished_Screenshots/Bottom_Portion.png)
