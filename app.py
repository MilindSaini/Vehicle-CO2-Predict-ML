from flask import Flask

app = Flask(__name__)

try:
   from controllers import *
except Exception as e:
    print(e)


# $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"