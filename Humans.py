import sqlite3

connect = sqlite3.connect("database_2.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS 
Humans (
passport_id INTEGER PRIMARY KEY,
name TEXT,
surname TEXT,
ref_to_auto TEXT);
""")

connect.commit()

passport_id = input("Please enter your passport number: ")
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
ref_to_auto = input("Please enter the model of your car: ")

P="insert into Humans (passport_id, name, surname, ref_to_auto) values ('"+passport_id+"','"+name+"','"+surname+"','"+ref_to_auto+"')"

cursor.execute(P)

connect.commit()

cursor.execute("""
UPDATE Humans
SET name = "Olya"
WHERE name = "Oleg"
""")

connect.commit()

fetch_all_query = cursor.execute("""
                                 SELECT * from Humans;
                                 """)

print(fetch_all_query.fetchall())