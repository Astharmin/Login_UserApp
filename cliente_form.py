

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class ClienteForm(FlaskForm):
    id = HiddenField("id")
    nombre = StringField('Nombre',
                         validators=[DataRequired()])
    apellido = StringField('Apellido',
                           validators=[DataRequired()])

    # IntegerField() --> Funcion para recibir datosn en Int
    mail = StringField('Mail',
                        validators=[DataRequired()])
    guardar = SubmitField('Guardar')