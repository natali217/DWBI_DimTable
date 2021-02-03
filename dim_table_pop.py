import pandas as pd
import pyodbc 

# connect database 
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-23GC4NEK;'
                      'Database=Studying;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


# cursor.execute('''
#                 INSERT INTO Studying.dbo.Test(Name, Age)
#                 VALUES
#                 ('Bob',55),
#                 ('Jenny',66)
#                 ''')
# conn.commit()

cursor.execute('SELECT * FROM Studying.dbo.Test')

for row in cursor:
    print(row)