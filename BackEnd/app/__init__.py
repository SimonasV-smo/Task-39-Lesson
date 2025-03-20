from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicializuojame SQLAlchemy objektą
db = SQLAlchemy()


def create_app():
    # Sukuriame Flask aplikaciją
    app = Flask(__name__)

    # Konfigūruojame duomenų bazę
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Įgaliname CORS
    CORS(app)

    # Prijungiame SQLAlchemy prie aplikacijos
    db.init_app(app)

    return app
