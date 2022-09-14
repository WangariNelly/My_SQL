#!/usr/bin/python3

from db_connector import my_connection, my_cursor
from datetime import  datetime

class  Operations:
   """ This class contains all database operations
   """
   def insert_product(self,Product_name, Price):
      """ This method inserts a new product into a table
      """
      try:

         sql = ("INSERT INTO Products(Product_name, Price, Date_) VALUES(%s, %s ,%s)")
         my_cursor.execute(sql, (Product_name, Price,))
         my_connection.commit()
         print("inserted")

      except:
         print("not  inserted")

   def list_all(self):
      """This method reads all data from the products table."""

      sql = ("SELECT * FROM Products")
      my_cursor.execute(sql)
      result = my_cursor.fetchall()
      for i in result:
         print(i)

   def update_by_id(self,new_id, old_id):
      """This method updates new data to products table"""

      sql = ("UPDATE Products SET new_id=%s WHERE old_id=%S")
      my_cursor.execute(sql,new_id,old_id,)
      my_connection.commit()

   def delete_by_id(self,id):
      """This method deletes data from products"""

      sql= ("DELETE FROM Products WHERE id=%s")
      my_cursor.execute(sql,id,)
      my_connection.commit()
      self.list_all()

