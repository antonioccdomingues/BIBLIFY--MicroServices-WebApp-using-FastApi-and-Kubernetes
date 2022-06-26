from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import ARRAY,UUID
from sqlalchemy.orm import relationship


from .database import Base 


book_authors = Table('book_authors', Base.metadata,
    Column('book_id', ForeignKey('books.book_id'), primary_key=True),
    Column('author_id', ForeignKey('authors.id'), primary_key=True)
)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    books = relationship ("Book", secondary="book_authors", back_populates='authors')



class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, index=True)
    title =  Column(String, index=True, nullable=False)
    date = Column(Date)
    amount_in_stock = Column(Integer)
    amount_reserved = Column(Integer)
    authors = relationship("Author", secondary="book_authors",uselist=True, back_populates='books')

    

class Order(Base):
    __tablename__='orders'
  
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    requester_id = Column( Integer, ForeignKey('users.user_id'))
    status = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    complete = Column(Boolean)

    

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)


