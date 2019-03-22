# -*- coding: utf-8 -*-

# Instalar todas as dependências abaixo

# pip3 install flask
# pip3 install pymongo
# pip3 install dnspython

# Executar python3 app.py

import flask
import pymongo

USER = 'admin'
PASSWORD = '!23Mudar$'

MONGODB_URL = 'mongodb+srv://{}:{}@cluster0-nstlp.mongodb.net/test?retryWrites=true'
MONGODB_URL = MONGODB_URL.format(USER, PASSWORD)

class Model:
    def __repr__(self):
        return str(self,__dict__)

class Usuario:

    def __init__(self, nome, endereco, idade):
        self.nome = nome
        self.nome = endereco
        self.nome = idade

def main():
    conn = pymongo.MongoClient(MONGODB_URL)

    db = conn.mongao
    monguinho = db.monguinho

    usuario = Usuario('Fabio', 'Rua Tutz Tutz', 30)

    monguinho.insert(usuario.__dict__)

    for resultado in monguinho.find({}):
        print(resultado)

if __name__ == '__main__':
    main()