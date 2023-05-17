from flask import jsonify


class Resultado:

    def __init__(self, produto, empresa, sentimento,aspectos,avaliacoes):
        self.produto = produto
        self.empresa = empresa
        self.sentimento = sentimento
        self.aspectos = aspectos
        self.avaliacoes = avaliacoes

    def json(self):
        return jsonify({
            "produto": self.produto,
            "empresa ": self.empresa,
            "sentimento": self.sentimento,
            "aspectos": self.aspectos,
            "avaliacoes" : self.avaliacoes
        })
