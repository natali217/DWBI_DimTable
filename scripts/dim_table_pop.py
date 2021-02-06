import sys
import pyodbc
import pandas as pd
from datetime import datetime

###################################################################
# region 1 connect to the database 

# set local variables
server_name = 'LAPTOP-23GC4NEK'
database_name = 'Studying'

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      f'Server={server_name};'
                      f'Database={database_name};'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
print("DATABASE CONNECTED SUCCESSFULLY")

# endregion

###################################################################
# region 2 create a dimention table

with open('dim_table_cr.sql') as sql_file:
    cr_querry = sql_file.read()

cursor.execute(cr_querry)
conn.commit()
print('DIMENTION TABLE CREATED SUCCESSFULLY')

# endregion

###################################################################
# region 3 generate data

# set start and end data to generate
start = '1/1/2020'
end = '31/12/2020'

data_frame = pd.DataFrame({"Date": pd.date_range(start, end)})
data_frame["Date"] = pd.to_datetime(data_frame.Date)
data_frame["DateKey"] = data_frame["Date"].dt.strftime('%Y%m%d')
data_frame["DayOfMonth"] = data_frame.Date.dt.day
data_frame["DayName"] = data_frame.Date.dt.day_name()
data_frame["DayNameShort"] = data_frame.Date.dt.strftime('%a')
data_frame["DayOfWeek"] = data_frame.Date.dt.dayofweek + 1
data_frame["WeekOfYear"] = data_frame.Date.dt.isocalendar().week
data_frame["Month"] = data_frame.Date.dt.month
data_frame["MonthName"] = data_frame.Date.dt.month_name()
data_frame["MonthNameShort"] = data_frame.Date.dt.strftime('%b')
data_frame["Quarter"] = data_frame.Date.dt.quarter
data_frame["Year"] = data_frame.Date.dt.year
data_frame["YearHalf"] = (data_frame.Date.dt.quarter + 1) // 2
data_frame["IsWeekend"] = ((data_frame.Date.dt.dayofweek + 1) > 5)
data_frame["IsWeekday"] = ((data_frame.Date.dt.dayofweek + 1) < 6)
data_frame["Date"] = data_frame["Date"].dt.strftime('%m/%d/%Y')

# save data to csv
data_frame.to_csv(r'data.csv', index=False, header=True)
print('DATA GENERATED SUCCESSFULLY')

# endregion

###################################################################
# region 4 ETL process

# get data from csv file
data_file = 'data.csv'
data = pd.read_csv(data_file)

# insert data into database
for i in data.itertuples():
    cursor.execute("""INSERT INTO Studying.dbo.DateDim
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   i.Date,
                   i.DateKey,
                   i.DayOfMonth,
                   i.DayName,
                   i.DayNameShort,
                   i.DayOfWeek,
                   i.WeekOfYear,
                   i.Month,
                   i.MonthName,
                   i.MonthNameShort,
                   i.Quarter,
                   i.Year,
                   i.YearHalf,
                   i.IsWeekend,
                   i.IsWeekday
                   )

print('...')
conn.commit()
conn.close()
print("ETL PROCESS COMPLETED SUCCESSFULLY")

# endregion