#!/usr/bin/python3
from db_connector import my_connection, my_cursor
import MySQLdb
from operations import Operations

if __name__ == "__main__":
   db = Operations()

print("WELCOME TO MY QUERY!")
print("*************MENU**************")
print("0 - Insert\n1 -View all\n2 - Update_by_id\n3 -Delete_by_id" )

choice = int(input("Enter choice: "))

if choice == 0:
   db.insert_product()
elif choice == 1:
   db.list_all()
elif choice == 2:
   db.update_by_id
elif choice == 3:
   db.delete_by_id()

my_cursor.close()
my_connection.close()
