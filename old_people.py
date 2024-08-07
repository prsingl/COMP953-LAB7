"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
import sqlite3
import pandas as pd
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Query the database for people aged 50 or older
    c.execute('''
        SELECT name, age FROM people WHERE age >= 50
    ''')

    # Fetch all results
    old_people = c.fetchall()

    # Close the connection
    conn.close()

    return old_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for name, age in name_and_age_list:
        print(f'{name}, {age} years old')

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # Convert list of tuples to a pandas DataFrame
    df = pd.DataFrame(name_and_age_list, columns=['Name', 'Age'])

    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)

if _name_ == '_main_':
    main()