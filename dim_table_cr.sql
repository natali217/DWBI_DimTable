USE Studying;

CREATE TABLE DATE_DIM 
(
    [Date] CHAR(10),
    [DateKey] INT PRIMARY KEY,
    [DayOfMonth] VARCHAR(2),
    [DayName] VARCHAR(10),
    [DayOfWeek] CHAR(1),
    [WeekOfMonth] CHAR(1),
    [WeekOfYear] VARCHAR(2),
    [Month] VARCHAR(2),
    [MonthName] VARCHAR(10),
    [Quarter] CHAR(1),
    [Year] CHAR(4),
    [YearHalf] CHAR(1),
    [IsWeekend] BIT,
    [IsWeekday] BIT,
    [IsHolidayUSA] BIT
);

USE Studying;
SELECT * FROM Person;

USE Studying;
CREATE TABLE Test(
	[Name] VARCHAR(30),
	[AGE] INT);

USE Studying;
DROP TABLE Test;

USE Studying;
SELECT * FROM dbo.Test;