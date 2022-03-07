from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dlvskcjfhlafvv:12c7746e897203d3c597068941e21373f649cf1d67104bd6db82044a3ad97c62@ec2-52-204-196-4.compute-1.amazonaws.com:5432/dk1aoiov0d7in"
app.config['SECRET_KEY'] = "averybadtime"
db = SQLAlchemy(app)


if __name__ == "__main__":
    from main import *

    app.run(debug=True, port=8080)
