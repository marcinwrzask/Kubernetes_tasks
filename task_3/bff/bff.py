from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/api1")
def hello_world():
    return urllib.request.urlopen("http://api1").read()

if __name__ == "__main__":
    port = 80
    app.run(debug=True, host='0.0.0.0', port=port)
