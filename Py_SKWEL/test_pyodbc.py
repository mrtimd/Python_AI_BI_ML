#test_pyodbc.py
#The sample code is simplified for clarity, and doesn't necessarily represent best practices recommended by Microsoft.

import pyodbc
server='FRANKENSTIENSMO'
database='AdventureWorks2014'
username='sa'
password='Password95'
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};  SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Run a query
#cursor.execute("SELECT @@version")
cursor.execute("SELECT Name FROM Production.Product FOR JSON AUTO;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

#Sample insert query

#count = cursor.execute("""
#INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
#VALUES (?,?,?,?,?)""",
#'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
#cnxn.commit()
#print('Rows inserted: ' + str(count))

#---Tims Notes 082022
#Azure connect may look like this: server = 'tcp:myserver.database.windows.net' 

#SELECT *   FROM [T_SQL_2018].[HR].[Employees]

#FRANKENSTIENSMO
#T_SQL_2018
#SELECT @@SERVERNAME
#-----------
#Another connection to test - https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/

""" import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM products')

for i in cursor:
    print(i) """

#To Panda dataframe portion
#When applying pd.read_sql_query, don’t forget to place the connection string variable at the end. In our case, the connection string variable is conn.

""" import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT * FROM products', conn)

print(df)
print(type(df)) """