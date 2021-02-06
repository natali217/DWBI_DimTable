DOCUMENTATION

INTRO

Task to do: create a solution which can be applied across all databases used in department and integrated to  CI/CD pipelines.

Technical details: Solution is splited into 2 parts.

-1 part - SQL scripts designed for creation of the table, should be implemented as DROP/CREATE. This SQL script should be called into database via executor(here is Python)

-2 part - ETL scripts for data population.

IMPLEMENTATION

Project has 4 files: 

First part
SQL scripts designed 

Second part

1 Database connection:
Connection to the database was implemented using pyodbc library.

2 Creation of dimension table

3 Data generation:

4 Data population:


RESULTS
