# Libraries
from flask import Flask
from flask import request
from config import DevelopmentConfig
from flask_wtf import CSRFProtect
from modelo import db
from flask import render_template
import formpy

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

    # Intancia de un formulario para Funcionarios
    funcionario_form = formpy.Official(None)

    # GET
    if request.method == 'GET':
        return render_template('funcionarios.html', title = "funcionarios", tables = tables, funcionario_form = funcionario_form)


# Route clientes
@app.route('/clientes', methods=['GET', 'POST'])
def cientes():

    # Instance of client form
    client_form = formpy.Client(None)

    # GET
    if request.method == 'GET':
        return render_template('clientes.html', title = "clientes", tables = tables, client_form = client_form )

# Route paquetes
@app.route('/paquetes', methods=['GET', 'POST'])
def paquetes():

    # Instance package form
    paquete_form = formpy.Package(None)
    
    # GET
    if request.method == 'GET':
        return render_template('paquetes.html', title = "paquetes", tables = tables, paquete_form = paquete_form)


# main
if __name__ == '__main__':
    csrf.init_app(app) # init encript
    db.init_app(app) # init bd

    with app.app_context():
        db.create_all()

    app.run(port = 8008)
