# Libraries
from flask import Flask
from flask import request
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from modelo import db
from modelo import Client
from modelo import Official
from modelo import Package
from flask import render_template
import formpy

# init ...
app = Flask(__name__) # Flask
app.config.from_object(DevelopmentConfig) # Config
csrf = CSRFProtect() # encrypt
tables = ["clientes", "paquetes", "funcionarios","QR"]

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

    # POST
    if request.method == "POST":

        # Get data from request
        official_form =  formpy.Official(request.form)

        # form validate
        if official_form.validate():
            # Check if offical exists
            official_query = Official.query.filter_by(id_official = official_form.id_official.data).first()
            if official_query is None:

                # new official for insert to db
                official_new = Official(official_form.id_official.data,
                                        official_form.name_official.data)
                # db Insert
                db.session.add(official_new)
                db.session.commit()
                return jsonify(success = 1, message="El funcionario a sido creado")
            else:
                return jsonify(success = 0,  error_msg=str("El funcionario ya existe"))
        else:
            return jsonify(success = 0, error_msg=str("campos invalidos"))

# Route clientes
@app.route('/clientes', methods=['GET', 'POST'])
def cientes():

    # Instance of client form
    client_form = formpy.Client(None)

    # GET
    if request.method == 'GET':
        return render_template('clientes.html', title = "clientes", tables = tables, client_form = client_form )

    # POST
    if request.method == 'POST':

        # Get data from request
        client_form = formpy.Client(request.form)

        # form validate
        if client_form.validate():

            # Check if client exists
            client_query = Client.query.filter_by(id_client = client_form.id_client.data).first()

            if client_query is None:

                # instance from db of client_form
                client_new = Client(client_form.id_client.data,
                                    client_form.name_client.data,
                                    client_form.address_client.data)
                # add db
                db.session.add(client_new)
                db.session.commit()
                return jsonify(success = 1, message="El cliente a sido creado")
            else:
                return jsonify(success = 0,  error_msg=str("El cliente ya existe"))
        else:
            return jsonify(success = 0, error_msg=str("campos invalidos"))

# Route paquetes
@app.route('/paquetes', methods=['GET', 'POST'])
def paquetes():

    # Instance package form
    paquete_form = formpy.Package(None)
    paquete_form.client.choices=[] # Evita repeticion

    # For dinamic SelectField
    paquete_form.client.choices.append(('',''))
    if Client.query.all() is not None:
        for i in Client.query.all():
            paquete_form.client.choices.append((i.id_client, i.id_client))

    # GET
    if request.method == 'GET':
        return render_template('paquetes.html', title = "paquetes", tables = tables, paquete_form = paquete_form)

    # POST
    if request.method == "POST":
        package_form = formpy.Package(request.form)

        # form validate
        if package_form.validate():
            package_query = Package.query.filter_by(id_package = package_form.id_package.data).first()

            if package_query is None:
                package_new = Package(package_form.id_package.data,
                                      package_form.client.data,
                                      package_form.descrption_package.data,
                                      package_form.estate_package.data)
                db.session.add(package_new)
                db.session.commit()

                return jsonify(success = 1, message="El paquete a sido creado")

            else:
                return jsonify(success = 0,  error_msg=str("El paquete ya existe"))

        else:
            return jsonify(success = 0, error_msg=str("campos invalidos"))

@app.route('/QR', methods=['GET'])
def QR():
    QR_form = formpy.QR(None)
    QR_form.package.choices = []

    # For dinamic SelectField
    QR_form.package.choices.append(('',''))
    if Package.query.all() is not None:
        for i in Package.query.all():
            QR_form.package.choices.append((i.id_package, i.id_package))

    chl = request.args.get('package','None')
    uri = 'https://chart.googleapis.com/chart?chl='+chl+"&chld=H&choe=UTF-8&chs=300x300&cht=qr"
    return render_template('QR.html', title = "QR", tables = tables, QR_form = QR_form, uri = uri, chl = chl)



# main
if __name__ == '__main__':
    csrf.init_app(app) # init encript
    db.init_app(app) # init bd

    with app.app_context():
        db.create_all()

    app.run(port = 8008)
