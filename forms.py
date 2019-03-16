from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, Length, optional


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    emp_no = IntegerField('emp_no', validators=[DataRequired()])
    location = StringField('location', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    seat_no = IntegerField('seat_no', validators=[optional()])
    sl_no_1 = StringField('sl_no_1', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    model = StringField('model', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    make = StringField('make', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    tel_tvm = StringField('tel_tvm', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    test_pc = StringField('test_pc', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    processor = StringField('processor', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    ram = StringField('ram', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    hdd = StringField('hdd', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    asset_no = StringField('asset_no', validators=[DataRequired(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    allocation_date = StringField('allocation_date', validators=[DataRequired(
    ), Length(min=-1, max=80, message='length must be less than 80 chars')])
    project_name = StringField('project_name', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    won_no = StringField('won_no', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    end_date = StringField('end_date', validators=[DataRequired(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
