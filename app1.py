from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_app
collection = db.img_dict


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    img_dict = list(db.img_dict.find())
    

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", img_dict=img_dict)


if __name__ == "__main__":
    app.run(debug=True)
