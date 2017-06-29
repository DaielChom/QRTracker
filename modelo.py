from flask_sqlalchemy import SQLAlchemy

#Inicializa base de datos
db = SQLAlchemy()

class Official(db.Model):

    # Table name
    __tablename__ = "Official"

    # Atributes
    id_offcial = db.Column(db.String(20), primary_key = True, nullable = False)
    nanme_official = db.Column(db.String(20), nullable = True)

    # Constructor
    def __init__(self, id_official, name_official):
        self.id_official = id_offcial
        self.name_official = nanme_official
