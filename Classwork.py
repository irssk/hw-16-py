import sqlite3
connect = sqlite3.connect("database.db")
cursor = connect.cursor()

Tb_name = "Fruit"
data = "name TEXT, color TEXT"
cols = "name, color"
name_color = "'lemon', 'yellow'"


def create_table(cursor, Tb_name, data):
    todo = f"""
    CREATE TABLE IF NOT EXISTS 
    {Tb_name} ({data})"""
    cursor.execute(todo)
    connect.commit()

create_table(cursor, Tb_name, data)

def insert_info(cursor, Tb_name, name_color):
    todo = f"""
    INSERT INTO {Tb_name} ({cols}) VALUES ({name_color})
    """
    cursor.execute(todo)
    connect.commit()

insert_info(cursor, Tb_name, name_color)