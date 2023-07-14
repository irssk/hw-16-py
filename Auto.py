import sqlite3

connect = sqlite3.connect("database_2.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
Auto (
auto_id INTEGER PRIMARY KEY AUTOINCREMENT ,
label TEXT,
color TEXT,
number INT);
""")

connect.commit()

label = input("Please enter the model of your car: ")
color = input("Please enter the color of your car: ")
number = input("Please enter the number of your car: ")

P="insert into Auto (label, color, number) values ('"+label+"','"+color+"','"+number+"')"

cursor.execute(P)

fetch_all_query = cursor.execute("""
                                 SELECT * from Auto;
                                 """)

print(fetch_all_query.fetchall())