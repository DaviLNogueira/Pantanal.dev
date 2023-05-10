from flask import Flask
from flask_restx import Api , marshal
from flask_caching import Cache
import yaml

cache = Cache()


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, version='1.0', title="Pantanal Dev", description="O melhor grupo", doc='/docs')
        self.app.config['CACHE_TYPE'] = 'simple'
        self.cache = cache
        self.cache.init_app(app=self.app)

    def run(self):
        self.app.run(
            debug=True
        )


server = Server()
