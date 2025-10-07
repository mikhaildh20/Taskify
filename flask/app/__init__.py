from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup credentials
server = 'localhost'
database = 'TaskifyDB'
username = 'sa'
password = 'polman'

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes