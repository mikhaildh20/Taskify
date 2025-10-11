from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # Setup credentials
    server = 'localhost'
    database = 'TaskifyDB'
    username = 'sa'
    password = '123'

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # ambil secret key dari env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)

    # Import routes setelah app & db ready
    from app import routes  

    with app.app_context():
        db.create_all()  # Bikin tabel kalau belum ada

    return app
