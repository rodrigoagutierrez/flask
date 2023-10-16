from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
class TodoForm(Form):
   description = StringField('Descripción', validators=[DataRequired()])
   submit = SubmitField('Crear')
   
class DeleteTodoForm():
    submit = SubmitField('Eliminar')
    
class UpdateTodoForm(Form):
    submit = SubmitField('Actualizar')