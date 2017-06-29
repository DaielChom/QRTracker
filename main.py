# Libraries
from flask import Flask
from flask import request
from config import DevelopmentConfig
from flask_wtf import CSRFProtect
from modelo import db
from flask import render_template

# init ...
app = Flask(__name__) # Flask
app.config.from_object(DevelopmentConfig) # Config
csrf = CSRFProtect() # encrypt
tables = ["clientes", "paquetes", "funcionarios"]

# Route /
@app.route('/', methods=['GET'])
def index():
    #print(db.get_tables_for_bind())
    return render_template('index.html', title = "QRTraker", tables = tables)

# Route funcionarios
@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'GET':
        return render_template('funcionarios.html', title = "funcionarios", tables = tables)

# Route clientes
@app.route('/clientes', methods=['GET', 'POST'])
def cientes():
    if request.method == 'GET':
        return render_template('clientes.html', title = "clientes", tables = tables)

# Route paquetes
@app.route('/paquetes', methods=['GET', 'POST'])
def paquetes():
    if request.method == 'GET':
        return render_template('paquetes.html', title = "paquetes", tables = tables)


# main
if __name__ == '__main__':
    csrf.init_app(app) # init encript
    db.init_app(app) # init bd

    with app.app_context():
        db.create_all()

    app.run(port = 8008)
