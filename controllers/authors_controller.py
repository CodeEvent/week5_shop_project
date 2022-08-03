from multiprocessing.dummy import active_children
from flask import Flask, render_template, request, redirect, Blueprint
from sqlalchemy import lateral
from models.author import Author
import repositories.book_repo as book_repo
import repositories.author_repo as author_repo

authors_blueprint = Blueprint("authors", __name__)

# NEW > GET > '/authors/new' = #Returns an HTML form to the browser
@authors_blueprint.route("/authors/new", methods=['GET']) #NEW
def new_author():
    return render_template('authors/new.html')    

# view the author list
@authors_blueprint.route("/authors")
def list_of_authors():
    authors = author_repo.select_all()
    return render_template('authors/index.html', authors=authors)

#save a new author
@authors_blueprint.route("/authors", methods=['POST'])
def save_added_author():
    first_name = request.form['first_name']
    last_name = request.form ['last_name']
    active = request.form['active']
    fb_page = request.form['fb_page']
    twitter = request.form['twitter']
    instagram = request.form['instagram']
    author = Author(first_name, last_name, fb_page, twitter, instagram, active)
    author_repo.save(author)
    return redirect("/authors")

#show individual authors by their id
@authors_blueprint.route("/authors/<id>")
def show_author_by_id(id):
    author = author_repo.select(id)
    return render_template("authors/show.html", author=author)

@authors_blueprint.route('/authors/<id>/edit')
def edit_author_by_id_already_populated(id):
    author = author_repo.select(id)
    return render_template("authors/edit.html", author=author)

@authors_blueprint.route('/authors/<id>', methods=['POST'])
def update_author(id):
    author = author_repo.select(id)
    first_name = request.form['first_name']
    last_name = request.form ['last_name']
    active = request.form['active']
    author.first_name = first_name
    author.last_name = last_name
    author.active = active
    author_repo.update(author)
    return redirect('/authors')





# CREATE > POST > '/tasks'
#Receives the data from  the form to insert into the DB



