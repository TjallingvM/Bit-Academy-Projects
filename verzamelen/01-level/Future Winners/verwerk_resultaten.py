import csv
import mysql.connector
import sys

#Controle of er een bestand is meegegeven in programma-aanroep
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    print("ERROR: Geen bestandsnaam geleverd!")
    exit()

#Create and use database
mara_db = mysql.connector.connect(host="localhost",user="bit_academy", password="bit_academy")
mara_cursor = mara_db.cursor()
db_name = "marathons"
mara_cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
mara_cursor.execute(f"CREATE DATABASE {db_name}")
mara_cursor.execute(f"USE {db_name}")

#inport sql file as header and rows
rows = []
with open("marathon_results.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

#inport sql user_file as header and rows
with open(input_file, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

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
    print("Bestand succesvol geladen!")