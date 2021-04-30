from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename

class ImageForm(FlaskForm):
    image = FileField(label='select image...',validators=[FileRequired()])
    submit = SubmitField(label='upload')