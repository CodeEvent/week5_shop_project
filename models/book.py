class Book:
    def __init__(self, title, description , genre, price, bar_code, author_id, id = None):
        self.title = title
        self.description = description
        self.genre = genre
        self.price = price
        self.bar_code = bar_code
        self.author_id = author_id
        self.id = id