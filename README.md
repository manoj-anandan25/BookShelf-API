## Book Library API – Flask + SQLite

A simple and powerful RESTful API for managing a digital book library, built with Python, Flask, and SQLite.

This API allows you to create, read, update, and delete book records.  hggfx
Perfect for learning backend development, testing REST APIs, or integrating into a frontend/book management app.

---
 Features

-  View all books
-  View a book by ID
-  Add a new book
-  Update full book record (PUT)
-  Update part of a book record (PATCH)
-  Delete a book

---

Book Model

Each book contains the following fields:

| Field     | Type     | Required | Description              |
|-----------|----------|----------|--------------------------|
| `id`      | Integer  | Auto     | Unique book ID           |
| `title`   | String   | Yes      | Title of the book        |
| `author`  | String   | Yes      | Author's name            |
| `genre`   | String   | No       | Genre of the book        |
| `year`    | Integer  | No       | Year of publication      |
| `available` | Boolean | No (default `True`) | Is book available? |

---

Base URL

```

[http://localhost:5000](http://localhost:5000)

````


 API Endpoints

GET `/books`

Returns a list of all books.

**Response:**
```json
{
  "books": [
    {
      "id": 1,
      "title": "1984",
      "author": "George Orwell",
      "genre": "Dystopian",
      "year": 1949,
      "available": true
    }
  ]
}
````

---

 GET `/books/<id>`

Returns a book by ID.

```http
GET /books/1
```

Response:

```json
{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "genre": "Dystopian",
  "year": 1949,
  "available": true
}
```


POST `/books`

Adds a new book.

Headers:

```
Content-Type: application/json
```

Body Example:

```json
{
  "title": "1984",
  "author": "George Orwell",
  "genre": "Dystopian",
  "year": 1949,
  "available": true
}
```

Response:

```json
{
  "id": 1
}
```

---

 DELETE `/books/<id>`

Deletes a book by ID.

```http
DELETE /books/1
```

Response:

```json
{
  "message": "yeet!@ flashed!"
}
```



 PUT `/books/<id>`

Fully updates a book record.

Body Example:

```json
{
  "title": "Animal Farm",
  "author": "George Orwell",
  "genre": "Political Satire",
  "year": 1945,
  "available": false
}
```

Response:

```json
{
  "message": "updated Book data!"
}
```



PATCH `/books/<id>`

Partially updates a book record.

Body Example:

```json
{
  "available": false
}
```

Response:

```json
{
  "message": "patched the Book successfully!"
}
```


 How to Run Locally

1. Clone the repo

```bash
git clone https://github.com/yourusername/book-library-api.git
cd book-library-api
```

 2. Install requirements

```bash
pip install flask flask_sqlalchemy
```

3. Run the application

```bash
python app.py
```

The app will be live at:
`http://localhost:5000`

---

 Test the API Using

* [Postman](https://www.postman.com/)
* curl
* HTTP client in your frontend app

---

 Project Structure

```
book-library-api/
├── app.py           # Main Flask app
├── data.db          # SQLite database (auto-created)
└── README.md        # Project documentation
```

---

 Notes

* The database (`data.db`) is created automatically on first run.
* You can view it with any SQLite viewer or CLI.
* Add more fields like ISBN, ratings, etc. to extend functionality.



