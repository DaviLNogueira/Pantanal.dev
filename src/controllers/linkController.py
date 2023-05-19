from flask_restx import Resource, fields
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
        avaliacoes_filtradas = [ava for ava in avaliacaoes if len(avaliacao) < 512]

        if len(avaliacoes_filtradas) < 1:
            execption = pantanalException(mensagem="Não foi possível realizar a busca por avaliações")
            return execption.get()
        predicts = ia.predecit(avaliacoes_filtradas)

        resultado = Resultado(sentimento=0, produto=produto,avaliacoes=avaliacoes_filtradas)
        cache.set(cache_key, {'produto': produto, 'sentimento': 0, 'avaliacoes': avaliacaoes}, timeout=600)

        return resultado.json()

    def obter_cache(self, cached_results):
        produto_cahe = cached_results.get('produto')
        sentimento = cached_results.get('sentimento')
        avaliacoes = cached_results.get('avaliacoes')
        return Resultado(sentimento=sentimento, produto=produto_cahe,avaliacoes=avaliacoes)
