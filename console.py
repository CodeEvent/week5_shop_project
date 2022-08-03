import pdb
from pickle import TRUE
from db.run_sql import run_sql
from models.author import Author
import repositories.author_repo as author_repo




author1 = Author('Steven', "Dionisio", 'fb_stdio', 'twitter_stdio', 'insta_stdio', True)
author_repo.save(author1)


# author_repo.delete_all()
author_repo.update(author1)
author_repo.delete(author1.id)


pdb.set_trace()