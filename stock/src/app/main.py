from typing import List,Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from . import crud, models, schemas

from .database import SessionLocal, engine
#import database

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from starlette.middleware.cors import CORSMiddleware

import asyncio




async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

async def db() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as db:
        yield db



loop = asyncio.get_event_loop()
task = loop.create_task(init_db())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

###############____BOOKS___#############################################

@app.get('/v1/book')#, response_model=List[schemas.Book])
async def read_books(db=Depends(db), title: Optional[str] = None, author:Optional[str]=None, id:Optional[int]=None):
    books = await crud.get_books(db, title=title, author=author, id=id)
    if books is None:
        raise HTTPException(status_code=404, detail="Books not found")
    
    return books


@app.post('/v1/book')
async def post_book(book: schemas.BookSchema,db=Depends(db)):

    book2 = await crud.save_book(db, book)
    print(book2)
    if book2 is None:
        raise HTTPException(status_code=404, detail="Unknown Author id")
    return book2

@app.delete('/v1/book/{bookId}' )
async def delete_book(bookId:int,db=Depends(db)):
    msg = await crud.delete_book(db, bookId)
    return msg

##########################____ORDERS________#################################

@app.post('/v1/order')
async def post_order(book: schemas.Order,db=Depends(db)):
    order = await crud.save_order(db, book)
    if order is None:
        raise HTTPException(status_code=404, detail="Unknown Book or User id")
    return order

@app.get('/v1/order') # response_model=List[schemas.Order])
async def read_orders( book_id: Optional[int] =None, book_title: Optional[str]=None, requester: Optional[int]=None, status:Optional[str]=None,begin_date:Optional[str]=None,end_date:Optional[str]=None, db=Depends(db),):
    order = await crud.get_orders(db, book_id,book_title, requester, status, begin_date, end_date)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return order

############################__AUTHORS___########################################################

@app.post('/v1/author')
async def post_author(author: schemas.AuthorBase,db=Depends(db)):
    return await crud.save_author(db, author)

@app.get('/v1/author')#, response_model=schemas.Author)
async def get_author(id: Optional[int] =None, name: Optional[str]=None,db=Depends(db)):
    return await crud.get_author(db, name, id)

@app.delete('/v1/author/{id}' )
async def delete_book(id:int,db=Depends(db)):
    msg = await crud.delete_author(db, id)
    return msg

############################__USERS___########################################################


@app.post('/v1/user')
async def post_user(user: schemas.User,db=Depends(db)):
    return await crud.save_user(db, user)

@app.get('/v1/user')
async def get_user(id: Optional[int] =None, db=Depends(db)):
    return await crud.get_user(db, id)

@app.delete('/v1/user/{id}' )
async def delete_user(id:int,db=Depends(db)):
    msg = await crud.delete_user(db, id)
    return msg


