"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(_file_))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create the people table
    c.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # Initialize the Faker library
    fake = Faker()

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Generate and insert 200 fake people
    for _ in range(200):
        name = fake.name()
        age = fake.random_int(min=18, max=90)
        email = fake.email()
        c.execute('''
            INSERT INTO people (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if _name_ == '_main_':
    main()