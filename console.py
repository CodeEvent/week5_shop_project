import pdb
from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repo as author_repo
import repositories.book_repo as book_repo





author1 = Author('Steven', "Dionisio", 'fb_stdio', 'twitter_stdio', 'insta_stdio')
author_repo.save(author1)


# author_repo.delete_all()
# book_repo.delete_all
author_repo.update(author1)
# author_repo.delete(author1.id)
# book_repo.delete(book1.id)

pdb.set_trace()