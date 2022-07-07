from flask import Flask
from . import sensor
from flask import jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("ui"))

@app.route("/api/value")
def value():
    val = sensor.read_value()
    return jsonify({
        "value": val
    })

@app.route("/api/switch")
def switch():
    return jsonify({
        "on": sensor.is_threshold_reached(),
        "pin": sensor.SENSOR_PIN,
    })

@app.route("/ui")
def ui():
    return render_template("index.html")