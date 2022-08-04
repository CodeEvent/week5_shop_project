from turtle import title
from flask import Flask, render_template, request, redirect, Blueprint
from sqlalchemy import lateral
from models.book import Book   
import repositories.author_repo as author_repo
import repositories.book_repo as book_repo

books_blueprint = Blueprint("books", __name__)

# NEW > GET > '/books/new' = #Returns an HTML form to the browser
@books_blueprint.route("/books/new", methods=['GET']) #NEW
def new_book():
    return render_template('books/new.html')    

# view the book list
@books_blueprint.route("/books")
def list_of_books():
    books = book_repo.select_all()
    return render_template('books/index.html', books=books)

#save a new book
@books_blueprint.route("/books", methods=['POST'])
def save_added_book():
    title = request.form['title']
    description = request.form ['description']
    stock = request.form['stock']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    genre = request.form['genre']
    ISBN_code = request.form['ISBN_code']
    author_id = request.form['author_id']
    book = Book(title, description, stock, buying_cost, selling_price, genre,ISBN_code,author_id)
    book_repo.save(book)
    return redirect("/books")

#show individual books by their id
@books_blueprint.route("/books/<id>")
def show_book_by_id(id):
    book = book_repo.select(id)
    return render_template("books/show.html", book=book)

@books_blueprint.route('/books/<id>/edit')
def edit_book_by_id_already_populated(id):
    book = book_repo.select(id)
    return render_template("books/edit.html", book=book)

@books_blueprint.route('/books/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    description = request.form ['description']
    stock = request.form['stock']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    genre = request.form['genre']
    ISBN_code = request.form['ISBN_code']
    author_id = request.form['author_id']
    book = Book(title, description, stock, buying_cost, selling_price, genre,ISBN_code,author_id)
    book_repo.save(book)
    return redirect('/books')






