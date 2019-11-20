# import  required dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

#create flask app
app = Flask(__name__)

#set up mongo 
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

#Route that will query Mongo Database and pass data to html
@app.route("/")
def home(): 

    # Find data
    scraped_mars_data = mongo.db.scraped_mars_data.find_one()

    # Return template and data
    return render_template("index.html", scraped_mars_data=scraped_mars_data)


 # Route will call and scrape
@app.route("/scrape")
def scrape():

    # scrape
    scraped_mars_data = scrape_mars.scrape()

    # update mongo db
    mongo.db.scraped_mars_data.update({}, scraped_mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)   