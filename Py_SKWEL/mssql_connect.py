#msql_connect.py

import pandas as pd
import pyodbc

server='FRANKENSTIENSMO'
database='AdventureWorks2014'
username='sa'
password='Password95'
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};  SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print("Fetchone from SQL query:")
#Run a query
#cursor.execute("SELECT @@version")
data = cursor.execute("SELECT Name FROM Production.Product;")
#cursor.execute("SELECT Name FROM Production.Product FOR JSON AUTO;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

#Load from MS SQL to Panda dataframe
df = pd.read_sql_query('SELECT Name FROM Production.Product', cnxn)
print("SQL query to Panda dataframe")
print(df)
print(type(df))