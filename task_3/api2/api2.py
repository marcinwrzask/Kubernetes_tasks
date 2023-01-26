from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello_world():
    n = random.randint(0, 10)
    if n%2 == 0:
        return "ERROR", 500
    else: return "OK" 


if __name__ == "__main__":
    port = 80
    app.run(debug=True, host='0.0.0.0', port=port)
