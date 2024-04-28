#!/usr/bin/python3
"""Create Flask app"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views


# creating a Flask app
app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def page_not_found(e):
    message = e.description
    return message, 400


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
