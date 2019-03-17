from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, Form
from wtforms.validators import DataRequired, Email, Length, optional


class AssetSearchForm(Form):
    choices = [('name', 'name'),
               ('emp_no', 'emp_no'),
               ('location', 'location'),
               ('sl_no_1', 'sl_no_1'),
               ('model', 'model'),
               ('make', 'make'),
               ('tel_tvm', 'tel_tvm'),
               ('test_pc', 'test_pc'),
               ('processor', 'processor'),
               ('ram', 'ram'),
               ('hdd', 'hdd'),
               ('asset_no', 'asset_no'),
               ('project_name', 'project_name'),
               ('won_no', 'won_no')]
    select = SelectField('Search for:', choices=choices)
    search = StringField('')


class AssetForm(FlaskForm):
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
    allocation_date = DateField('allocation_date', validators=[DataRequired()])
    project_name = StringField('project_name', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    won_no = StringField('won_no', validators=[optional(), Length(
        min=-1, max=80, message='length must be less than 80 chars')])
    end_date = DateField('end_date', validators=[DataRequired()])
