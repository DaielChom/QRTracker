# Libraries
from wtfroms import Form
from wtforms import StringField
from wtforms import validators

# Official form
class Official(Form):

    # validations
    validacion_tamano = validators.length(min = 4, max = 25)
    validacion_requerido = validators.Required(message="Requerido")

    # atributes
    id_official = StringField("ID", [validacion_tamano, validacion_requerido])
    name_official = StringField("Name", [validacion_tamano, validacion_requerido])
