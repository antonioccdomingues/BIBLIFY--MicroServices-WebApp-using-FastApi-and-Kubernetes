import os

# STOCK DB (Postgres)
STOCK_DB_NAME = "stock"
STOCK_DB_USER = os.environ.get("STOCK_DB_USER")
STOCK_DB_PASSWORD = os.environ.get("STOCK_DB_PASSWORD")
STOCK_DB_URL = f"postgresql+asyncpg://{STOCK_DB_USER}:{STOCK_DB_PASSWORD}@stock-db:5432/{STOCK_DB_NAME}"

