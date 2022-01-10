import json
from flask import Flask, render_template, redirect
from datetime import *
from data.squidbase import squidget, squidwrite

app = Flask(__name__)

@app.route("/")
def main():
    runs = squidget()
    total_distance = 0
    for r in runs:
        total_distance += r['distance']
    return render_template('home.html', runs=runs, total_distance=total_distance)

@app.route("/metadata")
def meta():
    return json.dumps(squidget())

@app.route("/post_run", methods=(['POST']))
def post():
    runs = squidget()
    run = {"distance": request.form['distance'],
            "day": date.today()}
    runs.append(run)
    squidwrite(runs)
    return "written"
    
