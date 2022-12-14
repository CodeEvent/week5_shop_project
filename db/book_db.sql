DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  fb_page VARCHAR(255), 
  twitter VARCHAR(255), 
  instagram VARCHAR(255),
  active BOOLEAN

);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  stock INT,
  buying_cost INT,
  selling_price INT,
  genre VARCHAR,
  isbn_code VARCHAR,
  author_id INT REFERENCES authors(id)
);


