import pdb
from pickle import TRUE
from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.book_repo as book_repo
import repositories.author_repo as author_repo


author_repo.delete_all()
# book_repo.delete_all()

author1 = Author('Steven', "Dionisio", 'fb_stdio', 'twitter_stdio', 'insta_stdio', True)
author_repo.save(author1)


book1 = Book("365 days", "Descriving life in 365", 3, 3.5, 9,80, "Adventure", "ISBN433-432", 1)
# author_repo.save(book1)

author_repo.update(author1)
# book_repo.update(book1)


# pdb.set_trace