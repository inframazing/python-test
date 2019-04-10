# -*- encoding: utf-8 -*-

# +==========================================================+
# |DATOS DEL PROGRAMA                                        |
# +==========================================================+
# |                                                          |
# |Proyecto:       python-test                               |
# |Descripcion:    Programa Principal de la Aplicacion       |
# |Archivo:        main.py                                   |
# |OS:             Linux (ZorinOS 12.4)                      |
# |Python:         3.6.7                                     |
# |Desarrollador:  Ing. Agustin Noguez Salazar               |
# |                                                          |
# +==========================================================+
# |LIBRERIAS EXTERNAS                                        |
# +==========================================================+
# |                                                          |
# | $ sudo apt-get install python3-pandas                    |
# | $ sudo apt-get install python3-xlrd                      |
# |                                                          |
# +==========================================================+
# |POR HACER:                                                |
# +==========================================================+
# |TODO: API REST                                            |
# |TODO: Procesar Excel de Orden de Compra                   |
# |TODO: Procesar Excel de Recepción de Mercancía            |
# +----------------------------------------------------------+

import os
import pandas as pd
import pymongo
from flask import Flask, render_template, request

__author__ = 'Tinny'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

global connection

# Connect with MongoDB
uri = "mongodb+srv://python:test@python-test-aodbq.mongodb.net/ilusion"
connection = pymongo.MongoClient(uri)
database = connection['ilusion']
collection = database['almacenes']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/purchase_order")
def purchase():
    return render_template("purchase_order.html")


@app.route("/received_products")
def received():
    return render_template("received_products.html")


@app.route("/po_upload", methods=['POST'])
def po_upload():
    target = os.path.join(APP_ROOT, 'docs/po/')
    print(target)

    # Procesamiento del archivo

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        df = pd.read_excel(destination)
        pdv_list = df['PDV'].tolist()
        # collection.insert(pdv_list)
        print(type(pdv_list))
        print(pdv_list)

    # Buscamos la lista de almacenes

    return df.to_html()


@app.route("/rp_upload", methods=['POST'])
def rp_upload():
    target = os.path.join(APP_ROOT, 'docs/rp/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        df = pd.read_excel(destination)
        return df.to_html()


@app.route("/warehouses")
def warehouses():
    return render_template("warehouses.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
