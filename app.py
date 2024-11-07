from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import pandas as pd

openai.api_key = ''

app = Flask(__name__)
CORS(app)

# Carregar o conjunto de dados do CSV
try:
    filmes_df = pd.read_csv('imdb_top_1000.csv')
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")

def validar_sinopse(sinopse):
    try:
        prompt = f"Is the following text a movie synopsis? Respond with 'yes' or 'no': {sinopse}"
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        resposta = response.choices[0].message['content'].strip().lower()
        return resposta == "yes"
    except Exception as e:
        print(f"Erro ao validar a sinopse: {e}")
        return False  # Se houver um erro, considere como inválido

def analisar_sinopse(sinopse):
    try:
        # Análise de gênero usando GPT
        prompt = f"Based on the following movie synopsis, identify the main genre in English: {sinopse}. Please respond with a single genre."
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip().lower()
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "error"

@app.route('/analisar', methods=['POST'])
def processar_sinopse():
    dados = request.get_json(force=True)
    sinopse_provida = dados.get('sinopse')

    # Validar a sinopse antes de prosseguir com a análise
    if not validar_sinopse(sinopse_provida):
        return jsonify({"error": "Insira uma sinopse válida"}), 400

    # Analisar a sinopse e obter o gênero previsto
    genero_predito = analisar_sinopse(sinopse_provida)
    
    return jsonify({"genero": genero_predito}), 200

@app.route('/testar_precisao', methods=['GET'])
def testar_precisao():
    generos_preditos = []
    generos_reais = []

    for index, row in filmes_df.iterrows():
        sinopse = row['Overview']  # A coluna que contém as sinopses
        genero_real = row['Genre']  # A coluna que contém os gêneros

        # Analisar a sinopse e obter o gênero previsto
        genero_predito = analisar_sinopse(sinopse)

        # Adicionar à lista para comparação
        generos_preditos.append(genero_predito)
        generos_reais.append([g.strip().lower() for g in genero_real.split(',')])  # Converte a lista de gêneros para minúsculas

    # Cálculo da precisão
    acertos = sum(1 for gp, gr in zip(generos_preditos, generos_reais) if gp in gr)  # Verifica se o gênero previsto está entre os gêneros reais
    total = len(generos_reais)
    precisao = (acertos / total) * 100 if total > 0 else 0

    return jsonify({"precisao": precisao, "total_testado": total}), 200

if __name__ == '__main__':
    app.run(debug=True)
