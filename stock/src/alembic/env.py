from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine

import sys
from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(parent_dir)

from app.config import STOCK_DB_URL  # noqa
from app.database import Base
from app.database import engine
import app.models 


config = context.config





fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", STOCK_DB_URL)
# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
  
    url = config.get_main_option("sqlalchemy.url")
    #context.configure(
    #    url=getenv("DATABASE_URL"), target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    	

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    #from app.database import engine
    #connectable = engine
    #connectable = engine_from_config(
    #    config.get_section(config.config_ini_section),
    #   prefix='sqlalchemy.',
    #   poolclass=pool.NullPool)
    connectable = AsyncEngine(
        engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )
    
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    run_migrations_offline()
else:
    #run_migrations_online()
    asyncio.run(run_migrations_online())
