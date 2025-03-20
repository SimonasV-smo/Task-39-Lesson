from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app
from models import db
from routes import routes

app = create_app()

# Inicializuojame duomenų bazę su aplikacija
db.init_app(app)

# Užregistruojame maršrutus
app.register_blueprint(routes)

# Sukuriame duomenų bazę (jei ji dar neegzistuoja)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
