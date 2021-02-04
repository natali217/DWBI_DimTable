import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendarUSA
import calendar
import datetime
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

#cursor.execute('SELECT * FROM Studying.dbo.Test')
#for row in cursor:
#    print(row)

# pandas doesn't provide method to calculate number of weeks in a month. Here is a solution for this:
def week_of_month(tgtdate):
    tgtdate = tgtdate.to_pydatetime()

    days_this_month = calendar.mdays[tgtdate.month]
    for i in range(1, days_this_month):
        d = datetime.datetime(tgtdate.year, tgtdate.month, i)
        if d.day - d.weekday() > 0:
            startdate = d
            break
    return (tgtdate - startdate).days //7 + 1


def fill_date_table(start='01/01/2020', end='12/31/2020'):
    date = pd.DataFrame(pd.date_range(start, end, freq='D'))
    df = pd.DataFrame({"Date": pd.date_range(start, end)})
    df["Date"] = pd.to_datetime(df.Date)
    df["DateKey"] = df["Date"].dt.strftime('%Y%m%d')
    df["DayOfMonth"] = df.Date.dt.day
    df["DayName"] = df.Date.dt.day_name()
    df["DayOfWeek"] = df.Date.dt.dayofweek + 1
    df["WeekOfMonth"] = date[0].apply(week_of_month)
    df["WeekOfYear"] = df.Date.dt.isocalendar().week
    df["Month"] = df.Date.dt.month
    df["MonthName"] = df.Date.dt.month_name()
    df["Quarter"] = df.Date.dt.quarter
    df["Year"] = df.Date.dt.year
    df["YearHalf"] = (df.Date.dt.quarter + 1) // 2
    df["IsWeekend"] = ((df.Date.dt.dayofweek + 1) > 5)
    df["IsWeekday"] = ((df.Date.dt.dayofweek + 1) < 6)
    df["IsHolidayUSA"] = df.Date.isin(calendarUSA().holidays(df.Date.min(), df.Date.max()))
    df["Date"] = df["Date"].dt.strftime('%m/%d/%Y')
    return df



cursor.execute(fill_date_table())