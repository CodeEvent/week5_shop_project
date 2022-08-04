from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book   

import repositories.book_repo as book_repo
import repositories.author_repo as author_repo

from repositories.book_repo import select_all

books_blueprint = Blueprint("books", __name__)

# NEW > GET > '/books/new' = #Returns an HTML form to the browser
@books_blueprint.route("/books/new", methods=['GET']) #NEW
def books():
    authors = select_all()
    books = book_repo.select_all()
    return render_template('books/new.html', books=books, authors=authors)    

# view the book list
@books_blueprint.route("/books")
def list_of_books():
    books = book_repo.select_all()
    return render_template('books/index.html', books=books)

#save a new book
@books_blueprint.route("/books", methods=['POST'])
def save():
    title = request.form['title']
    description = request.form ['description']
    stock = request.form['stock']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    genre = request.form['genre']
    isbn_code = request.form['isbn_code']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, description, stock, buying_cost, selling_price, genre,isbn_code,author)
    book_repo.save(book)
    return redirect('/books')

#show individual books by their id
@books_blueprint.route("/books/<id>")
def show_book_by_id(id):
    book = book_repo.select(id)
    return render_template("books/show.html", book=book)

@books_blueprint.route('/books/<id>/edit')
def edit_book_by_id_already_populated(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template("books/edit.html", book=book, authors=authors)

@books_blueprint.route('/books/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    description = request.form ['description']
    stock = request.form['stock']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    genre = request.form['genre']
    isbn_code = request.form['isbn_code']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, description, stock, buying_cost, selling_price, genre,isbn_code,author,id)
    book_repo.update(book)
    return redirect('/books')





@books_blueprint.route("/books/add")
def add_book():
    authors = author_repo.select_all()
    return render_template("books/add.html", authors = authors)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    description = request.form ['description']
    stock = request.form['stock']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    genre = request.form['genre']
    isbn_code = request.form['isbn_code']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, description, stock, buying_cost, selling_price, genre,isbn_code,author)
    book_repo.save(book)
    return redirect('/books')



