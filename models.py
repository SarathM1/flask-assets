from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it_store.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Asset(db.Model):
    __tablename__ = 'asset_record'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    emp_no = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), nullable=True)
    seat_no = db.Column(db.Integer, nullable=True, unique=False)
    sl_no_1 = db.Column(db.String(20), nullable=True, unique=False)
    model = db.Column(db.String(80), nullable=True, unique=False)
    make = db.Column(db.String(20), nullable=True, unique=False)
    tel_tvm = db.Column(db.String(20), nullable=True, unique=False)
    test_pc = db.Column(db.String(20), nullable=True, unique=False)
    processor = db.Column(db.String(20), nullable=True, unique=False)
    ram = db.Column(db.String(20), nullable=True, unique=False)
    hdd = db.Column(db.String(20), nullable=True, unique=False)
    asset_no = db.Column(db.String(20), nullable=True, unique=False)
    allocation_date = db.Column(db.String(20), nullable=True, unique=False)
    project_name = db.Column(db.String(20), nullable=True, unique=False)
    won_no = db.Column(db.String(20), nullable=True, unique=False)
    end_date = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return '<Contacts %r>' % self.name
