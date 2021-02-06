DOCUMENTATION 

INTRO 

 
Task to do: create a solution, which can be applied across all databases used in department and integrated to  CI/CD pipelines. 

Technical details: Solution is splited into 2 parts: 

-1 part - SQL scripts designed for creation of the table, should be implemented as DROP/CREATE. This SQL script should be called into database via executor(here is Python). 

-2 part - ETL script for data population. 

 
IMPLEMENTATION 

Project has 4 files:  

dim_table_cr.sql - main SQL script, where the dimention table is created; 
dim_table_pop.py - file where created the connection to the database, data generation and the ETL process. 
my_info.txt - general information about creator; 
README.md(documentation) - general documentation of the project. 

First part 

Designing the SQL script for table creation. Aslo check, if the table exists. If yes – drop it. 

 
Second part 

1.Database connection: 
Connection to the database was implemented using pyodbc library. Here you indicate name of the database server and the exact database. 

2.Creation of dimension table:
Then the dim_table_cr.sql is read to create the actual table. 

3.Data generation: 
At that part the period of dates are set and the generated data using pandas library  are saved into csv file.			 
4.Data population: 
The last part is involved the main ETL process. That means that the csv file is read and tha data populate the table. 

 
HOW TO RUN THE PROJECT 

Run the command in the rigth file location in terminal to start the project:  
                            python dim_table_pop.py 

RESULTS 

Firstly, the created table is empty.
After running the file, the terminat tell that everything execute successfully. 
Finally, after execution the SELECT * FROM DateDim command in SSMS, the table will be filled with data. 
