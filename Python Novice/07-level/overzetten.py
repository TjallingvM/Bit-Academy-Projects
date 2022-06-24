'''
Auteur: Tjalling van Mourik
Datum: 04-04-2022

overzetten.py:
De voorbeelduitwerking van Python Novice -> 7. Python Extended -> 2. Tabel Overzetten

Schrijf een Pythonbestand wat de volgende stappen uitvoert:

Maak een nieuwe database genaamd python_novice en een nieuwe tabel genaamd 'users' aan in de Mysql Database.
Lees alle gegevens uit het bestand 'gebruikers.json';
Voeg van elke gebruiker hun naam, gender, leeftijd en lievelingskleur toe aan de tabel 'users';
Print "Geslaagd!" als het hele bestand is overgezet.
'''

import json
import mysql.connector

db_name = "python_novice"
# Create new database 'python_novice'
mydb = mysql.connector.connect(host="localhost",user="root")
mycursor = mydb.cursor()
mycursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
mycursor.execute(f"CREATE DATABASE {db_name}")
mycursor.execute(f"USE {db_name}")

# Get JSON file en convert to dict
with open("gebruikers.json") as json_file:
    user_dict = json.load(json_file)

# Read dict, convert to list
user_list = []
for user in user_dict:
    user_list.append((user['name'],user['gender'],user['age'],user['fav_color']))

# and create new table 'users' with this list
sql_table_drop = "DROP TABLE IF EXISTS users"
sql_table_create = """CREATE TABLE users (naam VARCHAR(255), gender VARCHAR(255), leeftijd INT, lievelingskleur VARCHAR(255))"""

mycursor.execute(sql_table_drop)
mycursor.execute(sql_table_create)

sql_add_user = "INSERT INTO users VALUES (%s,%s,%s,%s)"
mycursor.executemany(sql_add_user,user_list)
mydb.commit()
if mycursor.rowcount == len(user_dict):
    print("Geslaagd!")
