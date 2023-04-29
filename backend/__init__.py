import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .api.api import api

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(config=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    api.init_app(app)

    return app
