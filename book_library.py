from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)              # Unique identifier
    title = db.Column(db.String(100), nullable=False)         # Title of the book
    author = db.Column(db.String(100), nullable=False)        # Author name
    genre = db.Column(db.String(50), nullable=True)           # Genre (optional)
    year = db.Column(db.Integer, nullable=True)               # Year published
    available = db.Column(db.Boolean, default=True)  

    def __repr__(self):
        return f"{self.title}-{self.author},{self.genre},{self.year},{self.available}"

@app.route('/')
def home():
    return 'welcome to BooK_LiBraRy:)'

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get(id)
    return{"id":book.id,"title":book.title,"author":book.author,"genre":book.genre,"year":book.year,"available":book.available}

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {"id":book.id,"title":book.title,"author":book.author,"genre":book.genre,"year":book.year,"available":book.available}
        output.append(book_data)
    return{"books":output}

@app.route('/books', methods =['POST'])
def add_book():
    book = Book(title=request.json['title'],author=request.json['author'],genre=request.json['genre'],year=request.json['year'],available=request.json['available'])
    db.session.add(book)
    db.session.commit()
    return {"id":book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return{"error":"Not Found!"}
    db.session.delete(book)
    db.session.commit()
    return {"message":"yeet!@ flashed!"}

@app.route('/books/<id>',methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        return{"error":"Not Found"}
    book.title = request.json['title']
    book.author = request.json['author']
    book.genre = request.json['genre']
    book.year = request.json['year']
    book.available = request.json['available']
    db.session.commit()
    return {"message":"updated Book data!"}

@app.route('/books/<id>',methods=['PATCH'])
def patch_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error":"Not found!"}
    if "title" in request.json:
        book.title = request.json['title']
    if "author" in request.json:
        book.author = request.json['author']
    if "genre" in request.json:
        book.genre = request.json['genre']
    if "year" in request.json:
        book.year = request.json['year']
    if "available" in request.json:
        book.available = request.json['available']
    db.session.commit()
    return {"message":"patched the Book successfully!"}
