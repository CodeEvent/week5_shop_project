class Book:
    def __init__(self, 
                 title, 
                 description,
                 stock_quantity, 
                 buying_cost, 
                 selling_price, 
                 genre,  
                 ISBN_code, 
                 author_id, 
                 id = None):
        
        self.title = title
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.genre = genre
        self.ISBN_code = ISBN_code
        self.author_id = author_id
        self.id = id