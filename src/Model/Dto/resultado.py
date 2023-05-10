from flask import jsonify


class Resultado:

    def __init__(self):
        self.aspectos = None
        self.sentimento = None
        self.empresa = None
        self.produto = None

    def novaAvaliacao(self, produto, empresa, sentimento,aspectos):
        self.produto = produto
        self.empresa = empresa
        self.sentimento = sentimento
        self.aspectos = aspectos

        return self

    def json(self):
        return jsonify({
            "produto": self.produto,
            "empresa ": self.empresa,
            "sentimento": self.sentimento,
            "aspectos": self.aspectos
        })
