import sqlite3

connect = sqlite3.connect("database_2.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
Home (
home_id INTEGER PRIMARY KEY AUTOINCREMENT ,
area INT,
address TEXT,
owner TEXT);
""")

connect.commit()

area = input("Please enter the area of your house: ")
address = input("Please enter the address where you live: ")
owner = input("Please enter who the house owner is: ")

P="insert into Home (area, address, owner) values ('"+area+"','"+address+"','"+owner+"')"

cursor.execute(P)

connect.commit()

fetch_all_query = cursor.execute("""
                                 SELECT * from Home;
                                 """)

print(fetch_all_query.fetchall())

cursor.execute("""
DELETE FROM Home WHERE home_id = 1;
""")

connect.commit()