Nesse desafio eu propôs criar um pacote para estabelecer uma conexão tanto com o mongoDB quanto o MySQL, lendo um arquivo .json e adicionar esses dados em um dicionário e depois inserir os dados do dicionário em coleções no mongoDB e tabelas no MySQL e criar funções e códigos para realizar o CRUD

# crud_mongodb_mysql

Description. 
The package package_name is used to:
- Ler um arquivo .json em file1_name.py no modulo1_name, inseri-lo em um dicionário, criar uma conexão com o mongoDB e inserir os dados do dicionário em coleções do mongoDB
- Ler um arquivo .json em file2_name.py no modulo1_name, inseri-lo em um dicionário, criar uma conexão com o MySQL e inserir os dados do dicionário em tabelas do MySQL e criar essas tabelas antes de inserir os dados nelas
- O restante do crud do banco de dados mongoDB foi realizado no file1_name.py no modulo2_name

## Installation
Essa parte de publicar no pypa ainda não
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install crud_mongodb_mysql
```

## Usage

```python
from crud_mongodb_mysql.module1_name import file1_name
file1_name.conecta_e_inseri_dados(nome_do_banco, nome_da_colecao, arquivo_json)
from crud_mongodb.module1_name import file2_name
file2_name.conectar_bd(host, user, password, database)
file2_name.criarConexao_e_LerArquivo(arquivo_json, user, password, nome_banco)
file2_name.criar_tabela(cursor, nome_tabela, dados)
file2_name.inserir_dados(cursor, nome_tabela, dados)
file2_name.processar_json(cursor, nome_tabela_base, dados)

from crud_mongodb_mysql.module2_name import file1_name
file1_name.lerDado(conexao, filtro)
file1_name.lerVariosDados(conexao, filtro)
file1_name.atualizarUnicoDocumento(conexao, filtro, novo_dado)
file1_name.atualizarVariosDocumentos(conexao, filtro, novo_dado)
file1_name.excluirCampo(conexao, filtro, campo_excluido)
file1_name.deletaUnicoDocumento(conexao, filtro)
file1_name.deletaVariosDocumentos(conexao, filtro)
```

## Author
Rômulo Soares Rocha

## License
[MIT](https://choosealicense.com/licenses/mit/)
