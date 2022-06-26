from sqlalchemy.orm import Session
from . import schemas
from . import models
import array 
from sqlalchemy.future import select
from sqlalchemy import delete
from sqlalchemy.orm import selectinload,joinedload

async def get_books(db:Session, title: str=None, author: str = None, id: int = None):

    query = select(models.Book).options(joinedload(models.Book.authors))
    books = await db.execute(select(models.Book).options(joinedload(models.Book.authors)))  
    if id is not None:
        query = select(models.Book).options(joinedload(models.Book.authors)).where(models.Book.book_id == id)
    if title is not None:
        query = select(models.Book).options(joinedload(models.Book.authors)).where(models.Book.title.contains(title))
    books = await db.execute(query)
    books = books.scalars().unique()
    if author is not None:
        books2=[]

        for b in books:
            for a in b.authors:
                if author in a.name:
                    books2.append([schemas.BookSchema(book_id=b.book_id, title=b.title, date=b.date, amount_in_stock=b.amount_in_stock, amount_reserved=b.amount_reserved, authors=b.authors)])
        if books2!=[]:
            return books2

    return  [ schemas.BookSchema(book_id=b.book_id, title=b.title, date=b.date, amount_in_stock=b.amount_in_stock, amount_reserved=b.amount_reserved, authors=b.authors) for b in books]
  
async def get_book_id(db:Session, id :int=None ):
    
    if id is not None:
        book = await db.execute(select(models.Book).options(joinedload(models.Book.authors)).filter(models.Book.book_id == id))
        books = book.scalars().unique()
        return [ schemas.BookSchema(book_id=b.book_id, title=b.title, date=b.date, amount_in_stock=b.amount_in_stock, amount_reserved=b.amount_reserved, authors=b.authors) for b in books]
  
    else:
        return None


async def save_book(db: Session, info: schemas.BookSchema):
    b = info.dict()
    
    auths = b['authors']
    ids = [a['id'] for a in auths]
    authors = []
    for id in ids:
        a = await db.execute(select(models.Author).where(models.Author.id == id))
        a= a.scalars().first()
        if a is None:
            return None
        authors.append(a)
    
    book = models.Book(book_id=b['book_id'], title=b['title'], date=b['date'], amount_in_stock=b['amount_in_stock'], amount_reserved=b['amount_reserved'])
    book.authors = authors
    db.add(book)

    await db.commit()
    await db.refresh(book)
    
    return book

async def delete_book(db: Session, id:int):
    query = delete(models.book_authors).where(models.book_authors.c.book_id == id)
    await db.execute(query)
    query= delete(models.Book).where(models.Book.book_id==id)
    await db.execute(query)
    await db.commit()
    return "Delted Successfully"

def udpate_book( db:Session, id:int, stock:int, booked:int, name:str=""):
    b = db.query(models.Book).filter(models.Book.book_id==id)
    record = b.one()
    if stock is not None:
        record.amount_in_stock = stock
    if booked is not None:
        record.amount_reserved = booked
    if name is not "":
        record.name = name
    db.commit()

##########################

async def get_orders(db:Session, book_id: int = None, book_title: str =None, requester: int = None,status: str=None, begin_date: str=None, end_date: str=None):
    
    query = select(models.Order)

    if book_id is not None:
        query=select(models.Order).where(models.Order.book_id == book_id)

    if requester is not None:
        query=select(models.Order).where(models.Order.requester_id == requester)
    if status is not None:
        query=select(models.Order).where(models.Order.status == status)
    if begin_date is not None:
        query=select(models.Order).where(models.Order.begin_date == begin_date)
    if end_date is not None:
        query=select(models.Order).where(models.Order.end_date == end_date)

    orders = await db.execute(query)
    orders = orders.scalars().all()
    
    return orders

async def save_order(db: Session, info: schemas.Order):

    
    o = info.dict()
    book = o['book_id']
    user = o['requester_id']
    book = await db.execute(select(models.Book).where(models.Book.book_id == book))
    book=book.scalars().first()
    if book is None:
        return None
    user = await db.execute(select(models.User).where(models.User.user_id == user))
    user=user.scalars().first()
    if user is None:
        return None

    order = models.Order(id=o['id'], book_id=o['book_id'],requester_id=o['requester_id'],status=o['status'],begin_date=o['begin_date'],end_date=o['end_date'], complete=o['complete']) 

    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

def delete_order(db: Session, id:int):
    db.query(models.Order).filter(models.Order.id==id).delete()
    db.commit()
    return 

################################

async def save_author(db: Session, info: schemas.AuthorBase):
    author = models.Author(**info.dict())
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return author

async def delete_author(db: Session, id:int):

    query = delete(models.book_authors).where(models.book_authors.c.author_id == id)
    await db.execute(query)
    query = delete(models.Author).where(models.Author.id == id)
    await db.execute(query)
    await db.commit()

    return "Deleted Successfully"

async def get_author(db:Session, name: str = None, id: int =None):
    authors = await db.execute(select(models.Author)) 
    if name is not None:
        authors = await db.execute(select(models.Author).where(models.Author.name.contains(name))) 
    if id is not None:
        authors = await db.execute(select(models.Author).filter(models.Author.id == id))
    authors = authors.scalars().all()
    return [schemas.AuthorBase(id=a.id,name=a.name) for a in authors]
############################

async def get_user(db:Session, id: int =None):
    users = await db.execute(select(models.User))
    if id is not None:
        users = await db.execute(select(models.User).filter(models.User.user_id == id))
    users = users.scalars().all()
    return [schemas.User(user_id=a.user_id,email=a.email, name=a.name, is_active=a.is_active) for a in users]

async def save_user(db: Session, info: schemas.User):
    user = models.User(**info.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db: Session, id:int):
    query = delete(models.User).where(models.User.user_id == id)
    await db.execute(query)
    await db.commit()

    return "Deleted Successfully"


