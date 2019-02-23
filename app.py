from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


app = Flask(__name__)

# setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# connect to mongo db and collection



@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars_info = mongo.db.collection.find_one()
    return render_template("index.html", data=mars_info)



@app.route("/scrape")
def scraper():
    mars_data = scrape_mars.data_scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__== '__main__':
    app.run(debug=True)