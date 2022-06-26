FROM python:3.7
WORKDIR /usr/src/book_stock
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app ./app
COPY ./alembic ./alembic
COPY alembic.ini alembic.ini
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0" , "--reload"]

