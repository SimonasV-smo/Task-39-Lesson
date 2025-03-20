from app.__init__ import db

class Book(db.Model):
    __tablename__ = 'books'  # Lentelės pavadinimas duomenų bazėje

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Knygos pavadinimas
    author = db.Column(db.String(100), nullable=False)  # Autorius
    year = db.Column(db.Integer, nullable=False)  # Leidimo metai

    def to_dict(self):
        """Konvertuoja objektą į žodyną (dict), kad būtų lengviau siųsti kaip JSON atsakymą"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
