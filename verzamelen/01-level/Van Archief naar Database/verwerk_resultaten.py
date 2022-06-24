import csv
import mysql.connector
import sys
import os

#Create and use database
mara_db = mysql.connector.connect(host="localhost",user="bit_academy", password="bit_academy")
mara_cursor = mara_db.cursor()
db_name = "marathons"
mara_cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
mara_cursor.execute(f"CREATE DATABASE {db_name}")
mara_cursor.execute(f"USE {db_name}")

rows=[]

def add_csvfile(file_name):
    #inport csv-file as header and rows
    name = f"{os.getcwd()}/archive/{file_name}.csv"
    with open(name, "r", encoding='mac-roman') as file:
        print(f"Verwerk bestand{file_name}.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)


for file in range(1897,2017):
    add_csvfile(file)

print("CSV-bestand in de MySQL-database aan het laden...")
#create new table and fill it with rows (header is set manually)
sql_table_drop = "DROP TABLE IF EXISTS marathon"
sql_table_create = """CREATE TABLE marathon (year INT NOT NULL,
                                            winner VARCHAR(255) NOT NULL,
                                            gender ENUM ("Male","Female") NOT NULL,
                                            country VARCHAR(255) NOT NULL,
                                            time TIME NOT NULL,
                                            marathon VARCHAR(255) NOT NULL)"""

mara_cursor.execute(sql_table_drop)
mara_cursor.execute(sql_table_create)

sql_add_marathons = "INSERT INTO marathon VALUES (%s,%s,%s,%s,%s,%s)"
mara_cursor.executemany(sql_add_marathons,rows)
mara_db.commit()
if mara_cursor.rowcount == len(rows):
    print("Klaar!")