from flask_restx import fields
from src.server.instance import server

avaliacao = server.api.model('Resultado', {
    "produto": fields.String(description="Produto a ser avaliado"),
    "empresa": fields.String(description="Qual empresa o produto é na hora da compra"),
    "sentimento": fields.Float(
        description="Média dos raking  das avaliações sobre a satisfação geral",
        max=5, min=0
    ),
    "aspectos" : fields.List(fields.String,description="Aspectos que estão sendo avaliados encontrados")
})
