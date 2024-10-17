import pymongo

def lerDado(conexao, filtro):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.find_one(filtro)
        if resultado is not None:
            print("Documento encontrado: ", resultado)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")
        return False

def lerVariosDados(conexao, filtro):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.find_many(filtro)
        if resultado is not None:
            print("Documentos encontrados")
            for doc in resultado:
                print(doc)
                return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")
        return False
    

def atualizarUnicoDocumento(conexao, filtro, novo_dado):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.update_one(filtro, novo_dado)
        if resultado is not None:
            print("Documentos modificados:", resultado.modified_count)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")
        return False


def atualizarVariosDocumentos(conexao, filtro, novo_dado):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.update_many(filtro, novo_dado)
        if resultado is not None:
            print("Documentos modificados:", resultado.modified_count)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")
        return False


def excluirCampo(conexao, filtro, campo_excluido):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.update_many(filtro, { "$unset": { f"{campo_excluido}": "" } } )
        if resultado is not None:
            print("Documentos modificados:", resultado.modified_count)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")
        return False


def deletaUnicoDocumento(conexao, filtro):
    db, colecao = conexao
    if db is not None and colecao is not None:
        resultado = colecao.delete_one(filtro)
        if resultado is not None:
            print("Documentos excluídos:", resultado.deleted_count)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")


def deletaVariosDocumentos(conexao, filtro):
    db, colecao = conexao
    if db is not None and colecao is not None: 
        resultado = colecao.delete_many(filtro)
        if resultado is not None:
            print("Documentos excluídos:", resultado.deleted_count)
            return True
        else:
            print("Filtro inválido")
            return False
    else:
        print("Conexão inválida com o banco de dados ou coleção inválida")