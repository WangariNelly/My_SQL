#!/usr/bin/python3

from sqlalchemy import  create_engine

"""Connecting to MySQL server at localhost using mysql-python DBAPI """

engine = create_engine("mysql+mysqldb://root:Ak0881216#@localhost/Products_db" ,
echo=True, pool_size=5, max_overflow=10, encoding='utf-8'
)


engine.connect()

print(engine)
