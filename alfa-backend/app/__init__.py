from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql5413380:GLLT6jDGCh@sql5.freesqldatabase.com:3306/sql5413380'

db = SQLAlchemy(app)

from app import routes