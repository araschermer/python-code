# Create a database with three tables: authors, books, authorbooks
# Authors: id, first_name, last_name columns
#  Books: id, title and number of pages columns
# AuthorBooks: id, author_id, book_id
# Author books pairings are separated, to easily store books by the same author
# for books with multiple authors, multiple entries would be added to the author books table
# functionalities-to implement:
# 1- books table should be updated with the new book
#  if the author is a new author, then authors table should be updated to include the new author,
#  otherwise authors should not be duplicated
# The authorbook table should be updated with the new book

# Solution using psycopg2
import psycopg2
import os

PASSWORD = os.environ.get('PASSWORD')
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres",
                              host="localhost",
                              password=PASSWORD,
                              port="5432",
                              database="library"
                              )
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Creating a database
cursor.execute('''CREATE database library1;''')

# Create three tables authors, books and author_books
# Authors: id, first_name, last_name columns
# Books: id, title and number of pages columns
# AuthorBooks: id, author_id, book_id
cursor.execute('''DROP TABLE  if exists books CASCADE;''')
cursor.execute('''DROP TABLE  if exists authors CASCADE;''')
cursor.execute('''DROP TABLE  if exists author_books CASCADE;''')

cursor.execute('''create table authors( author_id  SERIAL PRIMARY KEY ,first_name TEXT, last_name TEXT);''')
cursor.execute('''create table books( book_id SERIAL PRIMARY KEY ,title TEXT NOT NULL , pages_number TEXT);''')
cursor.execute('''create table author_books( author_book_id  SERIAL PRIMARY KEY ,author_id INT, book_id INT,
 FOREIGN KEY (author_id) REFERENCES authors(author_id),FOREIGN KEY (book_id) REFERENCES books(book_id));''')


# view data in the table :
# cursor.execute("SELECT * FROM books")
# print(cursor.fetchall())
# to insert a new sale into the database :
def check_if_author_exists(title):
    pass


def inset_book(title, pages_number, first_name, last_name):
    try:
        new_book_id = cursor.execute('''INSERT INTO books (title, pages_number) VALUES(%s, %s) RETURNING book_id''',
                                     (title, pages_number))
        author_id = None
        if not check_if_author_exists(title):
            author_id = cursor.execute(
                '''INSERT INTO authors (first_name, last_name) VALUES(%s, %s) RETURNING book_id''',
                (first_name, last_name))
        else:
            author_id = cursor.execute('''SELECT author_id FROM authors WHERE  first_name=%s''', (first_name,))
        author_book_id = cursor.execute(
            '''INSERT INTO author_books (author_id, book_id) VALUES(%s, %s) RETURNING author_book_id''',
            (author_id, new_book_id))
    except:
        connection.rollback()
        # commit changes
    finally:
        connection.commit()


# solution using SQLAlchemy core


# solution using SQLAlchemy ORM
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

connection = psycopg2.connect(user="postgres",
                              host="localhost",
                              password=PASSWORD,
                              port="5432",
                              )
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Creating a database
cursor.execute('''CREATE database library3;''')
engine = create_engine(f'postgres://postgres:{PASSWORD}@localhost:5432/library3')
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))

    def __repr__(self):
        return f"<Author(author_id='{self.author_id}', first_name='{self.first_name}', last_name='{self.last_name}'>"


class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    pages_number = Column(Integer)

    def __repr__(self):
        return f"<Book(book_id='{self.book_id}', title='{self.title}', pages_number='{self.pages_number}'>"


class AuthorBooks(Base):
    __tablename__ = 'author_books'

    author_book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    author = relationship("Author")
    book = relationship("Book")

    def __repr__(self):
        return f'''<AuthorBooks(author_book_id='{self.author_book_id}', author_first_name='{self.author.first_name}',
         author_last_name='{self.author.last_name}', book_title='{self.book.title}'>'''


Base.metadata.create_all(engine)


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_book(title, pages_number, first_name, last_name):
    book = Book(title=title, pages_number=pages_number)

    session = create_session()

    try:
        existing_author = session.query(Author).filter(Author.first_name ==
                                                       first_name, Author.last_name == last_name).first()

        session.add(book)

        if existing_author is not None:
            session.flush()
            book_author_pair = AuthorBooks(author_id=existing_author.author_id,
                                           book_id=book.book_id)
        else:
            author = Author(first_name=first_name, last_name=last_name)
            session.add(author)
            session.flush()
            book_author_pair = AuthorBooks(author_id=author.author_id,
                                           book_id=book.book_id)

        session.add(book_author_pair)
        session.commit()

        print(book_author_pair)

    except:
        session.rollback()
        raise

    finally:
        session.close()
