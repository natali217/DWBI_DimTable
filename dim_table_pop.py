import pandas as pd
import pyodbc 

# connect database 
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-23GC4NEK;'
                      'Database=Studying;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Studying.dbo.Person')

for row in cursor:
    print(row)