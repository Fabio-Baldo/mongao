# -*- coding: utf-8 -*-

# Instalar todas as dependências abaixo

# pip3 install flask
# pip3 install pymongo
# pip3 install dnspython

import flask

import pymongo

USER = 'admin'
PASSWORD = '!23Mudar$'

MONGODB_URL = f'mongodb+srv://{USER}:{PASSWORD}@cluster0-kb7mp.mongodb.net/test?retryWrites=true'


client = pymongo.MongoClient("mongodb+srv://admin:<!23Mudar$>@cluster0-kb7mp.mongodb.net/test?retryWrites=true")
db = client.test



def main():
    conn = pymongo.MongoClient(MONGODB_URL)


if __name__ == '__main__':
    main()