import json
from pymongo import MongoClient

def conecta_e_inseri_dados(nome_do_banco, nome_da_colecao, arquivo_json):

    # Conectando ao MongoDB (substitua pela URI do seu MongoDB se necessário)
    client = MongoClient("mongodb://localhost:27017/")

    # Selecionando o banco de dados e a coleção
    db = client[f"{nome_do_banco}"]
    colecao = db[f"{nome_da_colecao}"]

    # Carregando o arquivo JSON
    with open(f'{arquivo_json}') as f:
        dados = json.load(f)  # Carrega o JSON como um dicionário


    # Verifica se o JSON é uma lista ou um único documento
    if isinstance(dados, list):
        colecao.insert_many(dados)  # Insere múltiplos documentos
    else:
        colecao.insert_one(dados)

    return db, colecao