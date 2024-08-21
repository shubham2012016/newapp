from flask import Flask, render_template

app = Flask(__name__,template_folder="C:/Users/Dell/Desktop/samachar/templates")

@app.route("/")
def home():
    return render_template("index.html")
