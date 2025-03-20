from flask_sqlalchemy import SQLAlchemy

# Sukuriame SQLAlchemy objektą, bet jo nepririšame prie aplikacijos
db = SQLAlchemy()

def init_db(app):
    """Inicializuojame duomenų bazę su Flask aplikacija"""
    db.init_app(app)  # Prijungiame duomenų bazę prie aplikacijos
    with app.app_context():
        db.create_all()  # Sukuriame lenteles, jei jų nėra
