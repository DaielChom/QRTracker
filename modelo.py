from flask_sqlalchemy import SQLAlchemy

#Inicializa base de datos
db = SQLAlchemy()

class Official(db.Model):

    # Table name
    __tablename__ = "Official"

    # Atributes
    id_official = db.Column(db.String(20), primary_key = True, nullable = False)
    nanme_official = db.Column(db.String(20), nullable = True)
    


    # Constructor
    def __init__(self, id_official, name_official):
        self.id_official = id_offcial
        self.name_official = nanme_official

class Client(db.Model):

    __tablename__ = "Client"

    id_client = db.Column(db.String(20), primary_key= True, nullable = False)
    name_client = db.Column(db.String(20), nullable= False)
    address_client = db.Column(db.String(20), nullable= False)
    packages = db.relationship("Package", backref="Client", lazy ="dynamic")

    def __init__(self, id_client, name_client, address_client):
        self.id_client = id_client
        self.name_client = name_client
        self.address_client = address_client

class Package(db.Model):

    __tablename__ = "Package"

    id_package = db.Column(db.String(20), primary_key = True, nullable = False)
    client = db.Column(db.String(20), db.ForeignKey('Client.id_client'))
    descrption_package = db.Column(db.Text(), nullable = False)
    estate_package = db.Column(db.String(20), nullable = False)

monitor = db.Table('monitor',
                    db.Column('id_monitor', db.String(20), primary_key = True, nullable = True),
                    db.Column('package', db.String(20), db.ForeignKey('Package.id_package')),
                    db.Column('official', db.String(20), db.ForeignKey('Official.id_official')),
                    db.Column('long_monitor', db.Float(), nullable = False),
                    db.Column('lati_monitor', db.Float(), nullable = False),
                    db.Column('alti_monitor', db.Integer(), nullable = False),
                    db.Column('hour_monitor', db.Time(), nullable = False),
                    db.Column('date_monitor', db.Date(), nullable = False),)
