from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    r = requests.get("http://api2")
    while r.status_code != 200:
        r = requests.get("http://api2")
    return r.text

if __name__ == "__main__":
    port = 80
    app.run(debug=True, host='0.0.0.0', port=port)
