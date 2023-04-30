import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.routing import BaseConverter

from .api.api import api

basedir = os.path.abspath(os.path.dirname(__file__))


class StrListConverter(BaseConverter):
    regex = r".+(?:,.+)*,?"

    def to_python(self, value):
        return value.split(",")

    def to_url(self, value):
        return ",".join(value)


def create_app(config=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.url_map.converters["str_list"] = StrListConverter

    api.init_app(app)

    return app
