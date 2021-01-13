import sqlite3 as db
from sqlite3 import Error
#from sklearn import datasets
#from sklearn import svm

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
    total = 0
    correct = 0
    cur = conn.cursor()
    while True: # selects a random row from database
        cur.execute("SELECT * FROM documents ORDER BY RANDOM() LIMIT 1;")
        clue_id, clue, answer = cur.fetchone()
        category = cur.execute("SELECT category FROM classifications, categories WHERE id = category_id and clue_id = ?;", (clue_id,))
        category = cur.fetchone()
        print()
        print("CATEGORY: ", category)
        print(clue)
        # compare user answer with actual answer
        usr_answer = input()
        if usr_answer.lower() in answer.lower() and len(usr_answer) > 1 :
            print("Correct!")
            correct += 1
        else :
            print("ANSWER: ", answer)
            incorrect_ids.append(clue_id)
        total += 1
        pct = 100 * correct/total
        print(pct , "%")
        
 
 
def main():
    print("Running SQLite", db.sqlite_version)
    # path to database of parsed jeopardy clues from j-archive.com
    path = "/Users/Victor/Documents/GitHub/jeopardy-parser/clues.db"
    
    # create a database connection
    conn = create_connection(path)
    with conn:           
        # Select clues from database
        select_clue(conn)
        """
        If correct, forget about it, add result to statistics
        If incorrect, mark it as incorrect, add result to statistics
        Statistics = % of questions answered right in category
        """

if __name__ == '__main__':
    main()
