from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


db_psw = os.environ.get('POSTGRES_PASSWORD')
db_user = os.environ.get('POSTGRES_USER')
db_name = os.environ.get('POSTGRES_DB')

print(db_name, db_psw, db_user)

@app.route("/")
def hello_world():
    try:
        conn = psycopg2.connect(
            host = 'postgres',
            database = db_name,
            user = db_user,
            password = db_psw,
            port = 5432
        )
        n = "Database connected successfully"
    except:
        n = "Database not connected successful"

    return jsonify(n)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
