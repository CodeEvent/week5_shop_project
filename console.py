from bdb import set_trace
import pdb
from models.book import Book
from models.author import Author


import repositories.book_repo as book_repo
import repositories.author_repo as author_repo

book_repo.delete_all()
author_repo.delete_all()


# author1 = Author('Steven', "Dionisio", 'fb_stdio', 'twitter_stdio', 'insta_stdio', True)
# author_repo.save(author1)

author2 = Author('Harry', "White", 'fb_stdio', 'twitter_stdio', 'insta_stdio', True)
author_repo.save(author2)


# book1 = Book("365 days", "Descriving life in 365", 3, 3.5, 9.80, "Adventure", "ISBN433-432", author1)
# book_repo.save(book1)


book = Book("The lion", "in the jungle", 3,3,9, "Adventure", "ISBN433-432", author2)
book_repo.save(book)


books = book_repo.select_all()
# for book in books:
#     print(book.__dict__)




pdb.set_trace()