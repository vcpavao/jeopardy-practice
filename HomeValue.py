#!/Library/Frameworks/Python.framework/Versions/3.6/bin python3

import sqlite3 as db
from sqlite3 import Error
from sklearn import datasets
from sklearn import svm

"""
Creates connection to SQLite database
"""
def create_connection(db_file):
    try:
        conn = db.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None
"""
Selects random clue from database
"""
def select_clue(conn):
    incorrect_ids = []
    cur = conn.cursor()
    while True: # selects a random row from database
        cur.execute("SELECT * FROM documents ORDER BY RANDOM() LIMIT 1;")
        clue_id, clue, answer = cur.fetchone()
        category = cur.execute("SELECT category FROM categories WHERE id = ? LIMIT 1;", (clue_id,))
        category = cur.fetchone()
        print()
        print("CATEGORY: ", category)
        print(clue)
        # compare user answer with actual answer
        usr_answer = input()
        if usr_answer != answer:
            print(answer)
            incorrect_ids.append(clue_id)
        else:
            print("Correct!")
        
 
 
def main():
    print("Running SQLite", db.sqlite_version)
    # path to database of parsed jeopardy clues from j-archive.com
    path = "/Users/vcpavao/jeopardy-parser/clues.db"
    
    # create a database connection
    conn = create_connection(path)
    with conn:           
        # Select clues from database
        select_clue(conn)
        
        # If correct, forget about it, add result to statistics
        # If incorrect, mark it as incorrect, add result to statistics
        # Statistics = % of questions answered right in category

if __name__ == '__main__':
    main()
