-- drop the table if it is exist
USE Studying;
DROP TABLE IF EXISTS DateDim;

-- create date dimention table
CREATE TABLE DateDim
(
    [Date] CHAR(10) NOT NULL,
    [DateKey] INT PRIMARY KEY NOT NULL,
    [DayOfMonth] VARCHAR(2) NOT NULL,
    [DayName] VARCHAR(10) NOT NULL,
    [DayNameShort] VARCHAR(3) NOT NULL,
    [DayOfWeek] CHAR(1) NOT NULL,
    [WeekOfYear] VARCHAR(2) NOT NULL,
    [Month] VARCHAR(2) NOT NULL,
    [MonthName] VARCHAR(10) NOT NULL,
    [MonthNameShort] VARCHAR(3) NOT NULL,
    [Quarter] CHAR(1) NOT NULL,
    [Year] CHAR(4) NOT NULL,
    [YearHalf] CHAR(1) NOT NULL,
    [IsWeekend] BIT NOT NULL,
    [IsWeekday] BIT NOT NULL,
);


-- select data from created and populated table
USE Studying;
SELECT * FROM DateDim;
