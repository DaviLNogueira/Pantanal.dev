from flask_restx import Resource
from src.server.instance import server
from src.validade.validadeJson import existeCampo
from src.exception.pantanalException import *

app, api = server.app, server.api


@api.route('/produtos')
class Produto(Resource):

    def post(self):
        response = api.payload
        try:
            existeCampo(['produto'], response)
        except pantanalException as e:
            return e.get()
