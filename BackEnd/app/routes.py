from flask import Blueprint, request, jsonify
from app.models import db, Book

# Sukuriame Blueprint objektą maršrutams
routes = Blueprint('routes', __name__)


# 1. Gauti visas knygas (GET /books)
@routes.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()  # Gaunamos visos knygos
    return jsonify([book.to_dict() for book in books]), 200  # Grąžiname JSON sąrašą


# 2. Pridėti naują knygą (POST /books)
@routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or not all(key in data for key in ['title', 'author', 'year']):
        return jsonify({"error": "Missing required fields"}), 400  # Klaida, jei trūksta laukų

    new_book = Book(
        title=data['title'],
        author=data['author'],
        year=data['year']
    )
    db.session.add(new_book)
    db.session.commit()  # Išsaugome įrašą duomenų bazėje
    return jsonify(new_book.to_dict()), 201  # Grąžiname sukurtą knygą


# 3. Redaguoti esamą knygą (PUT /books/<id>)
@routes.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)  # Randa knygą pagal ID arba grąžina 404 klaidą
    book.title = data.get('title', book.title)  # Atnaujina pavadinimą, jei pateikta
    book.author = data.get('author', book.author)  # Atnaujina autorių, jei pateikta
    book.year = data.get('year', book.year)  # Atnaujina metus, jei pateikta
    db.session.commit()  # Išsaugome pakeitimus
    return jsonify(book.to_dict()), 200  # Grąžiname atnaujintą knygą


# 4. Ištrinti knygą (DELETE /books/<id>)
@routes.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)  # Randa knygą pagal ID arba grąžina 404 klaidą
    db.session.delete(book)
    db.session.commit()  # Ištrinamas įrašas
    return jsonify({"message": "Book deleted"}), 200  # Grąžiname patvirtinimą
