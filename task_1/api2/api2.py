from flask import Flask

app = Flask(__name__)


@app.route("/api2")
def hello_world():
    return "API2"


if __name__ == "__main__":
    port = 80
    app.run(debug=True, host='0.0.0.0', port=port)

