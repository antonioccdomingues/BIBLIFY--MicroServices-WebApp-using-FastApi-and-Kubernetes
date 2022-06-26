from typing import List, Optional

from pydantic import BaseModel


from datetime import date 


class AuthorBase(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):

    user_id: int 
    email: str
    name: Optional[str] 
    is_active : Optional[bool]
    class Config:
        orm_mode = True



class Order(BaseModel):

    id: int
    book_id: int
    requester_id: int
    status: Optional[str] 
    begin_date: Optional[date] 
    end_date: Optional[date] 
    complete: Optional[bool] 
    class Config:
        orm_mode = True 


class BookBase(BaseModel):

    book_id: int
    title: str
    date: Optional[date] 
    amount_in_stock: int
    amount_reserved: int

    class Config:
        orm_mode = True

class BookSchema(BookBase):
    authors: List[AuthorBase]

class AuthorSchema(AuthorBase):
    books: List[BookBase]  


class ApiResponse(BaseModel):

    code: Optional[int] 
    type: Optional[str] 
    message: Optional[str] 
    class Config:
        orm_mode = True
