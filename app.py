import json
from flask import Flask, render_template, redirect, url_for, request
from datetime import *
from data.squidbase import squidget, squidwrite

app = Flask(__name__)

@app.route("/")
def main():
    progress_percent = 20
    runs = squidget()['runs']
    total_distance = 0
    for r in runs:
        total_distance += r['distance']
    return render_template('home.html',
                runs=runs, 
                total_distance=total_distance, 
                percent=round(total_distance/1000,2),
                progress_percent=progress_percent)

@app.route("/metadata")
def meta():
    return json.dumps(squidget())

@app.route("/test")
def test():
    return render_template('index.html')

@app.route("/post_run", methods=(['POST']))
def post():
    runs = squidget()['runs']
    distance = request.form['distance']
    try:
        float(distance)
    except:
        return "not a valid float"
    run = {"distance": float(distance),
            "day": (date(2022, 12, 31) - date.today()).days}
    runs.append(run)
    data = {"runs":runs}
    squidwrite(data)
    return redirect(url_for('main'))
    
