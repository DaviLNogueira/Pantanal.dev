from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/produto/<string:produto>', methods=['POST'])
def produtoEspecifico(produto):
    return jsonify({'Produto Escolhido': produto})


@app.route('/link/', methods=['POST'])
def linkProduto():
    link = request.get_json()
    return jsonify({'link': link['link']})


app.run(port=5000, host='localhost', debug=True)