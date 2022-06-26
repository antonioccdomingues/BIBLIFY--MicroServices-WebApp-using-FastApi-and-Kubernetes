from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

import os

from .config import STOCK_DB_URL 



USER = os.environ.get('POSTGRES_USER') 
PASS = os.environ.get('POSTGRES_PASSWORD') 
HOSTNAME = os.environ.get('SERVICE') 
DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASS}@{HOSTNAME}/stock"


engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
