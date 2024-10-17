import json
import pymysql

# Função para conectar ao banco de dados
def conectar_bd(host, user, password, database):
    return pymysql.connect(host=host, user=user, password=password, database=database)



def criarConexao_e_LerArquivo(arquivo_json, user, password, nome_banco):
    

    # Abrindo e lendo o arquivo JSON
    with open(arquivo_json) as f:
        dados_json = json.load(f)

    # Conectar ao banco de dados
    conexao = conectar_bd('localhost', user, password, nome_banco)

    try:
        with conexao.cursor() as cursor:
            # Processar o JSON de forma genérica
            processar_json(cursor, 'tabela_principal', dados_json)
            conexao.commit()
            print("Dados inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados:", e)
    finally:
        # Fechar a conexão
        conexao.close()


# Função para criar uma tabela a partir de qualquer estrutura de JSON
def criar_tabela(cursor, nome_tabela, dados):
    # Determina os tipos das colunas dinamicamente (assumindo VARCHAR como padrão)
    colunas = []
    for chave, valor in dados.items():
        if isinstance(valor, int):
            tipo = "INT"
        elif isinstance(valor, float):
            tipo = "FLOAT"
        else:
            tipo = "VARCHAR(255)"
        colunas.append(f"{chave} {tipo}")

    colunas_sql = ", ".join(colunas)
    
    criar_tabela_sql = f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        {colunas_sql}
    )
    """
    cursor.execute(criar_tabela_sql)

# Função para inserir os dados na tabela
def inserir_dados(cursor, nome_tabela, dados):
    colunas = ", ".join(dados.keys())
    placeholders = ", ".join(["%s"] * len(dados))
    
    inserir_sql = f"""
    INSERT INTO {nome_tabela} ({colunas})
    VALUES ({placeholders})
    """
    cursor.execute(inserir_sql, tuple(dados.values()))


# Função recursiva para percorrer a estrutura JSON
def processar_json(cursor, nome_tabela_base, dados):
    if isinstance(dados, dict):
        for chave, valor in dados.items():
            nome_tabela = f"{nome_tabela_base}_{chave}"  # Tabelas criadas a partir da chave
            if isinstance(valor, dict):
                # Se o valor é outro dicionário, cria uma tabela para ele
                criar_tabela(cursor, nome_tabela, valor)
                # Insere os dados na nova tabela
                inserir_dados(cursor, nome_tabela, valor)
            elif isinstance(valor, list):
                # Se o valor é uma lista, processa cada item da lista
                for item in valor:
                    processar_json(cursor, nome_tabela, item)
            else:
                # Se for um valor simples, cria uma tabela com base na chave
                criar_tabela(cursor, nome_tabela_base, {chave: valor})
                inserir_dados(cursor, nome_tabela_base, {chave: valor})

    elif isinstance(valor, list):
        for item in valor:
            processar_json(cursor, nome_tabela, item)