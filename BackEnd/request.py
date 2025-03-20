import requests

BASE_URL = "http://127.0.0.1:5000/books"

def get_books():
    """Gauti visas knygas"""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("GET /books:", response.json())
    else:
        print("Error:", response.status_code, response.text)

def add_book(title, author, year):
    """Pridėti naują knygą"""
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    response = requests.post(BASE_URL, json=new_book)
    if response.status_code == 201:
        print("POST /books (Added):", response.json())
    else:
        print("Error:", response.status_code, response.text)

def update_book(book_id, title, author, year):
    """Redaguoti esamą knygą"""
    updated_book = {
        "title": title,
        "author": author,
        "year": year
    }
    response = requests.put(f"{BASE_URL}/{book_id}", json=updated_book)
    if response.status_code == 200:
        print("PUT /books/{id} (Updated):", response.json())
    else:
        print("Error:", response.status_code, response.text)

def delete_book(book_id):
    """Ištrinti knygą"""
    response = requests.delete(f"{BASE_URL}/{book_id}")
    if response.status_code == 200:
        print("DELETE /books/{id} (Deleted):", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    # Testavimas
    print("Gauti visas knygas:")
    get_books()

    print("\nPridėti naują knygą:")
    add_book("1984", "George Orwell", 1949)

    print("\nRedaguoti knygą:")
    update_book(1, "Animal Farm", "George Orwell", 1945)

    print("\nIštrinti knygą:")
    delete_book(1)

    print("\nGauti visas knygas po pakeitimų:")
    get_books()
