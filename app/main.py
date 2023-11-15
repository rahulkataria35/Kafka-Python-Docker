"""main.py"""
import sys
import os
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/status", methods=['POST', 'GET'])
def hello():
    "*******************Healthy****************"
    return jsonify({"status":"UP"})

if __name__ == "__main__":
    app.run()
    