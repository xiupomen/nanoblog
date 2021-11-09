from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length

from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextAreaField('简介', validators=[Length(min=0, max=256)])
    submit = SubmitField('提交')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('用户名已存在')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('说点啥...', validators=[DataRequired(), Length(min=1, max=256)])
    submit = SubmitField('发射 piu ~')


class SearchForm(FlaskForm):
    q = StringField('搜索', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField('', validators=[
        DataRequired(), Length(min=0, max=512)])
    submit = SubmitField('发射~')