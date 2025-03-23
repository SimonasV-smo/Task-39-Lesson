from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from database import setup_db, db
from models import Book

app = Flask(__name__)
CORS(app)
setup_db(app)

@app.route('/', methods=['GET'])
def index():
    return "Sveiki, API veikia!"


# GET /books - visos knygos
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# POST /books - pridėti knygą
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        year=data['year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# PUT /books/<id> - redaguoti knygą
@app.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404)

    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)

    db.session.commit()
    return jsonify(book.to_dict())

# DELETE /books/<id> - ištrinti knygą
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404)

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Knyga ištrinta sėkmingai!"})

if __name__ == '__main__':
    app.run(debug=True)
