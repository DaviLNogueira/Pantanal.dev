from flask import jsonify


class Resultado:

    def __init__(self):
        self.qualidade = None
        self.custo = None
        self.entrega = None
        self.sentimento = None
        self.empresa = None
        self.produto = None

    def novaAvaliacao(self, produto, empresa, sentimento, entrega, custo, qualidade):
        self.produto = produto
        self.empresa = empresa
        self.sentimento = sentimento
        self.entrega = entrega
        self.custo = custo
        self.qualidade = qualidade
        return self

    def json(self):
        return jsonify({
            "produto": self.produto,
            "empresa ": self.empresa,
            "sentimento": self.sentimento,
            "entrega": self.entrega,
            "custo": self.custo,
            "qualidade": self.qualidade,
        })
