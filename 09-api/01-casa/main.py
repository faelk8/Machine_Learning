from flask import Flask, request, jsonify
# from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

# Colunas que o modelo precisa
colunas = ['tamanho','ano','garagem']
# Carregando o modelo de previsao de preço
modelo = pickle.load(open('/home/rafael/MEGA/github/Machine_Learning/09-api/01-casa/model/modelo.sav','rb'))

app = Flask(__name__)
# app.config['BASIC_AUTH_USERNAME'] = 'rafael'
# app.config['BASIC_AUTH_PASSWORD'] = 'batista'

# basic_auth = BasicAuth(app)

# acesso principal
@app.route('/')
def home():
    return "Minha primeira API."

# passa a frase para o modelo
@app.route('/sentimento/<frase>')
# @basic_auth.required
def sentimento(frase):
    """
    Faz a classificação da frase.

    Input:
        string: frase

    Outpu:
        string: polaridade valor float -1 a 1
    """
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

@app.route('/cotacao/', methods=['POST'])
# @basic_auth.required
def cotacao():
    """
    Faz a previsão do valor da casa.

    Input: 
        post json: {
                "tamanho":120,
                "ano":2001,
                "garagem":2
               }

    Outpu:
        array: posição 0 - float
    """
    # Content-Type - application/json
    dados = request.get_json()
    # garante que os dados estejam na sequencia correta
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    # o retorno é um array como precisa apenas do valor pega o index 0
    return jsonify(preco=preco[0])

# Executa a aplicação
# debug=True reconece a alteração sem precisar reiniciar a aplicação
app.run(debug=True)