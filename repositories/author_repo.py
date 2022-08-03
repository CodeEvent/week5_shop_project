from unittest import result
from db.run_sql import run_sql
from models.author import Author


def save(author):
    sql = "INSERT INTO authors (first_name, last_name, fb_page, twitter, instagram, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [author.first_name, author.last_name, author.fb_page, author.twitter, author.instagram, author.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author
    
#SELECT ONE
def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        author = Author(result['first_name'], result['last_name'], result['fb_page'], result['twitter'], result['instagram'], result['active'], result['id'])
    return author

# SELECT ALL AUTHORS
def select_all():
    authors = []
    sql = 'SELECT * FROM authors'
    results = run_sql(sql)
    
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['fb_page'], row['twitter'], row['instagram'], row['active'], row['id'])
        authors.append(author)
    return authors
    

# #DELETE ALL
# def delete_all():
#     sql = 'DELETE FROM authors'
#     run_sql(sql)
    
#DELETE ONE
def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)    
    
#UPDATE AUTHOR'S OBJECT IN THE DB
def update(author):
    sql = "UPDATE authors SET (first_name, last_name, fb_page, twitter, instagram, active) = (%s,%s,%s,%s,%s, %s) WHERE id = %s"
    values = [author.first_name, author.last_name, author.fb_page, author.twitter, author.instagram, author.active, author.id]
    run_sql(sql, values)
    
    
# EDIT AUTHOR BY ID
def edit(author):
    sql = 'UPDATE members SET (first_name, last_name, fb_page, twitter, instagram,active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [author.first_name, author.last_name, author.fb_page, author.member_twitter, author.instagram, author.active, author.id]
    run_sql(sql, values)
    
# EDIT AUTHOR BY ID 
def add(author):
    sql = 'INSERT INTO authors (first_name, last_name, fb_page, twitter, instagram, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id'
    values = [author.first_name, author.last_name, author.fb_page, author.twitter, author.instagram, author.active, author.id]
    results = run_sql(sql, values)
    author.id = results[0]['id']
    author.id = id

# VIEW ALL AUTHORS
def view_all():
    authors = []
    
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['fb_page'], row['twitter'], row['instagram'],row['active'],row['id'])
        authors.append(author)
    return authors
        

    
# VIEW AUTHOR BY ID
def view(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        author = Author(
            result['first_name'],
            result['last_name'], 
            result['fb_page'], 
            result['twitter'], 
            result['instagram'],
            result['active'],
            result['id'])
        
    return author