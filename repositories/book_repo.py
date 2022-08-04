from unittest import result

from zmq import bytes_sockopts
from db.run_sql import run_sql
from models.book import Book
from repositories import author_repo


def save(book):
    sql = "INSERT INTO books (title, description, stock, buying_cost, selling_price, genre, ISBN_code,author) VALUES (%s, %s, %s, %s, %s, %s,%s, %s) RETURNING id"
    values = [book.title, book.description, book.stock, book.buing_cost, book.selling_price, book.genre, book.ISBN_code, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book
    
#SELECT ONE
def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'], result['description'], result['stock'], result['selling_price'], result['genre'], result['ISBN_code'], author, result['id'])
    return book

# # SELECT ALL BOOKS
def select_all():
    books = []
    sql = 'SELECT * FROM books'
    results = run_sql(sql)
    
    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], row['description'], row['stock'], row['selling_price'], row['genre'], row['ISBN_code'], author, row['id'])
        book.append(book)
    return books
    

#DELETE ALL
def delete_all():
    sql = 'DELETE FROM books'
    run_sql(sql)
    
#DELETE ONE
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)    
    
#UPDATE AUTHOR'S OBJECT IN THE DB
def update(book):
    sql = "UPDATE book SET (title, description, stock, twitter, selling_price, genre, ISBN_code, author_id) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [book.title, book.description, book.stock, book.buing_cost, book.selling_price, book.genre, book.ISBN_code, book.author.id]
    run_sql(sql, values)
    
    
# EDIT BOOK BY ID
def edit(book):
    sql = 'UPDATE books SET (title, description, stock, twitter, selling_price, genre, ISBN_code, author_id) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s'
    values = [book.title, book.description, book.stock, book.buing_cost, book.selling_price, book.genre, book.ISBN_code, book.author.id]
    run_sql(sql, values)
    
# ADD BOOK BY ID 
def add(book):
    sql = 'INSERT INTO books (title, description, stock, twitter, selling_price, genre, ISBN_code, author_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id'
    values = [book.title, book.description, book.stock, book.buing_cost, book.selling_price, book.genre, book.ISBN_code, book.author.id]
    results = run_sql(sql, values)
    book.id = results[0]['id']
    book.id = id

# # VIEW ALL BOOKS as a replica to the select_all
# def view_all():
#     books = []
    
#     sql = "SELECT * FROM books"
#     results = run_sql(sql)
#     for row in results:
        
#         book = Book(row['title'], row['description'], row['stock'], row['selling_price'], row['genre'], row['ISBN_code'], row['author_id'], row['id'])
#         books.append(book)
#     return books
        

    
# # VIEW BOOK BY ID replica of select by id 
# # def view(id):
#     book = None
#     sql = "SELECT * FROM books WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
    
#     if result is not None:
#         book = Book(result['title'], result['description'], result['stock'], result['selling_price'], result['genre'], result['ISBN_code'], result['author_id'], result['id'])
#     return book



