from flask import Flask, render_template
import random
from datetime import date
import requests

year = date.today().year

app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1, 10)
    return render_template("index.html", rand = random_number, year=year)

@app.route("/guess/<string:name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io/?name={name}")
    return render_template("guess.html", name=name.capitalize(), age=age_response.json()["age"], gender=gender_response.json()["gender"])

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c594fae7ee846a6b8123"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
