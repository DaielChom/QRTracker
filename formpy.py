# Libraries
from wtforms import Form
from wtforms import StringField
from wtforms import validators
from wtforms import SelectField
from wtforms import TextField
from wtforms import FloatField
from wtforms import IntegerField


# Official form
class Official(Form):

    # validations
    validacion_tamano = validators.length(min = 4, max = 25)
    validacion_requerido = validators.Required(message="Requerido")

    # atributes
    id_official = StringField("ID", [validacion_tamano, validacion_requerido])
    name_official = StringField("Name", [validacion_tamano, validacion_requerido])

class Client(Form):

    # validations
    validacion_tamano = validators.length(min = 4, max = 25)
    validacion_requerido = validators.Required(message="Requerido")

    # atributes
    id_client = StringField("ID", [validacion_tamano, validacion_requerido])
    name_client = StringField("Name", [validacion_tamano, validacion_requerido])
    address_client = StringField("Address", [validacion_tamano, validacion_requerido])


class Package(Form):

    # Atributes
    id_package = StringField("ID")
    client = SelectField('Client', choices=[])
    descrption_package = TextField('Desrciption')
    estate_package = SelectField('Estate', choices=[('', ''),('Bodega', 'Bodega'),('Recogido', 'Recogido'),('Entregado', 'Entregado'),('Devuelto', 'Devuelto')])

class QR(Form):

    validacion_tamano = validators.length(min = 4, max = 25)
    validacion_requerido = validators.Required(message="Requerido")

    package = SelectField('Package', choices=[])
