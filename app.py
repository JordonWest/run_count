import json
from flask import Flask, render_template, redirect, url_for, request
from datetime import *
from data.squidbase import squidget, squidwrite

app = Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def main():
    runs = squidget()['runs']
    total_distance = 0
    for r in runs:
        total_distance += r['distance']
    return render_template('home.html', runs=runs, total_distance=total_distance)

@app.route("/metadata")
def meta():
    return json.dumps(squidget())

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
    
