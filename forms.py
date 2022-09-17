from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import email_validator
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField



##WTForm


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid Email")])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="Field should contain Email Address")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LogIn")


class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")
