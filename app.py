from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

app = Flask(__name__)
# Create connection variable

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Connect to a database. Will create one if not already available.

# mongo = PyMongo(app)

@app.route("/")
def index():
    img_dict = mongo.db.img_dict.find()
    return render_template("index.html", img_dict=img_dict)

@app.route("/scrape")
def scraper():
    img_dict = mongo.db.img_dict
    mars_data = scrape_mars.data_scrape()
    img_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__== '__main__':
    app.run(debug=True)