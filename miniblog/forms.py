from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("密码", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("确认")


class CkEditorForm(FlaskForm):
    title = StringField("标题", validators=[DataRequired(), Length(1, 20)])
    create_time = StringField("创建时间", validators=[DataRequired(), Length(1, 20)])
    text_field = CKEditorField("文章主体", validators=[DataRequired()])
    submit = SubmitField("创建")
