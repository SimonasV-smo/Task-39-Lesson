from app.__init__ import create_app  # Importuojame funkciją aplikacijos sukūrimui
from app.models import db  # Importuojame SQLAlchemy objektą
from app.routes import routes  # Importuojame Blueprint maršrutus

# Sukuriame Flask aplikaciją
app = create_app()

# Užregistruojame Blueprint maršrutus
app.register_blueprint(routes)

# Užtikriname, kad duomenų bazės lentelės yra sukurtos
with app.app_context():
    db.create_all()  # Sukuria lenteles, jei jų nėra

# Paleidžiame serverį
if __name__ == '__main__':
    app.run(debug=True)
