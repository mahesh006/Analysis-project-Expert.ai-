import sqlite3



#CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT, analysis real)"
CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS entries
                    (content TEXT, analysis TEXT)'''


CREATE_ENTRY = "INSERT INTO entries VALUES (?,  ?)"
RETRIEVE_ENTRIES = "SELECT * FROM entries"
sql = 'DELETE FROM entries'

def create_tables():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE)


def create_entry(content, analysis):
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_ENTRY, (content,analysis))


def retrieve_entries():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES)
        return cursor.fetchall()

def delete_entries():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()



CREATE_TABLE_STORE = '''CREATE TABLE IF NOT EXISTS playstore
                    (content TEXT, analysis TEXT)'''

CREATE_ENTRY_STORE = "INSERT INTO playstore VALUES (?,?)"
RETRIEVE_ENTRIES_STORE = "SELECT * FROM playstore"

sql_STORE = 'DELETE FROM playstore'

def create_tables_playstore():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE_STORE)


def create_entry_playstore(content, analysis):
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_ENTRY_STORE, (content, analysis))


def retrieve_entries_playstore():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES_STORE)
        return cursor.fetchall()

def delete_entries_playstore():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(sql_STORE)
        connection.commit()