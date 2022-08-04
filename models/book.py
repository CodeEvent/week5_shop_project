class Book:
    def __init__(self, title, description,stock, buying_cost, selling_price, genre,  ISBN_code, author, id = None):
        
        self.title = title
        self.description = description
        self.stock = stock
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.genre = genre
        self.ISBN_code = ISBN_code
        self.author = author
        self.id = id