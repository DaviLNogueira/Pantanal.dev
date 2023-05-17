from flask_restx import Resource, fields
from flask import jsonify
from src.server.instance import server
from src.validade.validadeJson import existeCampo
from src.exception.pantanalException import *
from src.Model.Dto.resultado import Resultado
from src.Model.schemaDocumentation.resultado import avaliacao
from src.Mineradoras import amazon
from src.moldelo import ia

app, api = server.app, server.api
cache = server.cache


@api.route('/link')
class Produto(Resource):

    @api.doc(model=avaliacao)
    @api.expect(
        server.api.model('Link', {
            "link": fields.String(description="Link a ser avaliado", required="true"), }))
    def post(self):
        response = api.payload
        try:
            existeCampo(['link'], response)
        except pantanalException as e:
            return e.get()

        link = response['link']
        cache_key = f"link{link}"
        cached_results = cache.get(cache_key)
        if cached_results:
            return self.obter_cache(cached_results).json()

        produto, avaliacaoes = amazon.by_product(link)
        predicts = ia.predecit(avaliacaoes)

        resultado = Resultado(aspectos='', produto=produto, sentimento=sum(predicts) / len(predicts) * 2.5, empresa='',
                              avaliacoes=avaliacaoes)
        cache.set(cache_key, {'produto': produto, 'resultados': predicts, 'avaliacoes': avaliacaoes}, timeout=600)

        return resultado.json()

    def obter_cache(self, cached_results):
        produto_cahe = cached_results.get('produto')
        predicts = cached_results.get('resultados')
        avaliacoes = cached_results.get('avaliacoes')
        return Resultado(aspectos='', produto=produto_cahe, sentimento=sum(predicts) / len(predicts) * 2.5, empresa='',
                         avaliacoes=avaliacoes)
