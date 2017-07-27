from flask_sqlalchemy import SQLAlchemy

#Inicializa base de datos
db = SQLAlchemy()

class Monitor(db.Model):
    __tablename__ = "Monitor"

    id_package = db.Column(db.String(20), db.ForeignKey('Package.id_package'), primary_key = True)
    id_official = db.Column(db.String(20), db.ForeignKey('Official.id_official'), primary_key = True)
    long_monitor = db.Column(db.String(20), nullable = False)
    lati_monitor = db.Column(db.String(20), nullable = False)
    alti_monitor = db.Column(db.String(20), nullable = False)
    hour_monitor= db.Column(db.String(20), nullable = False)
    date_monitor = db.Column(db.String(20), nullable = False)

    package = db.relationship('Package', backref="Monitor")
    offical = db.relationship('Official', backref="Monitor")

    def __init__(self, id_package, id_official, long_monitor, lati_monitor, alti_monitor, hour_monitor, date_monitor):
        self.id_package = id_package
        self.id_official = id_official
        self.long_monitor = long_monitor
        self.lati_monitor = lati_monitor
        self.alti_monitor = alti_monitor
        self.hour_monitor = hour_monitor
        self.date_monitor = date_monitor


class Official(db.Model):

    # Table name
    __tablename__ = "Official"

    # Atributes
    id_official = db.Column(db.String(20), primary_key = True, nullable = False)
    name_official = db.Column(db.String(20), nullable = True)

    # Constructor
    def __init__(self, id_official, name_official):
        self.id_official = id_official
        self.name_official = name_official

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

    def __init__(self, id_package, client, descrption_package, estate_package):
        self.id_package = id_package
        self.client = client
        self.descrption_package = descrption_package
        self.estate_package = estate_package

    def as_dict(self):
        obj_d = {
            'id_package': self.id_package,
            'client': self.client,
            'descrption_package': self.descrption_package,
            'state_package': self.estate_package,
        }
        return obj_d
