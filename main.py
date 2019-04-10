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
# |POR HACER:                                                |
# +==========================================================+
# |TODO: API REST                                            |
# |TODO: Procesar Excel de Orden de Compra                   |
# |TODO: Procesar Excel de Recepción de Mercancía            |
# +----------------------------------------------------------+

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
