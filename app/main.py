"""main.py"""

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/status", methods=['POST', 'GET'])
def hello():
    '''
    *******************Health-Check****************
    '''
    return jsonify({"status":"UP"})

if __name__ == "__main__":
    app.run()
    