import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [year, setYear] = useState('');
  const [search, setSearch] = useState('');
  const [editingId, setEditingId] = useState(null);

  const fetchBooks = () => {
    fetch('http://127.0.0.1:5000/books')
      .then(res => res.json())
      .then(data => setBooks(data));
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  const addBook = () => {
    if (!title || !author || !year) {
      alert('Užpildykite visus laukus!');
      return;
    }
    fetch('http://127.0.0.1:5000/books', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, author, year }),
    }).then(fetchBooks);

    setTitle('');
    setAuthor('');
    setYear('');
  };

  const deleteBook = (id) => {
    fetch(`http://127.0.0.1:5000/books/${id}`, { method: 'DELETE' })
      .then(fetchBooks);
  };

  const editBook = (book) => {
    setEditingId(book.id);
    setTitle(book.title);
    setAuthor(book.author);
    setYear(book.year);
  };

  const updateBook = () => {
    fetch(`http://127.0.0.1:5000/books/${editingId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, author, year }),
    }).then(fetchBooks);

    setEditingId(null);
    setTitle('');
    setAuthor('');
    setYear('');
  };

  const filteredBooks = books.filter(book =>
    book.title.toLowerCase().includes(search.toLowerCase()) ||
    book.author.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="App">
      <h1>Knygų valdymas</h1>

      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Pavadinimas" />
      <input value={author} onChange={(e) => setAuthor(e.target.value)} placeholder="Autorius" />
      <input value={year} onChange={(e) => setYear(e.target.value)} placeholder="Metai" type="number" />

      {editingId ? (
        <button onClick={updateBook}>Atnaujinti</button>
      ) : (
        <button onClick={addBook}>Pridėti</button>
      )}

      <input
        type="text"
        placeholder="Ieškoti knygos"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <table>
        <thead>
          <tr>
            <th>Pavadinimas</th>
            <th>Autorius</th>
            <th>Metai</th>
            <th>Veiksmai</th>
          </tr>
        </thead>
        <tbody>
          {filteredBooks.map(book => (
            <tr key={book.id}>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.year}</td>
              <td>
                <button onClick={() => editBook(book)}>Redaguoti</button>
                <button onClick={() => deleteBook(book.id)}>Ištrinti</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
