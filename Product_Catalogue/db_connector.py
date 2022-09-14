#!/usr/bin/python3
import MySQLdb 

my_connection = MySQLdb.connect(host='localhost', user='root', passwd='Ak0881216#', db='Products_db')
my_cursor = my_connection.cursor()
